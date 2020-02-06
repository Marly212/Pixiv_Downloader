import string
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from pixivpy3 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtGui import QIcon, QPixmap

# region Dark Theme
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.black)
dark_palette.setColor(QPalette.Button, QColor(100, 53, 53))
#dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)


# endregion


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Pixiv Downloader'
        self.left = 400
        self.top = 200
        self.width = 800
        self.height = 500
        self.setPalette(dark_palette)
        self.lbrowse = QtWidgets.QLineEdit(self)
        self.bbrowse = QtWidgets.QPushButton("Browse", self)
        self.ldownload = QtWidgets.QLineEdit(self)
        self.bdownload = QtWidgets.QPushButton("Download", self)
        self.label = QtWidgets.QLabel(self.centralWidget())
        self.label.setGeometry(QtCore.QRect(10, 120, 781, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kek.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.bbrowse.setGeometry(QtCore.QRect(670, 30, 75, 23))
        self.bbrowse.setObjectName("bbrowse")
        self.bbrowse.clicked.connect(self.on_click_browser)

        self.lbrowse.setGeometry(QtCore.QRect(20, 30, 621, 23))
        self.lbrowse.setObjectName("lbrowse")

        self.ldownload.setGeometry(QtCore.QRect(20, 70, 621, 23))
        self.ldownload.setObjectName("ldownload")

        self.bdownload.setGeometry(QtCore.QRect(670, 70, 75, 23))
        self.bdownload.setObjectName("bdownload")

        _translate = QtCore.QCoreApplication.translate
        self.bbrowse.setText(_translate("MainWindow", "Browse"))
        self.bdownload.setText(_translate("MainWindow", "Download"))

        self.show()

    @pyqtSlot()
    def on_click_browser(self):
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        self.lbrowse.setText(folder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())





