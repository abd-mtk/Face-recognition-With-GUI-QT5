import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QThread
from PyQt5.QtGui import QPixmap


class LiveUpdate(QThread):
    def __init__(self, ImageView, width, height):
        super().__init__()
        self.ImageView = ImageView
        self.width = width
        self.height = height

    @pyqtSlot(np.ndarray)
    def UpdateImagepixmap(self, image):
        QtImage = self.ConvertCvToQt(image)
        self.ImageView.setPixmap(QtImage)

    def ConvertCvToQt(self, image):
        RgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w, ch = RgbImage.shape
        bytes_per_line = ch * w
        ConvertToQt = QtGui.QImage(RgbImage.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = ConvertToQt.scaled(self.width, self.height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(pixmap)
