import cv2
import face_recognition
import numpy as np
from Control import DB_Connection
from Control.DB_Connection import Connection
from Model.STUDENT import Student


class CRUD(DB_Connection.Connection, Student):
    __instance = None

    @staticmethod
    def GetInstance():
        """ Static access method. """
        if CRUD.__instance is None:
            CRUD()
        return CRUD.__instance

    def __init__(self, student=None):
        if CRUD.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CRUD.__instance = self

        super().__init__()
        if not (student is None):
            self.id = student.get_id()
            self.name = student.get_name()
            self.department = student.get_department()
            self.stages = student.get_stage()
            self.type = student.get_type()
            self.image = student.get_image()
            self.isvalid = student.get_isvalid()

    def Insert(self, student):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = "INSERT INTO `students`(`id`, `name`, `department`, `stage`, `type`, `image`, `isvalid`)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (int(student.get_id()), student.get_name(), student.get_department(),
               student.get_stage(), student.get_type(), student.get_image(), student.get_isvalid())
        try:
            cur.execute(sql, val)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def Update(self, student, the_id: int):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)

        sql = f"UPDATE `students` SET `id`=%s,`name`=%s,`department`=%s,`stage`=%s," \
              f"`type`=%s,`image`=%s,`isvalid`=%s WHERE `id`={the_id}"
        val = (student.get_id(), student.get_name(), student.get_department(),
               student.get_stage(), student.get_type(), student.get_image(), student.get_isvalid())
        try:
            cur.execute(sql, val)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def Delete(self, the_id: int):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"DELETE FROM `students` WHERE `id`= {the_id}"
        try:
            cur.execute(sql)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def GetDataById(self, the_id: int) -> Student:
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT * FROM `students` WHERE id={the_id}"
        student_info = Student()
        try:
            cur.execute(sql)
            result = cur.fetchone()
            student_info.set_id(result['id'])
            student_info.set_name(result['name'])
            student_info.set_department(result['department'])
            student_info.set_stage(result['stage'])
            student_info.set_type(result['type'])
            student_info.set_image(result['image'])
            student_info.set_isvalid(result['isvalid'])
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

        return student_info

    def GetDataName(self, the_name: str) -> Student:
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT * FROM `students` WHERE `name`=%s"
        val = (the_name,)
        student_info = Student()
        try:
            cur.execute(sql, val)
            result = cur.fetchone()
            student_info.set_id(result['id'])
            student_info.set_name(result['name'])
            student_info.set_department(result['department'])
            student_info.set_stage(result['stage'])
            student_info.set_type(result['type'])
            student_info.set_image(result['image'])
            student_info.set_isvalid(result['isvalid'])
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()
        return student_info

    def UpdateImage(self, the_id: int, image):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"UPDATE `students` SET `image`=%s WHERE `id`=%s"
        val = (image, the_id)
        try:
            cur.execute(sql, val)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def Encoding(self, image_path: str) -> list:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        return encode

    def AddImageDecoded(self, s_id: int, s_name: str, s_image: str):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"INSERT INTO `recognition`(`student_id`, `student_name`, `image_encoded`) VALUES (%s,%s,%s)"
        image = self.Encoding(s_image)
        image = np.array(image).tobytes()
        val = (s_id, s_name, image)
        try:
            cur.execute(sql, val)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def GetImageBinary(self, the_id: int):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT `image` FROM `students` WHERE `id`={the_id}"
        image = []
        try:
            cur.execute(sql)
            result = cur.fetchone()
            image = result["image"]
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()
        return image

    def GetRecognitionInfo(self):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT * FROM `recognition`"
        ids = []
        names = []
        encoded = []
        try:
            cur.execute(sql)
            result = cur.fetchall()
            for data in result:
                ids.append(data['student_id'])
                names.append(data['student_name'])
                encoded.append(np.frombuffer(data['image_encoded']))
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()
        return ids, names, encoded

    def Validate(self, valid: int, the_id: int):
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"UPDATE `students` SET `isvalid`={valid} WHERE id={the_id} "
        try:
            cur.execute(sql)
            myconn.connection.commit()
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def IsFound(self, the_id: int) -> bool:
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT * FROM `students` WHERE `id`= {the_id} "
        try:
            cur.execute(sql)
            data = cur.fetchall()
            if len(data) <= 0 or data is None:
                return False
            else:
                return True
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def IsFoundName(self, the_name: str) -> bool:
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT * FROM `students` WHERE `name`= %s "
        val = (the_name,)
        try:
            cur.execute(sql, val)
            data = cur.fetchall()
            if len(data) <= 0 or data is None:
                return False
            else:
                return True
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()

    def IsValid(self, the_id: int) -> bool:
        myconn = Connection()
        cur = myconn.connector().cursor(dictionary=True)
        sql = f"SELECT `isvalid` FROM `students` WHERE `id`= {the_id} "
        try:
            cur.execute(sql)
            data = cur.fetchone()
            if data["isvalid"] == 1:
                return True
            else:
                return False
        except (TypeError, NameError):
            myconn.connection.rollback()
        finally:
            myconn.connection.close()


if __name__ == '__main__':

    pass
