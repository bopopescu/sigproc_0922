# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui',
# licensing of 'login.ui' applies.
#
# Created: Sun Sep 22 12:58:23 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 192)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.pass_LE = QtWidgets.QLineEdit(self.frame_2)
        self.pass_LE.setObjectName("pass_LE")
        self.horizontalLayout_4.addWidget(self.pass_LE)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.login_btn = QtWidgets.QPushButton(self.frame_2)
        self.login_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/FR_icons/Check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_5.addWidget(self.login_btn)
        self.quit_btn = QtWidgets.QPushButton(self.frame_2)
        self.quit_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/FR_icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_btn.setIcon(icon1)
        self.quit_btn.setObjectName("quit_btn")
        self.horizontalLayout_5.addWidget(self.quit_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.username_LE = QtWidgets.QLineEdit(self.frame_2)
        self.username_LE.setObjectName("username_LE")
        self.horizontalLayout_6.addWidget(self.username_LE)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Login", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.login_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Login", None, -1))
        self.quit_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))

import icons_rc
