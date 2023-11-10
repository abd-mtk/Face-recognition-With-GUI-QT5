import os
import sys
from tkinter import filedialog
import shutil
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QDialog
from Control.Camera import Camera
from Control.DataCrud import CRUD
from Control.DB_Connection import Connection
from Model.STUDENT import Student
from View.view import Ui_Main


class MainFunctions(Ui_Main):
    def __init__(self, Main):
        super().__init__(Main=Main)
        try:
            if Connection().connector() is not None:
                self.s1_state_label.setText("Connection")
            else:
                self.s1_state_label.setText("Disconnected")
        except Exception:
            raise Exception("This Connection is not supported!")
        # =============================================================================================================
        self.s1_insert.clicked.connect(self.Insert_)
        self.s1_update.clicked.connect(self.Update_)
        self.s1_update_image.clicked.connect(self.UpdateImage_)
        self.s1_delete.clicked.connect(self.Delete_)
        self.s1_SearchId_btn.clicked.connect(self.SearchId_)
        self.s1_SearchName_btn.clicked.connect(self.SearchName_)
        self.s1_take.clicked.connect(self.Take_)
        self.s1_AddImage.clicked.connect(self.AddImage_)
        self.s1_AddEncoding.clicked.connect(self.AddEncoding_)
        self.s1_close.clicked.connect(self.Close_)
        self.s1_clear.clicked.connect(self.Clear_)
        self.s1_allow.clicked.connect(self.Allow_)
        self.s1_block.clicked.connect(self.Block_)
        self.s1_RunCamera.clicked.connect(self.RunCamera_)
        self.s1_refresh.clicked.connect(self.Refresh_)
        # =============================================================================================================
        self.RunCamera = Camera(id_cam=0, Video=self.s1_LiveImage, state=False)
        self.RunCamera.start()

    def Insert_(self):
        if self.s1_id.text().isnumeric() and not CRUD.GetInstance().IsFound(
                int(self.s1_id.text())) and self.FieldsIsEmpty():
            Path = f"..\\Temp\\TemporaryCrudImage.jpg"
            if os.path.exists(Path):
                Path = Path
                BinaryImage = self.ImageToBinary(Path)
                try:
                    student = Student(int(self.s1_id.text()), self.s1_name.text(), self.s1_department.text(),
                                      self.s1_stage.currentText(), self.s1_type.currentText(), BinaryImage,
                                      self.GetValid(self.s1_valid.currentIndex()))
                    CRUD.GetInstance().Insert(student)
                except Exception as error:
                    print(error.__context__)
                os.remove(Path)
            else:
                self.ShowDialog(message="Take photo is required")
        else:
            self.ShowDialog("Warning", "The ID is invalid")

    def Update_(self):
        if self.s1_id.text().isnumeric() and CRUD.GetInstance().IsFound(int(
                self.s1_search_id.text())) and self.FieldsIsEmpty():
            self.TemporaryImage(int(self.s1_search_id.text()))
            path = "..\\Temp\\TempSqlImage.jpg"
            image = self.ImageToBinary(path)
            student = Student(int(self.s1_id.text()), self.s1_name.text(), self.s1_department.text(),
                              self.s1_stage.currentText(), self.s1_type.currentText(), image,
                              self.GetValid(self.s1_valid.currentIndex()))
            CRUD.GetInstance().Update(student, int(self.s1_search_id.text()))
            os.remove(path)
        else:
            self.ShowDialog("WARNING", "User ID Change Failed")

    def UpdateImage_(self):
        if self.s1_id.text().isnumeric() and CRUD.GetInstance().IsFound(int(
                self.s1_search_id.text())) and self.FieldsIsEmpty():
            self.TemporaryImage(int(self.s1_id.text()))
            path = f"..\\Temp\\TemporaryCrudImage.jpg"
            if os.path.exists(path):
                image = self.ImageToBinary(path)
                CRUD.GetInstance().UpdateImage(int(self.s1_id.text()), image)
                os.remove(path)
            else:
                self.ShowDialog(message="You Must Take Photo To Update")
        pass

    def Delete_(self):
        if self.s1_search_id.text().isnumeric() and CRUD.GetInstance().IsFound(self.s1_search_id.text()):
            try:
                ID = int(self.s1_search_id.text())
                CRUD.GetInstance().Delete(ID)
                path = "..\\Temp\\TempSqlImage.jpg"
                self.s1_Review_image.setPixmap(QPixmap())
                self.Clear_()
                os.remove(path)
            except Exception:
                pass
        else:
            self.ShowDialog("Warning", "The id not exists")

    def SearchId_(self):
        if self.s1_search_id.text().isnumeric() and CRUD.GetInstance().IsFound(self.s1_search_id.text()):
            ID = int(self.s1_search_id.text())
            student = CRUD.GetInstance().GetDataById(ID)
            self.TemporaryImage(ID)
            path = "..\\Temp\\TempSqlImage.jpg"
            pixmap = QPixmap(path)
            self.s1_Review_image.setPixmap(pixmap)
            self.s1_id.setText(str(student.get_id()))
            self.s1_name.setText(str(student.get_name()))
            self.s1_department.setText(str(student.get_department()))
            self.s1_stage.setCurrentIndex(self.GetStage(student.get_stage()))
            self.s1_type.setCurrentIndex(self.GetType(student.get_type()))
            self.s1_valid.setCurrentIndex(self.SetValid(int(student.get_isvalid())))
            os.remove(path)
        else:
            self.ShowDialog("Warning", "The id not exists")

    def SearchName_(self):
        if self.s1_search_name.text().isalpha() and CRUD.GetInstance().IsFoundName(self.s1_search_name.text()):
            Name = self.s1_search_name.text()
            student = CRUD.GetInstance().GetDataName(Name)
            self.TemporaryImage(int(student.get_id()))
            path = "..\\Temp\\TempSqlImage.jpg"
            pixmap = QPixmap(path)
            self.s1_Review_image.setPixmap(pixmap)
            self.s1_id.setText(str(student.get_id()))
            self.s1_name.setText(str(student.get_name()))
            self.s1_department.setText(str(student.get_department()))
            self.s1_stage.setCurrentIndex(self.GetStage(student.get_stage()))
            self.s1_type.setCurrentIndex(self.GetType(student.get_type()))
            self.s1_valid.setCurrentIndex(self.SetValid(int(student.get_isvalid())))
            self.s1_search_id.setText(str(student.get_id()))
            os.remove(path)

        else:
            self.ShowDialog("Warning", "The Name not exists")

    def Take_(self):
        try:
            image = self.RunCamera.LiveImage
            ImageName = "TemporaryCrudImage.jpg"
            path = f"..\\Temp\\TemporaryCrudImage.jpg"
            os.chdir("..\\Temp")
            cv2.imwrite(ImageName, image)
            self.s1_Review_image.setPixmap(QPixmap(path))
        except Exception:
            raise Exception("Take Image Error")

    def CopyImage(self, path):
        try:
            Path = f"..\\Temp\\TemporaryCrudImage.jpg"
            shutil.copyfile(path, Path)
            self.s1_Review_image.setPixmap(QPixmap(path))
        except Exception:
            raise Exception("Take Image Error")

    def AddImage_(self):
        try:
            ImagePath = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=[('image files', '.jpg'), ])
            self.CopyImage(ImagePath)
        except Exception as Error:
            print(Error.__context__)

    def AddEncoding_(self):
        if self.s1_id.text().isnumeric() and CRUD.GetInstance().IsFound(int(
                self.s1_search_id.text())) and self.FieldsIsEmpty():
            try:
                path = f"..\\Temp\\TemporaryCrudImage.jpg"
                CRUD.GetInstance().AddImageDecoded(int(self.s1_id.text()), self.s1_name.text(), path)
                os.remove(path)
            except Exception:
                self.ShowDialog(message="Encoding is not WORKING")
                raise Exception("Encoding is not WORKING")
        else:
            self.ShowDialog(message="Enter the User information")

    def Allow_(self):
        if self.s1_id.text().isnumeric() and CRUD.GetInstance().IsFound(int(self.s1_id.text())):
            CRUD.GetInstance().Validate(1, self.s1_id.text())
            self.s1_valid.setCurrentIndex(0)
        else:
            self.ShowDialog("WARNING", "User ID Change Failed")

    def Block_(self):
        if self.s1_id.text().isnumeric() and CRUD.GetInstance().IsFound(int(self.s1_id.text())):
            CRUD.GetInstance().Validate(0, self.s1_id.text())
            self.s1_valid.setCurrentIndex(1)
        else:
            self.ShowDialog("WARNING", "User ID Change Failed")

    def RunCamera_(self):
        try:
            self.RunCamera.state = not self.RunCamera.state
        except Exception:
            raise Exception("state error")

    def Close_(self):
        sys.exit()

    def Clear_(self):
        self.dialog()
        self.s1_id.setText("")
        self.s1_name.setText("")
        self.s1_department.setText("")
        self.s1_search_id.setText("")
        self.s1_search_name.setText("")
        self.s1_stage.setCurrentIndex(-1)
        self.s1_type.setCurrentIndex(-1)
        self.s1_valid.setCurrentIndex(-1)
        self.s1_Review_image.setPixmap(QPixmap())

    def FieldsIsEmpty(self) -> bool:
        if self.s1_id.text() == '' or self.s1_name.text() == '' \
                or self.s1_department.text() == '' or self.s1_stage.currentIndex() < 0 \
                or self.s1_type.currentIndex() < 0 or self.s1_valid.currentIndex() < 0 \
                or not self.s1_id.text().isnumeric():
            return False
        else:
            return True

    def TemporaryImage(self, the_id: int):
        path = "..\\Temp\\TempSqlImage.jpg"
        binary_data = CRUD.GetInstance().GetImageBinary(the_id)
        self.WriteImage(binary_data, path)

    def WriteImage(self, data, filename):
        try:
            with open(filename, 'wb') as file:
                file.write(data)
                file.flush()
        except IOError:
            raise Exception("image cannot be write")
            file.close()
        finally:
            file.close()

    def ImageToBinary(self, filename):
        try:
            with open(filename, 'rb') as file:
                binaryData = file.read()
                file.flush()
            return binaryData
        except IOError:
            raise Exception("image cannot be write")
            file.close()
        finally:
            file.close()

    def GetType(self, Type: str) -> int:
        if Type.startswith("Morning", 0):
            return 0
        else:
            return 1

    def GetStage(self, Stage: str) -> int:
        if Stage == "First":
            return 0
        elif Stage == "Second":
            return 1
        elif Stage == "Third":
            return 2
        elif Stage == "Fourth":
            return 3
        elif Stage == "Fifth":
            return 4
        else:
            return -1

    def GetValid(self, Valid: int) -> bool:
        if Valid == 0:
            return True
        else:
            return False

    def SetValid(self, Valid: int) -> int:
        if Valid == 1:
            return 0
        if Valid == 0:
            return 1

    def ShowDialog(self, title: str = 'Warning', message: str = 'Error'):
        msgBox = QMessageBox()
        msgBox.setGeometry(600, 350, 200, 20)
        msgBox.setText(message)
        msgBox.setStyleSheet("width:150px;\n"
                             "height:20px;\n"
                             "font: 80 12pt \"MS Shell Dlg 2\";\n"
                             "font-family: \"Times New Roman\";\n"
                             "font-weight: bold;")
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.exec_()

    def dialog(self):
        MESSAGE = QDialog()
        MESSAGE.setGeometry(600, 350, 200, 20)

        MESSAGE.exec_()

    def Refresh_(self):
        try:
            if Connection().connector() is not None:
                self.s1_state_label.setText("Connection")
            else:
                self.s1_state_label.setText("Disconnected")
        except Exception:
            raise Exception("The connection take longer than expected")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = QtWidgets.QMainWindow()
    view = MainFunctions(ex)
    ex.show()
    sys.exit(app.exec_())
    sys.exit()
