# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def __init__(self, Main):
        Main.setObjectName("Main")
        Main.resize(1366, 715)
        self.s1_take = QtWidgets.QPushButton(Main)
        self.s1_take.setGeometry(QtCore.QRect(900, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_take.setFont(font)
        self.s1_take.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_take.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: rgb(255,0,255);\n"
                                   "border-color: rgb(0, 85, 127);\n"
                                   "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.s1_take.setObjectName("s1_take")
        self.label_8 = QtWidgets.QLabel(Main)
        self.label_8.setGeometry(QtCore.QRect(20, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.s1_update = QtWidgets.QPushButton(Main)
        self.s1_update.setGeometry(QtCore.QRect(740, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_update.setFont(font)
        self.s1_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_update.setStyleSheet("border-radius: 8px;\n"
                                     "background-color: rgb(0,255,255);\n"
                                     "border-color: rgb(0, 85, 127);\n"
                                     "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                     "font-family: \"Times New Roman\";\n"
                                     "font-weight: bold;")
        self.s1_update.setObjectName("s1_update")
        self.s1_search_id = QtWidgets.QLineEdit(Main)
        self.s1_search_id.setGeometry(QtCore.QRect(160, 580, 181, 31))
        self.s1_search_id.setStyleSheet("background-color: rgb(60,179,113);\n"
                                        "border-color: rgb(0, 85, 127);\n"
                                        "border-radius: 10px;\n"
                                        "padding:5px;\n"
                                        "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                        "font-family: \"Times New Roman\";\n"
                                        "font-weight: bold;")
        self.s1_search_id.setObjectName("s1_search_id")
        self.s1_insert = QtWidgets.QPushButton(Main)
        self.s1_insert.setGeometry(QtCore.QRect(610, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_insert.setFont(font)
        self.s1_insert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_insert.setStyleSheet("border-radius: 8px;\n"
                                     "background-color: rgb(0,255,0);\n"
                                     "border-color: rgb(0, 85, 127);\n"
                                     "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                     "font-family: \"Times New Roman\";\n"
                                     "font-weight: bold;")
        self.s1_insert.setObjectName("s1_insert")
        self.s1_Review_image = QtWidgets.QLabel(Main)
        self.s1_Review_image.setGeometry(QtCore.QRect(900, 110, 450, 400))
        self.s1_Review_image.setStyleSheet("border-style: solid;\n"
                                           "border-color: rgb(0,0,128);\n"
                                           "border-width: 5px;\n"
                                           "border-radius: 10px;\n"
                                           "padding: 1px;\n"
                                           "")
        self.s1_Review_image.setText("")
        self.s1_Review_image.setScaledContents(True)
        self.s1_Review_image.setObjectName("s1_Review_image")
        self.s1_AddImage = QtWidgets.QPushButton(Main)
        self.s1_AddImage.setGeometry(QtCore.QRect(1070, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_AddImage.setFont(font)
        self.s1_AddImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_AddImage.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: rgb(255,0,255);\n"
                                       "border-color: rgb(0, 85, 127);\n"
                                       "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                       "font-family: \"Times New Roman\";\n"
                                       "font-weight: bold;")
        self.s1_AddImage.setObjectName("s1_AddImage")
        self.s1_name = QtWidgets.QLineEdit(Main)
        self.s1_name.setGeometry(QtCore.QRect(160, 150, 181, 31))
        self.s1_name.setStyleSheet("background-color: rgb(60,179,113);\n"
                                   "border-color: rgb(0, 85, 127);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.s1_name.setObjectName("s1_name")
        self.s1_SearchId_btn = QtWidgets.QPushButton(Main)
        self.s1_SearchId_btn.setGeometry(QtCore.QRect(350, 580, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_SearchId_btn.setFont(font)
        self.s1_SearchId_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_SearchId_btn.setStyleSheet("border-radius: 8px;\n"
                                           "background-color: rgb(0,128,128);\n"
                                           "border-color: rgb(0, 85, 127);\n"
                                           "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                           "font-family: \"Times New Roman\";\n"
                                           "font-weight: bold;")
        self.s1_SearchId_btn.setFlat(False)
        self.s1_SearchId_btn.setObjectName("s1_SearchId_btn")
        self.s1_close = QtWidgets.QPushButton(Main)
        self.s1_close.setGeometry(QtCore.QRect(1210, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_close.setFont(font)
        self.s1_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_close.setStyleSheet("border-radius: 8px;\n"
                                    "background-color: rgb(255,255,0);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_close.setObjectName("s1_close")
        self.s1_RunCamera = QtWidgets.QPushButton(Main)
        self.s1_RunCamera.setGeometry(QtCore.QRect(550, 530, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_RunCamera.setFont(font)
        self.s1_RunCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_RunCamera.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(255,0,255);\n"
                                        "border-color: rgb(0, 85, 127);\n"
                                        "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                        "font-family: \"Times New Roman\";\n"
                                        "font-weight: bold;")
        self.s1_RunCamera.setObjectName("s1_RunCamera")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(20, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                 "border-radius: 10px;\n"
                                 "padding:5px;\n"
                                 "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                 "font-family: \"Times New Roman\";\n"
                                 "font-weight: bold;")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Main)
        self.label_6.setGeometry(QtCore.QRect(20, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.s1_SearchName_btn = QtWidgets.QPushButton(Main)
        self.s1_SearchName_btn.setGeometry(QtCore.QRect(350, 660, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_SearchName_btn.setFont(font)
        self.s1_SearchName_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_SearchName_btn.setStyleSheet("border-radius: 8px;\n"
                                             "background-color: rgb(0,128,128);\n"
                                             "border-color: rgb(0, 85, 127);\n"
                                             "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                             "font-family: \"Times New Roman\";\n"
                                             "font-weight: bold;")
        self.s1_SearchName_btn.setFlat(False)
        self.s1_SearchName_btn.setObjectName("s1_SearchName_btn")
        self.s1_state_label = QtWidgets.QLabel(Main)
        self.s1_state_label.setGeometry(QtCore.QRect(1220, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_state_label.setFont(font)
        self.s1_state_label.setStyleSheet("background-color: #ffc;\n"
                                          "border-color: rgb(0, 85, 127);\n"
                                          "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                          "font-family: \"Times New Roman\";\n"
                                          "font-weight: bold;\n"
                                          "padding: 6px;\n"
                                          "border-radius: 10px;\n"
                                          "")
        self.s1_state_label.setText("")
        self.s1_state_label.setObjectName("s1_state_label")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.s1_AddEncoding = QtWidgets.QPushButton(Main)
        self.s1_AddEncoding.setGeometry(QtCore.QRect(1240, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_AddEncoding.setFont(font)
        self.s1_AddEncoding.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_AddEncoding.setStyleSheet("border-radius: 10px;\n"
                                          "background-color: rgb(255,0,255);\n"
                                          "border-color: rgb(0, 85, 127);\n"
                                          "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                          "font-family: \"Times New Roman\";\n"
                                          "font-weight: bold;")
        self.s1_AddEncoding.setObjectName("s1_AddEncoding")
        self.s1_clear = QtWidgets.QPushButton(Main)
        self.s1_clear.setGeometry(QtCore.QRect(430, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_clear.setFont(font)
        self.s1_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_clear.setStyleSheet("border-radius: 8px;\n"
                                    "background-color: rgb(255,255,0);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_clear.setObjectName("s1_clear")
        self.s1_block = QtWidgets.QPushButton(Main)
        self.s1_block.setGeometry(QtCore.QRect(260, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_block.setFont(font)
        self.s1_block.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_block.setStyleSheet("border-radius: 8px;\n"
                                    "background-color: rgb(255,0,0);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_block.setObjectName("s1_block")
        self.s1_search_name = QtWidgets.QLineEdit(Main)
        self.s1_search_name.setGeometry(QtCore.QRect(160, 660, 181, 31))
        self.s1_search_name.setStyleSheet("background-color: rgb(60,179,113);\n"
                                          "border-color: rgb(0, 85, 127);\n"
                                          "border-radius: 10px;\n"
                                          "padding:5px;\n"
                                          "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                          "font-family: \"Times New Roman\";\n"
                                          "font-weight: bold;")
        self.s1_search_name.setObjectName("s1_search_name")
        self.s1_type = QtWidgets.QComboBox(Main)
        self.s1_type.setGeometry(QtCore.QRect(160, 370, 181, 31))
        self.s1_type.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_type.setStyleSheet("background-color: rgb(60,179,113);\n"
                                   "border-color: rgb(0, 85, 127);\n"
                                   "border-radius: 10px;\n"
                                   "padding:12px 0px 0px 5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.s1_type.setObjectName("s1_type")
        self.s1_type.addItem("")
        self.s1_type.addItem("")
        self.s1_delete = QtWidgets.QPushButton(Main)
        self.s1_delete.setGeometry(QtCore.QRect(1000, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_delete.setFont(font)
        self.s1_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_delete.setStyleSheet("border-radius: 8px;\n"
                                     "background-color: rgb(220,20,50);\n"
                                     "border-color: rgb(0, 85, 127);\n"
                                     "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                     "font-family: \"Times New Roman\";\n"
                                     "font-weight: bold;")
        self.s1_delete.setObjectName("s1_delete")
        self.label_5 = QtWidgets.QLabel(Main)
        self.label_5.setGeometry(QtCore.QRect(20, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.s1_valid = QtWidgets.QComboBox(Main)
        self.s1_valid.setGeometry(QtCore.QRect(160, 470, 181, 31))
        self.s1_valid.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_valid.setStyleSheet("background-color: rgb(60,179,113);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "border-radius: 10px;\n"
                                    "padding:5px;\n"
                                    "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_valid.setObjectName("s1_valid")
        self.s1_valid.addItem("")
        self.s1_valid.addItem("")
        self.s1_stage = QtWidgets.QComboBox(Main)
        self.s1_stage.setGeometry(QtCore.QRect(160, 270, 181, 31))
        self.s1_stage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_stage.setStyleSheet("background-color: rgb(60,179,113);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "border-radius: 10px;\n"
                                    "padding:5px;\n"
                                    "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_stage.setObjectName("s1_stage")
        self.s1_stage.addItem("")
        self.s1_stage.addItem("")
        self.s1_stage.addItem("")
        self.s1_stage.addItem("")
        self.s1_stage.addItem("")
        self.s1_LiveImage = QtWidgets.QLabel(Main)
        self.s1_LiveImage.setGeometry(QtCore.QRect(390, 110, 450, 400))
        self.s1_LiveImage.setStyleSheet("border-style: solid;\n"
                                        "border-color: green;\n"
                                        "border-width: 5px;\n"
                                        "border-radius: 10px;\n"
                                        "padding: 1px;")
        self.s1_LiveImage.setText("")
        self.s1_LiveImage.setScaledContents(True)
        self.s1_LiveImage.setObjectName("s1_LiveImage")
        self.s1_refresh = QtWidgets.QPushButton(Main)
        self.s1_refresh.setGeometry(QtCore.QRect(990, 660, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_refresh.setFont(font)
        self.s1_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_refresh.setStyleSheet("background-color: #ffc;\n"
                                      "border-color: rgb(0, 85, 127);\n"
                                      "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                      "font-family: \"Times New Roman\";\n"
                                      "font-weight: bold;\n"
                                      "padding: 6px;\n"
                                      "border-radius: 10px;")
        self.s1_refresh.setObjectName("s1_refresh")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.s1_id = QtWidgets.QLineEdit(Main)
        self.s1_id.setGeometry(QtCore.QRect(160, 90, 181, 31))
        self.s1_id.setStyleSheet("background-color: rgb(60,179,113);\n"
                                 "border-color: rgb(0, 85, 127);\n"
                                 "border-radius: 10px;\n"
                                 "padding:5px;\n"
                                 "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                 "font-family: \"Times New Roman\";\n"
                                 "font-weight: bold;")
        self.s1_id.setObjectName("s1_id")
        self.s1_update_image = QtWidgets.QPushButton(Main)
        self.s1_update_image.setGeometry(QtCore.QRect(870, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_update_image.setFont(font)
        self.s1_update_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_update_image.setStyleSheet("border-radius: 8px;\n"
                                           "background-color: rgb(0,200,255);\n"
                                           "border-color: rgb(0, 85, 127);\n"
                                           "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                           "font-family: \"Times New Roman\";\n"
                                           "font-weight: bold;")
        self.s1_update_image.setObjectName("s1_update_image")
        self.label_9 = QtWidgets.QLabel(Main)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 321, 41))
        self.label_9.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 16pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.s1_allow = QtWidgets.QPushButton(Main)
        self.s1_allow.setGeometry(QtCore.QRect(160, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.s1_allow.setFont(font)
        self.s1_allow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s1_allow.setStyleSheet("border-radius: 8px;\n"
                                    "background-color: rgb(0,255,0);\n"
                                    "border-color: rgb(0, 85, 127);\n"
                                    "font: 80 14pt \"MS Shell Dlg 2\";\n"
                                    "font-family: \"Times New Roman\";\n"
                                    "font-weight: bold;")
        self.s1_allow.setObjectName("s1_allow")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.s1_department = QtWidgets.QLineEdit(Main)
        self.s1_department.setGeometry(QtCore.QRect(160, 210, 181, 31))
        self.s1_department.setStyleSheet("background-color: rgb(60,179,113);\n"
                                         "border-color: rgb(0, 85, 127);\n"
                                         "border-radius: 10px;\n"
                                         "padding:5px;\n"
                                         "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                         "font-family: \"Times New Roman\";\n"
                                         "font-weight: bold;")
        self.s1_department.setObjectName("s1_department")
        self.label_7 = QtWidgets.QLabel(Main)
        self.label_7.setGeometry(QtCore.QRect(20, 470, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(58, 126, 173);\n"
                                   "border-radius: 10px;\n"
                                   "padding:5px;\n"
                                   "font: 80 12pt \"MS Shell Dlg 2\";\n"
                                   "font-family: \"Times New Roman\";\n"
                                   "font-weight: bold;")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MTK"))
        self.s1_take.setText(_translate("Main", "Take"))
        self.label_8.setText(_translate("Main", "Search by name :"))
        self.s1_update.setText(_translate("Main", "Update"))
        self.s1_insert.setText(_translate("Main", "Insert"))
        self.s1_AddImage.setText(_translate("Main", "Add"))
        self.s1_SearchId_btn.setText(_translate("Main", "Search"))
        self.s1_close.setText(_translate("Main", "Close"))
        self.s1_RunCamera.setText(_translate("Main", "Recognition"))
        self.label.setText(_translate("Main", "ID:"))
        self.label_6.setText(_translate("Main", "Search by id :"))
        self.s1_SearchName_btn.setText(_translate("Main", "Search"))
        self.label_3.setText(_translate("Main", "Department:"))
        self.s1_AddEncoding.setText(_translate("Main", "Encoding"))
        self.s1_clear.setText(_translate("Main", "Clear"))
        self.s1_block.setText(_translate("Main", "Block"))
        self.s1_type.setItemText(0, _translate("Main", "Morning Study\n"
                                                       ""))
        self.s1_type.setItemText(1, _translate("Main", "Evening Study\n"
                                                       ""))
        self.s1_delete.setText(_translate("Main", "Delete"))
        self.label_5.setText(_translate("Main", "Type:"))
        self.s1_valid.setItemText(0, _translate("Main", "Allowed"))
        self.s1_valid.setItemText(1, _translate("Main", "Blocked"))
        self.s1_stage.setItemText(0, _translate("Main", "First"))
        self.s1_stage.setItemText(1, _translate("Main", "Second"))
        self.s1_stage.setItemText(2, _translate("Main", "Third"))
        self.s1_stage.setItemText(3, _translate("Main", "Fourth"))
        self.s1_stage.setItemText(4, _translate("Main", "Fifth"))
        self.s1_refresh.setText(_translate("Main", "Refresh Connection State"))
        self.label_4.setText(_translate("Main", "Stage:"))
        self.s1_update_image.setText(_translate("Main", "Update Image"))
        self.label_9.setText(_translate("Main", "              Student Infromation"))
        self.s1_allow.setText(_translate("Main", "Allow"))
        self.label_2.setText(_translate("Main", "Name:"))
        self.label_7.setText(_translate("Main", "Valid:"))
