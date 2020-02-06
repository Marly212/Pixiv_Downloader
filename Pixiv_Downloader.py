# -*- coding: UTF-8 -*-
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from pixivpy3 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tkinter as tk
from tkinter import filedialog
import tempfile
import re

# region Dark Theme
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
# dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.black)
dark_palette.setColor(QPalette.Button, QColor(100, 53, 53))
# dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

# endregion

api = AppPixivAPI()
aapi = AppPixivAPI()
list3 = []
list4 = []
images = []
List_of_checked = []
List_of_unchecked = []
List_to_download = []
base_name = ""
List_test = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 1092)
        MainWindow.setPalette(dark_palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # region Button Browse
        self.bbrowse = QtWidgets.QPushButton(self.centralwidget)
        self.bbrowse.setGeometry(QtCore.QRect(1040, 60, 75, 23))
        self.bbrowse.setObjectName("Button Browse")
        self.bbrowse.setDisabled(True)
        self.bbrowse.clicked.connect(self.on_click_browser)
        # endregion

        # region Label Browse
        self.lbrowse = QtWidgets.QLineEdit(self.centralwidget)
        self.lbrowse.setGeometry(QtCore.QRect(20, 60, 991, 23))
        self.lbrowse.setObjectName("Text Browse")
        self.lbrowse.setDisabled(True)
        self.lbrowse.setReadOnly(True)
        # endregion

        # region Button Download
        self.bdownload = QtWidgets.QPushButton(self.centralwidget)
        self.bdownload.setGeometry(QtCore.QRect(1040, 100, 75, 23))
        self.bdownload.setObjectName("Button Download")
        self.bdownload.setDisabled(True)
        self.bdownload.clicked.connect(self.on_click_download)
        # endregion

        # region Button Login
        self.blogin = QtWidgets.QPushButton("Login", self.centralwidget)
        self.blogin.setGeometry(QtCore.QRect(1040, 20, 75, 23))
        self.blogin.setObjectName("Button Login")
        self.blogin.clicked.connect(self.on_click_login)
        # endregion

        # region Label Username
        self.lblusername = QtWidgets.QLabel("Username:", self.centralwidget)
        self.lblusername.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblusername.setFont(font)
        self.lblusername.setObjectName("lblusername")
        # endregion

        # region QLineEdit Username
        self.lusername = QtWidgets.QLineEdit(self.centralwidget)
        self.lusername.setGeometry(QtCore.QRect(90, 20, 371, 23))
        self.lusername.setObjectName("Text Username")
        self.lusername.textChanged.connect(self.loginchanged)
        # endregion

        # region Label Passwort
        self.lblpassword = QtWidgets.QLabel("Password:", self.centralwidget)
        self.lblpassword.setGeometry(QtCore.QRect(560, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblpassword.setFont(font)
        self.lblpassword.setObjectName("lblpassword")
        # endregion

        # region QLineEdit Passwort
        self.lpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lpassword.setGeometry(QtCore.QRect(640, 20, 371, 23))
        self.lpassword.setEchoMode(QLineEdit.Password)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.lpassword.setFont(font)
        self.lpassword.setObjectName("Text Passwort")
        # endregion

        # region Label PixivID
        self.lblid = QtWidgets.QLabel(self.centralwidget)
        self.lblid.setGeometry(QtCore.QRect(850, 100, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblid.setFont(font)
        self.lblid.setObjectName("lblid")
        # endregion

        # region QLineEdit PixivID
        self.lblPixivID = QtWidgets.QLineEdit(self.centralwidget)
        self.lblPixivID.setGeometry(QtCore.QRect(900, 100, 111, 23))
        self.lblPixivID.setObjectName("Pixiv ID")
        self.lblPixivID.setDisabled(True)
        self.lblPixivID.textEdited.connect(self.PixivID_text_changed)
        # endregion

        # region Button MyFeed
        self.bmyfeed = QtWidgets.QPushButton(self.centralwidget)
        self.bmyfeed.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.bmyfeed.setObjectName("bmyfeed")
        self.bmyfeed.setDisabled(True)
        self.bmyfeed.clicked.connect(self.on_click_myfeed)
        # endregion

        # region Button Recommended
        self.brecommended = QtWidgets.QPushButton(self.centralwidget)
        self.brecommended.setGeometry(QtCore.QRect(130, 100, 80, 23))
        self.brecommended.setObjectName("Recommended")
        self.brecommended.setDisabled(True)
        self.brecommended.clicked.connect(self.on_click_ranking)
        # endregion

        # region Labelfelder

        self.lblpicture1 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture1.setGeometry(QtCore.QRect(10, 140, 151, 171))
        self.lblpicture1.setText("")
        self.lblpicture1.setPixmap(QtGui.QPixmap("C:/Users/bruce.lieber/Desktop/Testbilder/kek.png"))
        self.lblpicture1.setScaledContents(True)
        self.lblpicture1.setObjectName("lblpicture1")

        self.lblpicture2 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture2.setGeometry(QtCore.QRect(210, 140, 151, 171))
        self.lblpicture2.setText("")
        self.lblpicture2.setScaledContents(True)
        self.lblpicture2.setObjectName("lblpicture2")

        self.lblpicture3 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture3.setGeometry(QtCore.QRect(410, 140, 151, 171))
        self.lblpicture3.setText("")
        self.lblpicture3.setScaledContents(True)
        self.lblpicture3.setObjectName("lblpicture3")

        self.lblpicture4 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture4.setGeometry(QtCore.QRect(610, 140, 151, 171))
        self.lblpicture4.setText("")
        self.lblpicture4.setScaledContents(True)
        self.lblpicture4.setObjectName("lblpicture4")

        self.lblpicture5 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture5.setGeometry(QtCore.QRect(810, 140, 151, 171))
        self.lblpicture5.setText("")
        self.lblpicture5.setScaledContents(True)
        self.lblpicture5.setObjectName("lblpicture5")

        self.lblpicture6 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture6.setGeometry(QtCore.QRect(1010, 140, 151, 171))
        self.lblpicture6.setText("")
        self.lblpicture6.setScaledContents(True)
        self.lblpicture6.setObjectName("lblpicture6")

        self.lblpicture7 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture7.setGeometry(QtCore.QRect(10, 350, 151, 171))
        self.lblpicture7.setText("")
        self.lblpicture7.setScaledContents(True)
        self.lblpicture7.setObjectName("lblpicture7")

        self.lblpicture8 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture8.setGeometry(QtCore.QRect(210, 350, 151, 171))
        self.lblpicture8.setText("")
        self.lblpicture8.setScaledContents(True)
        self.lblpicture8.setObjectName("lblpicture8")

        self.lblpicture9 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture9.setGeometry(QtCore.QRect(410, 350, 151, 171))
        self.lblpicture9.setText("")
        self.lblpicture9.setScaledContents(True)
        self.lblpicture9.setObjectName("lblpicture9")

        self.lblpicture10 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture10.setGeometry(QtCore.QRect(610, 350, 151, 171))
        self.lblpicture10.setText("")
        self.lblpicture10.setScaledContents(True)
        self.lblpicture10.setObjectName("lblpicture10")

        self.lblpicture11 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture11.setGeometry(QtCore.QRect(810, 350, 151, 171))
        self.lblpicture11.setText("")
        self.lblpicture11.setScaledContents(True)
        self.lblpicture11.setObjectName("lblpicture11")

        self.lblpicture12 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture12.setGeometry(QtCore.QRect(1010, 350, 151, 171))
        self.lblpicture12.setText("")
        self.lblpicture12.setScaledContents(True)
        self.lblpicture12.setObjectName("lblpicture12")

        self.lblpicture13 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture13.setGeometry(QtCore.QRect(10, 560, 151, 171))
        self.lblpicture13.setText("")
        self.lblpicture13.setScaledContents(True)
        self.lblpicture13.setObjectName("lblpicture13")

        self.lblpicture14 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture14.setGeometry(QtCore.QRect(210, 560, 151, 171))
        self.lblpicture14.setText("")
        self.lblpicture14.setScaledContents(True)
        self.lblpicture14.setObjectName("lblpicture14")

        self.lblpicture15 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture15.setGeometry(QtCore.QRect(410, 560, 151, 171))
        self.lblpicture15.setText("")
        self.lblpicture15.setScaledContents(True)
        self.lblpicture15.setObjectName("lblpicture15")

        self.lblpicture16 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture16.setGeometry(QtCore.QRect(610, 560, 151, 171))
        self.lblpicture16.setText("")
        self.lblpicture16.setScaledContents(True)
        self.lblpicture16.setObjectName("lblpicture16")

        self.lblpicture17 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture17.setGeometry(QtCore.QRect(810, 560, 151, 171))
        self.lblpicture17.setText("")
        self.lblpicture17.setScaledContents(True)
        self.lblpicture17.setObjectName("lblpicture17")

        self.lblpicture18 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture18.setGeometry(QtCore.QRect(1010, 560, 151, 171))
        self.lblpicture18.setText("")
        self.lblpicture18.setScaledContents(True)
        self.lblpicture18.setObjectName("lblpicture18")

        self.lblpicture19 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture19.setGeometry(QtCore.QRect(10, 780, 151, 171))
        self.lblpicture19.setText("")
        self.lblpicture19.setScaledContents(True)
        self.lblpicture19.setObjectName("lblpicture19")

        self.lblpicture20 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture20.setGeometry(QtCore.QRect(210, 780, 151, 171))
        self.lblpicture20.setText("")
        self.lblpicture20.setScaledContents(True)
        self.lblpicture20.setObjectName("lblpicture20")

        self.lblpicture21 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture21.setGeometry(QtCore.QRect(410, 780, 151, 171))
        self.lblpicture21.setText("")
        self.lblpicture21.setScaledContents(True)
        self.lblpicture21.setObjectName("lblpicture21")

        self.lblpicture22 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture22.setGeometry(QtCore.QRect(610, 780, 151, 171))
        self.lblpicture22.setText("")
        self.lblpicture22.setScaledContents(True)
        self.lblpicture22.setObjectName("lblpicture22")

        self.lblpicture23 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture23.setGeometry(QtCore.QRect(810, 780, 151, 171))
        self.lblpicture23.setText("")
        self.lblpicture23.setScaledContents(True)
        self.lblpicture23.setObjectName("lblpicture23")

        self.lblpicture24 = QtWidgets.QLabel(self.centralwidget)
        self.lblpicture24.setGeometry(QtCore.QRect(1010, 780, 151, 171))
        self.lblpicture24.setText("")
        self.lblpicture24.setScaledContents(True)
        self.lblpicture24.setObjectName("lblpicture24")

        # endregion

        # region CheckBox

        self.chboxdownload1 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload1.setGeometry(QtCore.QRect(40, 320, 70, 17))
        self.chboxdownload1.setObjectName("chboxdownload1")
        self.chboxdownload1.setDisabled(True)

        self.chboxdownload2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload2.setGeometry(QtCore.QRect(240, 320, 70, 17))
        self.chboxdownload2.setObjectName("chboxdownload2")
        self.chboxdownload2.setDisabled(True)

        self.chboxdownload3 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload3.setGeometry(QtCore.QRect(440, 320, 70, 17))
        self.chboxdownload3.setObjectName("chboxdownload3")
        self.chboxdownload3.setDisabled(True)

        self.chboxdownload4 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload4.setGeometry(QtCore.QRect(640, 320, 70, 17))
        self.chboxdownload4.setObjectName("chboxdownload4")
        self.chboxdownload4.setDisabled(True)

        self.chboxdownload5 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload5.setGeometry(QtCore.QRect(840, 320, 70, 17))
        self.chboxdownload5.setObjectName("chboxdownload5")
        self.chboxdownload5.setDisabled(True)

        self.chboxdownload6 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload6.setGeometry(QtCore.QRect(1040, 320, 70, 17))
        self.chboxdownload6.setObjectName("chboxdownload6")
        self.chboxdownload6.setDisabled(True)

        self.chboxdownload7 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload7.setGeometry(QtCore.QRect(40, 530, 70, 17))
        self.chboxdownload7.setObjectName("chboxdownload7")
        self.chboxdownload7.setDisabled(True)

        self.chboxdownload8 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload8.setGeometry(QtCore.QRect(240, 530, 70, 17))
        self.chboxdownload8.setObjectName("chboxdownload8")
        self.chboxdownload8.setDisabled(True)

        self.chboxdownload9 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload9.setGeometry(QtCore.QRect(440, 530, 70, 17))
        self.chboxdownload9.setObjectName("chboxdownload9")
        self.chboxdownload9.setDisabled(True)

        self.chboxdownload10 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload10.setGeometry(QtCore.QRect(640, 530, 70, 17))
        self.chboxdownload10.setObjectName("chboxdownload10")
        self.chboxdownload10.setDisabled(True)

        self.chboxdownload11 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload11.setGeometry(QtCore.QRect(840, 530, 70, 17))
        self.chboxdownload11.setObjectName("chboxdownload11")
        self.chboxdownload11.setDisabled(True)

        self.chboxdownload12 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload12.setGeometry(QtCore.QRect(1040, 530, 70, 17))
        self.chboxdownload12.setObjectName("chboxdownload12")
        self.chboxdownload12.setDisabled(True)

        self.chboxdownload13 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload13.setGeometry(QtCore.QRect(40, 740, 70, 17))
        self.chboxdownload13.setObjectName("chboxdownload13")
        self.chboxdownload13.setDisabled(True)

        self.chboxdownload14 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload14.setGeometry(QtCore.QRect(240, 740, 70, 17))
        self.chboxdownload14.setObjectName("chboxdownload14")
        self.chboxdownload14.setDisabled(True)

        self.chboxdownload15 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload15.setGeometry(QtCore.QRect(440, 740, 70, 17))
        self.chboxdownload15.setObjectName("chboxdownload15")
        self.chboxdownload15.setDisabled(True)

        self.chboxdownload16 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload16.setGeometry(QtCore.QRect(640, 740, 70, 17))
        self.chboxdownload16.setObjectName("chboxdownload16")
        self.chboxdownload16.setDisabled(True)

        self.chboxdownload17 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload17.setGeometry(QtCore.QRect(840, 740, 70, 17))
        self.chboxdownload17.setObjectName("chboxdownload17")
        self.chboxdownload17.setDisabled(True)

        self.chboxdownload18 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload18.setGeometry(QtCore.QRect(1040, 740, 70, 17))
        self.chboxdownload18.setObjectName("chboxdownload18")
        self.chboxdownload18.setDisabled(True)

        self.chboxdownload19 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload19.setGeometry(QtCore.QRect(40, 960, 70, 17))
        self.chboxdownload19.setObjectName("chboxdownload19")
        self.chboxdownload19.setDisabled(True)

        self.chboxdownload20 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload20.setGeometry(QtCore.QRect(240, 960, 70, 17))
        self.chboxdownload20.setObjectName("chboxdownload20")
        self.chboxdownload20.setDisabled(True)

        self.chboxdownload21 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload21.setGeometry(QtCore.QRect(440, 960, 70, 17))
        self.chboxdownload21.setObjectName("chboxdownload21")
        self.chboxdownload21.setDisabled(True)

        self.chboxdownload22 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload22.setGeometry(QtCore.QRect(640, 960, 70, 17))
        self.chboxdownload22.setObjectName("chboxdownload22")
        self.chboxdownload22.setDisabled(True)

        self.chboxdownload23 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload23.setGeometry(QtCore.QRect(840, 960, 70, 17))
        self.chboxdownload23.setObjectName("chboxdownload23")
        self.chboxdownload23.setDisabled(True)

        self.chboxdownload24 = QtWidgets.QCheckBox(self.centralwidget)
        self.chboxdownload24.setGeometry(QtCore.QRect(1040, 960, 70, 17))
        self.chboxdownload24.setObjectName("chboxdownload24")
        self.chboxdownload24.setDisabled(True)

        # endregion

        # region Ausgabe
        self.txtausgabe = QtWidgets.QTextEdit(self.centralwidget)
        self.txtausgabe.setGeometry(QtCore.QRect(10, 990, 1151, 61))
        self.txtausgabe.setReadOnly(True)
        self.txtausgabe.setObjectName("txtausgabe")
        # endregion

        # region MainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # endregion

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pixiv Downloader"))
        self.bbrowse.setText(_translate("MainWindow", "Browse"))
        self.bdownload.setText(_translate("MainWindow", "Download"))
        self.lblid.setText(_translate("MainWindow", "Pixiv ID:"))
        self.bmyfeed.setText(_translate("MainWindow", "My Feed"))
        self.brecommended.setText(_translate("MainWindow", "Recommended"))
        self.chboxdownload1.setText(_translate("MainWindow", "Download"))
        self.chboxdownload7.setText(_translate("MainWindow", "Download"))
        self.chboxdownload13.setText(_translate("MainWindow", "Download"))
        self.chboxdownload19.setText(_translate("MainWindow", "Download"))
        self.chboxdownload2.setText(_translate("MainWindow", "Download"))
        self.chboxdownload20.setText(_translate("MainWindow", "Download"))
        self.chboxdownload8.setText(_translate("MainWindow", "Download"))
        self.chboxdownload14.setText(_translate("MainWindow", "Download"))
        self.chboxdownload3.setText(_translate("MainWindow", "Download"))
        self.chboxdownload21.setText(_translate("MainWindow", "Download"))
        self.chboxdownload9.setText(_translate("MainWindow", "Download"))
        self.chboxdownload15.setText(_translate("MainWindow", "Download"))
        self.chboxdownload4.setText(_translate("MainWindow", "Download"))
        self.chboxdownload22.setText(_translate("MainWindow", "Download"))
        self.chboxdownload10.setText(_translate("MainWindow", "Download"))
        self.chboxdownload16.setText(_translate("MainWindow", "Download"))
        self.chboxdownload5.setText(_translate("MainWindow", "Download"))
        self.chboxdownload23.setText(_translate("MainWindow", "Download"))
        self.chboxdownload11.setText(_translate("MainWindow", "Download"))
        self.chboxdownload17.setText(_translate("MainWindow", "Download"))
        self.chboxdownload12.setText(_translate("MainWindow", "Download"))
        self.chboxdownload18.setText(_translate("MainWindow", "Download"))
        self.chboxdownload24.setText(_translate("MainWindow", "Download"))
        self.chboxdownload6.setText(_translate("MainWindow", "Download"))

    def on_click_download(self):
        if self.lblPixivID.text() == "":
            try:
                self.get_checked_box(images)
                images.clear()
            except Exception as e:
                self.txtausgabe.setText("Fehler, bitte überprüfen Sie die angegebene ID")
                self.txtausgabe.setText(e)
        else:
            try:
                eingabe = int(self.lblPixivID.text())
                json_result = api.illust_detail(eingabe)
                illust = json_result.illust
                base_name = os.path.basename(illust.image_urls['large'])
                extension = os.path.splitext(base_name)[1]
                name = "illust_id_%d_%s%s" % (illust.id, illust.title, extension)
                api.download(illust.image_urls.large, path=self.lbrowse.text() + "\\", name=name)
            except Exception as e:
                self.txtausgabe.setText(e)

    def on_click_browser(self):
        try:
            root = tk.Tk()
            root.withdraw()
            self.folder = filedialog.askdirectory()
            self.lbrowse.setText(self.folder)
            onclose = open("path.txt", "w")
            onclose.write(self.folder)
            onclose.close()
        except:
            self.txtausgabe.setText("Fehler, bitte gültigen Pfad angeben")

    def on_click_login(self):
        try:
            username = self.lusername.text()
            password = self.lpassword.text()
            api.login(username, password)
            oncloseusername = open("username.txt", "w")
            oncloseusername.write(self.lusername.text())
            oncloseusername.close()
            onclosepassword = open("password.txt", "w")
            onclosepassword.write(self.lpassword.text())
            onclosepassword.close()
            self.open()

            # region enable
            self.bbrowse.setDisabled(False)
            self.lbrowse.setDisabled(False)
            self.bdownload.setDisabled(False)
            self.lblPixivID.setDisabled(False)
            self.bmyfeed.setDisabled(False)
            self.brecommended.setDisabled(False)
            self.chboxdownload1.setDisabled(False)
            self.chboxdownload2.setDisabled(False)
            self.chboxdownload3.setDisabled(False)
            self.chboxdownload4.setDisabled(False)
            self.chboxdownload5.setDisabled(False)
            self.chboxdownload6.setDisabled(False)
            self.chboxdownload7.setDisabled(False)
            self.chboxdownload8.setDisabled(False)
            self.chboxdownload9.setDisabled(False)
            self.chboxdownload10.setDisabled(False)
            self.chboxdownload11.setDisabled(False)
            self.chboxdownload12.setDisabled(False)
            self.chboxdownload13.setDisabled(False)
            self.chboxdownload14.setDisabled(False)
            self.chboxdownload15.setDisabled(False)
            self.chboxdownload16.setDisabled(False)
            self.chboxdownload17.setDisabled(False)
            self.chboxdownload18.setDisabled(False)
            self.chboxdownload19.setDisabled(False)
            self.chboxdownload20.setDisabled(False)
            self.chboxdownload21.setDisabled(False)
            self.chboxdownload22.setDisabled(False)
            self.chboxdownload23.setDisabled(False)
            self.chboxdownload24.setDisabled(False)
            # endregion

        except Exception as e:
            self.txtausgabe.setText(e)

    def on_click_myfeed(self):
        try:
            self.onclose()
            illust_ranking = api.illust_ranking()
            id = 1
            for illust in illust_ranking.illusts[:24]:
                thumbnail_url = illust_ranking.illusts[id].image_urls.medium
                base_name = os.path.basename(illust_ranking.illusts[id].image_urls.medium)
                api.download(thumbnail_url, path=tempfile.gettempdir(), name=base_name)
                images.append(tempfile.gettempdir() + "\\" + base_name)
                List_test.append(tempfile.gettempdir() + "\\" + base_name)
                id = id + 1
            self.labels(images)

        except Exception as e:

            print(e)

        finally:
            self.status = 1

    def on_click_ranking(self):
        try:
            if self.status == 1:
                self.onclose()
            rank_list = api.illust_recommended()
            id = 1
            for illust in rank_list.illusts[:24]:
                thumbnail_url = rank_list.illusts[id].image_urls.medium
                base_name = os.path.basename(rank_list.illusts[id].image_urls.medium)
                List_test.append(base_name)
                api.download(thumbnail_url, path=tempfile.gettempdir(), name=base_name)
                images.append(tempfile.gettempdir() + "\\" + base_name)
                id = id + 1
            self.labels(images)

        except Exception as e:
            self.txtausgabe.setText(e)

        finally:
            self.status = 1

    def PixivID_text_changed(self):
        try:
            json_result = api.illust_detail(self.lblPixivID.text())
            thumbnail_url = json_result.illust.image_urls.medium
            base_name = os.path.basename(json_result.illust.image_urls.medium)
            api.download(thumbnail_url, path=tempfile.gettempdir(), name=base_name)
            self.lblpicture1.setPixmap(QtGui.QPixmap(tempfile.gettempdir() + "\\" + base_name))
        except:
            self.txtausgabe.setText("Fehler, bitte ID überprüfen")

    def loginchanged(self):
        self.onloginchange = open("username.txt", "w")
        self.onloginchange.write(self.lusername.text())
        self.onloginchange.close()

    def open(self):
        onopen = open("path.txt", "r")
        self.lbrowse.setText(onopen.read())
        onopen.close()

    def labels(self, images):
        list2 = [self.lblpicture1, self.lblpicture2, self.lblpicture3, self.lblpicture4, self.lblpicture5,
                 self.lblpicture6, self.lblpicture7, self.lblpicture8, self.lblpicture9, self.lblpicture10,
                 self.lblpicture11, self.lblpicture12, self.lblpicture13, self.lblpicture14, self.lblpicture15,
                 self.lblpicture16, self.lblpicture17, self.lblpicture18, self.lblpicture19, self.lblpicture20,
                 self.lblpicture21, self.lblpicture22, self.lblpicture23, self.lblpicture24]
        id = 0
        if id <= 24:
            for l in images:
                # l = Kompletter Pfad mit extension zum Bild im Temp Ordner
                image = str(l).replace("'", "").replace("[", "").replace("]", "")
                label = list2[id]
                label.setPixmap(QtGui.QPixmap(image))
                id = id + 1

    def get_checked_box(self, images):
        List = [(self.chboxdownload1.isChecked(), 1), (self.chboxdownload2.isChecked(), 2),
                (self.chboxdownload3.isChecked(), 3), (self.chboxdownload4.isChecked(), 4),
                (self.chboxdownload5.isChecked(), 5), (self.chboxdownload6.isChecked(), 6),
                (self.chboxdownload7.isChecked(), 7), (self.chboxdownload8.isChecked(), 8),
                (self.chboxdownload9.isChecked(), 9), (self.chboxdownload10.isChecked(), 10),
                (self.chboxdownload11.isChecked(), 11), (self.chboxdownload12.isChecked(), 12),
                (self.chboxdownload12.isChecked(), 13), (self.chboxdownload14.isChecked(), 14),
                (self.chboxdownload15.isChecked(), 15), (self.chboxdownload16.isChecked(), 16),
                (self.chboxdownload17.isChecked(), 17), (self.chboxdownload18.isChecked(), 18),
                (self.chboxdownload19.isChecked(), 19), (self.chboxdownload20.isChecked(), 20),
                (self.chboxdownload21.isChecked(), 21), (self.chboxdownload22.isChecked(), 22),
                (self.chboxdownload23.isChecked(), 23), (self.chboxdownload24.isChecked(), 24)]
        for i, v in List:
            # i = True oder False: v = Die Nachricht oben
            if i:
                List_of_checked.append(v)
                if v == 1:
                    List_to_download.append(images[0])
                if v == 2:
                    List_to_download.append(images[1])
                if v == 3:
                    List_to_download.append(images[2])
                if v == 4:
                    List_to_download.append(images[3])
                if v == 5:
                    List_to_download.append(images[4])
                if v == 6:
                    List_to_download.append(images[5])
                if v == 7:
                    List_to_download.append(images[6])
                if v == 8:
                    List_to_download.append(images[7])
                if v == 9:
                    List_to_download.append(images[8])
                if v == 10:
                    List_to_download.append(images[9])
                if v == 11:
                    List_to_download.append(images[10])
                if v == 12:
                    List_to_download.append(images[11])
                if v == 13:
                    List_to_download.append(images[12])
                if v == 14:
                    List_to_download.append(images[13])
                if v == 15:
                    List_to_download.append(images[14])
                if v == 16:
                    List_to_download.append(images[15])
                if v == 17:
                    List_to_download.append(images[16])
                if v == 18:
                    List_to_download.append(images[17])
                if v == 19:
                    List_to_download.append(images[18])
                if v == 20:
                    List_to_download.append(images[19])
                if v == 21:
                    List_to_download.append(images[20])
                if v == 22:
                    List_to_download.append(images[21])
                if v == 23:
                    List_to_download.append(images[22])
                if v == 24:
                    List_to_download.append(images[23])
            else:
                List_of_unchecked.append(v)

        self.download_checked()
        List_of_checked.clear()
        List_of_unchecked.clear()

    def download_checked(self):
        try:
            id = 0
            for l in List_to_download:
                image = str(l).replace("'", "").replace("[", "").replace("]", "")
                pixivid = re.sub('_p0_master1200.jpg', '', os.path.basename(image))
                json_result = api.illust_detail(pixivid)
                illust = json_result.illust
                base_name = os.path.basename(illust.image_urls['large'])
                extension = os.path.splitext(base_name)[1]
                name = "illust_id_%d_%s%s" % (illust.id, illust.title, extension)
                api.download(illust.image_urls.large, path=self.lbrowse.text() + "\\", name=name)
            List_to_download.clear()
            images.clear()
        except Exception as e:
            self.txtausgabe.setText(e)

    def onclose(self):
        print(List_test)
        for image in images:
            os.remove(image)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    onopenusername = open("username.txt", "r")
    ui.lusername.setText(onopenusername.read())
    onopenusername.close()
    onopenpassword = open("password.txt", "r")
    ui.lpassword.setText(onopenpassword.read())
    onopenpassword.close()
    sys.exit(app.exec_())


# illust = json_result.illust
# print(">>> origin url: %s" % illust.image_urls['large'])
# dl = "C:\\Program Files\\Windows B\\c#\\Pixiv_Test\\"
# api.download(illust.image_urls.large, "", dl, "Test.jpg")


# Ranking
# illust_ranking = api.illust_ranking()
# for illust in illust_ranking.illusts[:5]:
#    print(illust.image_urls.large)
#    base_name = os.path.basename(illust.image_urls['large'])
#    extension = os.path.splitext(base_name)[1]
#    name = "illust_id_%d_%s%s" % (illust.id, illust.title, extension)
#    api.download(illust.image_urls.large, path=self.lbrowse.text() + "\\", name=name)
#    print(">>> origin url: %s" % illust.image_urls['large'])
# self.label.setPixmap(QtGui.QPixmap(illust.image_urls['large']))
