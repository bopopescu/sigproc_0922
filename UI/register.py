# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui',
# licensing of 'register.ui' applies.
#
# Created: Sun Sep 22 12:58:34 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.firstname = QtWidgets.QLineEdit(self.frame_5)
        self.firstname.setObjectName("firstname")
        self.horizontalLayout_8.addWidget(self.firstname)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.username = QtWidgets.QLineEdit(self.frame_5)
        self.username.setObjectName("username")
        self.horizontalLayout_13.addWidget(self.username)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lastname = QtWidgets.QLineEdit(self.frame_5)
        self.lastname.setObjectName("lastname")
        self.horizontalLayout_6.addWidget(self.lastname)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.password= QtWidgets.QLineEdit(self.frame_5)
        self.password.setObjectName("password")
        self.horizontalLayout_14.addWidget(self.password)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.idnumber = QtWidgets.QLineEdit(self.frame_5)
        self.idnumber.setObjectName("idnumber")
        self.horizontalLayout_7.addWidget(self.idnumber)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.repassword = QtWidgets.QLineEdit(self.frame_5)
        self.repassword.setObjectName("repassword")
        self.horizontalLayout_15.addWidget(self.repassword)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.enroll_btn_2 = QtWidgets.QPushButton(self.frame_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/FR_icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enroll_btn_2.setIcon(icon)
        self.enroll_btn_2.setObjectName("enroll_btn_2")
        self.horizontalLayout_10.addWidget(self.enroll_btn_2)
        self.cancel_btn_2 = QtWidgets.QPushButton(self.frame_5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/FR_icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn_2.setIcon(icon1)
        self.cancel_btn_2.setObjectName("cancel_btn_2")
        self.horizontalLayout_10.addWidget(self.cancel_btn_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 3, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "REGISTER FACULTY MENU", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "First Name:", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Last Name:", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "ID Number:", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "Re-enter Password", None, -1))
        self.enroll_btn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Register", None, -1))
        self.cancel_btn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))

import icons_rc
