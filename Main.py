from PySide2 import QtWidgets
from UI import main
from UI import login
from UI import register
from UI import check
import mysql.connector
import createDataset
import trainData
import pandas
import recognition
import os

app = QtWidgets.QApplication()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sigproc"
)
dbCursor = mydb.cursor()


# condition for clicking of the Register Button

# for register faculty UI
class Reg(register.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUi(self)
        self.enroll_btn_2.clicked.connect(self.get)
        self.cancel_btn_2.clicked.connect(self.bye)

        # condition for clicking of the Register Button

    def get(self):
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        id = self.idnumber.text()
        username = self.username.text()
        password = self.password.text()
        repassword = self.repassword.text()
        if not firstname or not lastname or not id or not username or not password or not repassword:
            QtWidgets.QMessageBox.about(self, "Warning!", "All fields are required")
            return 0
        elif password != repassword:
            QtWidgets.QMessageBox.about(self, "Warning!", "Password do not match")
            return 0
        else:
            sql = "Select * FROM user WHERE username = '" + username + "'"
            dbCursor.execute(sql)
            result = dbCursor.fetchone()

            if result is not None:
                QtWidgets.QMessageBox.about(self, "Warning!", "Username already exists")
                return 0
            else:
                sql = "Select * FROM user WHERE id_number = '" + id + "'"
                dbCursor.execute(sql)
                result = dbCursor.fetchone()
                if result is not None:
                    QtWidgets.QMessageBox.about(self, "Warning!", "Student Number already registered")
                    return 0
                else:
                    sql = "INSERT INTO user (username, password, first_name, last_name, id_number ) VALUES (%s, %s, %s, %s, %s)"
                    val = (username, password, firstname, lastname, id)
                    dbCursor.execute(sql, val)
                    mydb.commit()
                    QtWidgets.QMessageBox.about(self, "Information", "User has been created")
                    self.close()

    def bye(self):
        self.close()


# for the Main Menu UI
class MainMenu(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setupUi(self)
        self.actionQuit_1.triggered.connect(self.bye)  # for quit button
        self.actionCheck_Attendance.triggered.connect(self.CheckAttendance)  # for check attendance
        self.actionRegister_Faculty.triggered.connect(self.RegFaculty)  # for register faculty
        self.actionReTrain.triggered.connect(self.ReTrain)  # for register faculty
        self.enroll_btn.clicked.connect(self.enroll)

    def bye(self):
        self.close()

    def RegFaculty(self):
        self.anotherwindow = Reg()
        self.anotherwindow.show()

    def ReTrain(self):
        self.anotherwindow = trainData.training()
        self.anotherwindow.show()

    def CheckAttendance(self):
        self.anotherwindow = Checking()
        self.anotherwindow.show()

    def enroll(self):
        id = self.idnumber.text()
        lastname = self.lastname.text()
        firstname = self.firstname.text()
        middlename = self.middlename.text()
        course = self.course.text()

        if not id or not lastname or not firstname or not course:
            QtWidgets.QMessageBox.about(self, "Warning!", "Please fill all required fields")
            return 0
        else:
            sql = "Select * FROM student WHERE id = '" + id + "'"
            dbCursor.execute(sql)
            result = dbCursor.fetchone()

            if result is not None:
                QtWidgets.QMessageBox.about(self, "Warning!", "Student already added")
                return 0
            else:
                createDataset.capturePhoto(id)
                sql = "INSERT INTO student (id_number, last_name, first_name, middle_name, course ) VALUES (%s, %s, %s, %s, %s)"
                val = (id, lastname, firstname, middlename, course)
                dbCursor.execute(sql, val)
                mydb.commit()
                df = pandas.read_csv("data.csv")
                name = lastname + ' ' +firstname + ' ' + middlename
                row = [id, name, course]
                while len(row) is not len(df.columns):
                    row.append('N\A')
                df.loc[len(df)] = row
                df = df.sort_values(by=['Name'])
                df.to_csv("data.csv", index=False)
                QtWidgets.QMessageBox.about(self, "Information", "Student has been added")


# for the Login Window UI
class Login(login.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.log)
        self.quit_btn.clicked.connect(self.quit)

    def log(self):
        if not self.pass_LE.text() or not self.username_LE.text():
            QtWidgets.QMessageBox.about(self, "Warning!", "Username/Password required")
            return 0
        else:
            # for login
            sql = "Select password FROM user WHERE username = '" + self.username_LE.text() + "'"
            dbCursor.execute(sql)
            result = dbCursor.fetchone()
            if result is None:
                QtWidgets.QMessageBox.about(self, "Warning!", "User does not exist")
                return 0
            else:
                password = result[0]
                if password != self.pass_LE.text():
                    QtWidgets.QMessageBox.about(self, "Warning!", "Username/Password do not match")
                    return 0
                else:
                    self.close()
                    self.anotherwindow = MainMenu()
                    self.anotherwindow.show()

    def quit(self):
        self.close()


# for the Check Attendance UI
class Checking(check.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Checking, self).__init__()
        self.setupUi(self)
        self.Start_btn.clicked.connect(self.startattendance)
        self.Back_btn.clicked.connect(self.check_back)


    def startattendance(self):  # code for check attendance
        print(self.Late_TimeEdit.time().toString())
        recognition.main(self.Late_TimeEdit.time().toString(), self.timeEdit_2.time().toString())
        os.system('start "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE" "data.csv"')
        self.close()

    def check_back(self):  # code for back button
        self.close()


if __name__ == '__main__':
    qt_app = Login()
    qt_app.show()
    app.exec_()
