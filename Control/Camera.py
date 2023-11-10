import time
from threading import Thread
import cv2
import numpy as np
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import face_recognition as FaceRecognitionCV
from Control.DB_Connection import Connection
from Control.DataCrud import CRUD
from Control.LiveUpdate import LiveUpdate
from Model.STUDENT import Student

path = f"..\\Files\\haarcascade_frontalface_default.xml"


class Camera(QThread):
    Frames = QtCore.pyqtSignal(np.ndarray)
    TheID = QtCore.pyqtSignal(np.ndarray)
    LiveImage = []

    def __init__(self, id_cam=0, Video=QPixmap, state=True):
        super().__init__()
        self.capture = cv2.VideoCapture(id_cam)
        self.Video = LiveUpdate(Video, 1080, 720)
        self.Frames.connect(self.Video.UpdateImagepixmap)
        self.faceLoc = None
        self.image = []
        self.face = None
        self.detect = False
        self.isvalid = False
        self.TheStudent = Student()
        self.SqlImageEncoded = []
        self.SqlImageName = []
        self.cascPath = path
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.state = state

    def UpdateData(self):
        try:
            if Connection().connector() is not None:
                IDs, self.SqlImageName, self.SqlImageEncoded = CRUD.GetInstance().GetRecognitionInfo()
            else:
                pass
        except Exception:
            raise Exception("Error Update Data Recognition Information")

    def CameraRun(self):
        while True:
            success, image = self.capture.read()
            image = cv2.flip(image, 1)
            self.LiveImage = image
            self.Frames.emit(image)
            if cv2.waitKey(1) & 0xFF == ord('q') or self.state is False:
                cv2.destroyAllWindows()
                pass
            else:
                if self.detect:
                    if self.isvalid:
                        y1, x1, y2, x2 = self.faceLoc
                        cv2.rectangle(self.LiveImage, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cv2.rectangle(self.LiveImage, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(self.LiveImage, self.TheStudent.get_name(), (x1 + 6, y2 - 6),
                                    cv2.FONT_HERSHEY_PLAIN, 1,
                                    (100, 0, 200),
                                    3)
                        cv2.putText(self.LiveImage, "The Student ID : " + str(self.TheStudent.get_id()), (10, 30),
                                    cv2.FONT_HERSHEY_PLAIN, 2,
                                    (0, 255, 0),
                                    3)
                        cv2.putText(self.LiveImage, "The Student Name : " + str(self.TheStudent.get_name()), (10, 60),
                                    cv2.FONT_HERSHEY_PLAIN, 2,
                                    (0, 255, 0),
                                    3)
                    else:
                        y1, x1, y2, x2 = self.faceLoc
                        cv2.rectangle(self.LiveImage, (x1, y1), (x2, y2), (0, 0, 255), 3)
                        cv2.rectangle(self.LiveImage, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                        cv2.putText(self.LiveImage, self.TheStudent.get_name() + ":BLOCKED", (x1 + 6, y2 - 6),
                                    cv2.FONT_HERSHEY_PLAIN, 1,
                                    (100, 0, 200), 3)
                        cv2.putText(self.LiveImage, "The Student ID : " + str(self.TheStudent.get_id()), (10, 30),
                                    cv2.FONT_HERSHEY_PLAIN, 2,
                                    (0, 255, 0),
                                    3)
                        cv2.putText(self.LiveImage, "The Student Name : " + str(self.TheStudent.get_name()), (10, 60),
                                    cv2.FONT_HERSHEY_PLAIN, 2,
                                    (0, 255, 0),
                                    3)
                else:
                    faces = self.faceCascade.detectMultiScale(self.LiveImage)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(self.LiveImage, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(self.LiveImage, "Unknown", (x + 6, y - 6), cv2.FONT_HERSHEY_PLAIN, 1,
                                    (100, 0, 200), 3)

                cv2.imshow("Reconstruction", image)
        self.capture.release()

    def Recognition(self):
        self.UpdateData()
        time.sleep(2)
        while True:
            if len(self.SqlImageName) > 0 and self.state:
                try:
                    facesCurFrame = FaceRecognitionCV.face_locations(self.LiveImage)
                    encodesCurFrame = FaceRecognitionCV.face_encodings(self.LiveImage, facesCurFrame)
                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                        matches = FaceRecognitionCV.compare_faces(self.SqlImageEncoded, encodeFace)
                        findDistance = FaceRecognitionCV.face_distance(self.SqlImageEncoded, encodeFace)
                        matchIndex = np.argmin(findDistance)
                        if matches[matchIndex]:
                            name = self.SqlImageName[matchIndex]
                            self.detect = True
                            self.faceLoc = faceLoc
                            self.TheStudent = Student()
                            self.TheStudent = CRUD.GetInstance().GetDataName(name)
                            self.isvalid = self.TheStudent.get_isvalid()
                        else:
                            self.detect = False
                            self.isvalid = False

                except Exception:
                    raise Exception(" Recognition error")
            else:
                pass

    def run(self):
        try:
            thread1 = Thread(target=self.CameraRun)
            thread2 = Thread(target=self.Recognition)

            thread1.start()
            thread2.start()

            while thread1.is_alive() or thread2.is_alive():
                thread1.join()
                thread2.join()
        except (KeyboardInterrupt, SystemExit):
            print("error")


if __name__ == '__main__':
    pass
