# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sun Sep 22 12:58:28 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.idnumber = QtWidgets.QLineEdit(self.frame_3)
        self.idnumber.setObjectName("idnumber")
        self.horizontalLayout_3.addWidget(self.idnumber)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lastname = QtWidgets.QLineEdit(self.frame_3)
        self.lastname.setObjectName("lastname")
        self.horizontalLayout_2.addWidget(self.lastname)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.firstname = QtWidgets.QLineEdit(self.frame_3)
        self.firstname.setObjectName("firstnane")
        self.horizontalLayout.addWidget(self.firstname)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.middlename = QtWidgets.QLineEdit(self.frame_3)
        self.middlename.setObjectName("middlename")
        self.horizontalLayout_6.addWidget(self.middlename)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.course = QtWidgets.QLineEdit(self.frame_3)
        self.course.setObjectName("course")
        self.horizontalLayout_4.addWidget(self.course)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.enroll_btn = QtWidgets.QPushButton(self.frame_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/FR_icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enroll_btn.setIcon(icon)
        self.enroll_btn.setObjectName("enroll_btn")
        self.horizontalLayout_5.addWidget(self.enroll_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.frame_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/FR_icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon1)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_5.addWidget(self.cancel_btn)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5.addWidget(self.frame_4, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCheck_Attendance = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/FR_icons/student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheck_Attendance.setIcon(icon3)
        self.actionCheck_Attendance.setObjectName("actionCheck_Attendance")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/FR_icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRegister_Faculty = QtWidgets.QAction(MainWindow)
        self.actionRegister_Faculty.setIcon(icon)
        self.actionRegister_Faculty.setObjectName("actionRegister_Faculty")
        refresh = QtGui.QIcon()
        refresh.addPixmap(QtGui.QPixmap(":/images/FR_icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReTrain = QtWidgets.QAction(MainWindow)
        self.actionReTrain.setObjectName("actionReTrain")
        self.actionReTrain.setIcon(refresh)

        self.actionQuit_1 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/FR_icons/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_1.setIcon(icon5)
        self.actionQuit_1.setObjectName("actionQuit_1")
        self.menuMenu.addAction(self.actionCheck_Attendance)
        self.menuMenu.addAction(self.actionRegister_Faculty)
        self.menuMenu.addAction(self.actionReTrain)

        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit_1)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Main Menu", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "ENROLL STUDENT MENU", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Student Number:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Last Name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "First Name:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Middle Name:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Course:", None, -1))
        self.enroll_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Enroll", None, -1))
        self.cancel_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu", None, -1))
        self.actionCheck_Attendance.setText(QtWidgets.QApplication.translate("MainWindow", "Check Attendance", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionRegister_Faculty.setText(QtWidgets.QApplication.translate("MainWindow", "Register Faculty", None, -1))
        self.actionReTrain.setText(QtWidgets.QApplication.translate("MainWindow", "Retrain", None, -1))
        self.actionQuit_1.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))

import icons_rc
