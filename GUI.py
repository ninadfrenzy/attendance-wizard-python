# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rep_lgc import *
import warnings
warnings.filterwarnings('ignore')
printstring = ""
tablename = ""
def_str = ""
class Ui_login_page(object):
    def setupUi(self, login_page):
        login_page.setObjectName("login_page")
        login_page.resize(959, 418)
        font = QtGui.QFont()
        font.setPointSize(9)
        login_page.setFont(font)
        login_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        login_page.setMouseTracking(True)
        login_page.setWhatsThis("")
        login_page.setAccessibleName("")
        login_page.setAccessibleDescription("")
        login_page.setIconSize(QtCore.QSize(50, 50))
        self.attendanceWizard = QtWidgets.QWidget(login_page)
        self.attendanceWizard.setObjectName("attendanceWizard")
        self.usernameInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.usernameInput.setGeometry(QtCore.QRect(670, 200, 281, 31))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.passwordInput.setGeometry(QtCore.QRect(670, 270, 281, 31))
        self.passwordInput.setObjectName("passwordInput")
        self.UserNameLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.UserNameLabel.setGeometry(QtCore.QRect(670, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.UserNameLabel.setFont(font)
        self.UserNameLabel.setObjectName("UserNameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.passwordLabel.setGeometry(QtCore.QRect(670, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.loginButton.setGeometry(QtCore.QRect(740, 320, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)

        self.logo = QtWidgets.QLabel(self.attendanceWizard)
        self.logo.setGeometry(QtCore.QRect(10, 10, 641, 391))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/test.png"))
        self.logo.setObjectName("logo")
        login_page.setCentralWidget(self.attendanceWizard)
        self.statusbar = QtWidgets.QStatusBar(login_page)
        self.statusbar.setObjectName("statusbar")
        login_page.setStatusBar(self.statusbar)

        self.retranslateUi(login_page)
        QtCore.QMetaObject.connectSlotsByName(login_page)

    def retranslateUi(self, login_page):
        _translate = QtCore.QCoreApplication.translate
        login_page.setWindowTitle(_translate("login_page", "Attendance Wizard "))
        self.UserNameLabel.setText(_translate("login_page", "User Name :"))
        self.passwordLabel.setText(_translate("login_page", "Password :"))
        self.loginButton.setText(_translate("login_page", "Login"))
    def login(self):
        user = self.usernameInput.text()
        password = self.passwordInput.text()
        if(authenticate(user, password)):
            report_page.show()
            login_page.close()
        else:
            err = QtWidgets.QMessageBox()
            err.setText('Invalid credentials')
            err.setIcon(QtWidgets.QMessageBox.Critical)
            err.exec_()


class Ui_ReportSelection_page(object):

    def setupUi(self, ReportSelection_page):
        self.filename = ""
        self.defaulters_str = ""
        self.warnings_str = ""
        self.sub_defaulters_str = ""
        ReportSelection_page.setObjectName("ReportSelection_page")
        ReportSelection_page.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ReportSelection_page)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(300, 500, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.submit)
        self.ORLabael = QtWidgets.QLabel(self.centralwidget)
        self.ORLabael.setGeometry(QtCore.QRect(60, 340, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ORLabael.setFont(font)
        self.ORLabael.setObjectName("ORLabael")
        self.selectReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectReportLabel.setGeometry(QtCore.QRect(220, 400, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectReportLabel.setFont(font)
        self.selectReportLabel.setObjectName("selectReportLabel")
        self.selectReportInput = QtWidgets.QComboBox(self.centralwidget)
        self.selectReportInput.setGeometry(QtCore.QRect(410, 400, 231, 31))
        self.selectReportInput.setObjectName("selectReportInput")
        connection_object=sql.connect('attendance.db')
        cursor = connection_object.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        res = cursor.fetchall()
        res = [ele for x in res for ele in x]
        
        self.selectReportInput.addItems(res)
        self.AddUserButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.AddUserButton.setGeometry(QtCore.QRect(0, 0, 222, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.AddUserButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddUserButton.setIcon(icon)
        self.AddUserButton.setIconSize(QtCore.QSize(50, 50))
        self.AddUserButton.setObjectName("AddUserButton")
        self.AddUserButton.clicked.connect(self.add_user)
        self.dateInput = QtWidgets.QDateEdit(self.centralwidget)
        self.dateInput.setGeometry(QtCore.QRect(410, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateInput.setFont(font)
        self.dateInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateInput.setObjectName("dateInput")
        self.subjectLabel = QtWidgets.QLabel(self.centralwidget)
        self.subjectLabel.setGeometry(QtCore.QRect(280, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setObjectName("subjectLabel")
        self.addNewREportLabel = QtWidgets.QLabel(self.centralwidget)
        self.addNewREportLabel.setGeometry(QtCore.QRect(210, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addNewREportLabel.setFont(font)
        self.addNewREportLabel.setObjectName("addNewREportLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(310, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.browseButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton_2.setGeometry(QtCore.QRect(410, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browseButton_2.setFont(font)
        self.browseButton_2.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.browseButton_2.setObjectName("browseButton_2")
        self.browseButton_2.clicked.connect(self.get_file)
        self.deletebutton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.deletebutton.setGeometry(QtCore.QRect(730, 0, 61, 61))
        self.deletebutton.setText("")
        self.deletebutton.clicked.connect(self.clear)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recycle-bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletebutton.setIcon(icon1)
        self.deletebutton.setIconSize(QtCore.QSize(50, 50))
        self.deletebutton.setObjectName("deletebutton")
        self.SubjectInput = QtWidgets.QTextEdit(self.centralwidget)
        self.SubjectInput.setGeometry(QtCore.QRect(410, 280, 271, 51))
        self.SubjectInput.setObjectName("SubjectInput")
        ReportSelection_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReportSelection_page)
        self.statusbar.setObjectName("statusbar")
        ReportSelection_page.setStatusBar(self.statusbar)

        self.retranslateUi(ReportSelection_page)
        QtCore.QMetaObject.connectSlotsByName(ReportSelection_page)

    def retranslateUi(self, ReportSelection_page):
        _translate = QtCore.QCoreApplication.translate
        ReportSelection_page.setWindowTitle(_translate("ReportSelection_page", "Attendance Wizard"))
        ReportSelection_page.setStatusTip(_translate("ReportSelection_page", "Delete all the reports from database"))
        self.submitButton.setText(_translate("ReportSelection_page", "Submit"))
        self.ORLabael.setText(_translate("ReportSelection_page", "_____________________________ OR ____________________________"))
        self.selectReportLabel.setText(_translate("ReportSelection_page", "Select Report:"))
        self.selectReportInput.setStatusTip(_translate("ReportSelection_page", "Select existing report from database"))
        self.AddUserButton.setStatusTip(_translate("ReportSelection_page", "Add new user"))
        self.AddUserButton.setText(_translate("ReportSelection_page", "Add User"))
        self.dateInput.setStatusTip(_translate("ReportSelection_page", "select date of generation of PDF"))
        self.subjectLabel.setText(_translate("ReportSelection_page", "Subjects:"))
        self.addNewREportLabel.setText(_translate("ReportSelection_page", "Add New Report:"))
        self.dateLabel.setText(_translate("ReportSelection_page", "Date:"))
        self.browseButton_2.setToolTip(_translate("ReportSelection_page", "<html><head/><body><p>select the PDF Report</p></body></html>"))
        self.browseButton_2.setStatusTip(_translate("ReportSelection_page", "Select the new PDF report"))
        self.browseButton_2.setText(_translate("ReportSelection_page", "Browse"))
        self.deletebutton.setStatusTip(_translate("ReportSelection_page", "Delete all the reports from database"))
        self.SubjectInput.setStatusTip(_translate("ReportSelection_page", "Enter comma separated subjects according to the report"))

    def get_file(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(report_page,'Single File', QtCore.QDir.rootPath() , '*.pdf')


    def submit(self):
        global tablename
        date_gen = self.dateInput.text()

        subjects = self.SubjectInput.toPlainText()
        if(subjects!=""):

            subjects = ["rollno","name"]+list(subjects.split(","))
        
        file = self.filename
        date_gen = date_gen.replace("/","_")
	date_gen = date_gen.replace("-","_")
        #print(date_gen,subjects,file)

        if (len(subjects)<=2 and date_gen!="" and file!=""):
            global def_str
            def_str = display_only_defaulters(file)
            def_ui = Ui_only_def_page()
            def_ui.setupUi(only_def)
            only_def.show()
            report_page.close()
        else:
            if(date_gen!="" and subjects!="" and file!=""):
                self.tablename="report"+date_gen
                self.frame,total_str = clean_data(file,subjects)
                store_data(self.frame,self.tablename)
            else:
                self.tablename = str(self.selectReportInput.currentText())
                if(self.tablename!=""):
                    self.frame,total_str = get_from_db(self.tablename,create_connection())
                else:
                    err = QtWidgets.QMessageBox()
                    err.setText('No Report selected!')
                    err.setIcon(QtWidgets.QMessageBox.Critical)
                    err.exec_()

            global printstring
            self.defaulters_str,self.warnings_str,self.sub_defaulters_str = find_irregulars(self.tablename,self.frame,create_connection())
            self.five_str = top_five(self.frame)
            self.most_bk = most_bunked_sub(self.frame)
            self.df,self.wr = counting(create_connection(),self.tablename)
            decoration = (["\n************************************AVERAGE ATTENDANCE************************************\n",
                "\n\n\n************************************TOP FIVE ATTENTIVE************************************\n\n",
                "\n\n\n****************************************DEFAULTERS****************************************\n\n",
                "\n\n\n**************************************SUB-DEFAULTERS**************************************\n\n",
                "\n\n\n*****************************************WARNINGS*****************************************\n\n",
                "\n\n\n******************************************MESSAGE*****************************************\n\n",
                "\n\n\nATTENDANCE WAS OBSERVED TO BE LESS IN: \n\n",
                "\n\n\nNUMBER OF DEFAULTERS:",
                "\n\n\nNUMBER OF SUBJECT-DEFAULTERS:",
                "\n\n\nNUMBER OF WARNINGS:"])
            printstring = printstring+decoration[7]+self.df+"\n"+decoration[9]+self.wr+"\n"+decoration[0]+total_str+decoration[2]+self.defaulters_str+decoration[4]+self.warnings_str+decoration[3]+self.sub_defaulters_str+decoration[1]+self.five_str+decoration[6]+self.most_bk
            summary_ui = Ui_summary_page()
            summary_ui.setupUi(summary_page)
            summary_page.show()
            report_page.close()        

    def clear(self):
        flush()

    def add_user(self):
        
        dialog = QtWidgets.QDialog()
        user = QtWidgets.QLineEdit(dialog)
        user.setPlaceholderText('username')
        user.move(50,30)
        password = QtWidgets.QLineEdit(dialog)
        password.setPlaceholderText('password')
        password.move(50,70)
        def add_to_users():
            usern = user.text()
            passwordval = password.text()
            add_to_db(usern,passwordval)
        addbutton= QtWidgets.QPushButton("Add", dialog)
        addbutton.move(50,100)
        addbutton.clicked.connect(add_to_users)
        dialog.exec_()



class Ui_only_def_page(object):
    def setupUi(self, summary_page):
        summary_page.setObjectName("summary_page")
        summary_page.resize(783, 640)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        summary_page.setFont(font)
        summary_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        summary_page.setToolTip("")
        summary_page.setWhatsThis("")
        summary_page.setAccessibleName("")
        summary_page.setAccessibleDescription("")
        self.attendanceWizard = QtWidgets.QWidget(summary_page)
        self.attendanceWizard.setObjectName("attendanceWizard")

        font = QtGui.QFont()
        font.setPointSize(11)

        self.backButton = QtWidgets.QCommandLinkButton(self.attendanceWizard)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 222, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.backButton.setFont(font)
        self.backButton.setToolTip("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("32-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.goback)
        self.summaryOutput = QtWidgets.QTextBrowser(self.attendanceWizard)
        self.summaryOutput.setGeometry(QtCore.QRect(20, 100, 731, 401))
        self.summaryOutput.setObjectName("summaryOutput")
        global def_str
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Monospace")
        self.summaryOutput.setText(def_str)
        self.summaryOutput.setFont(font)
       
        self.summarylabel = QtWidgets.QLabel(self.attendanceWizard)
        self.summarylabel.setGeometry(QtCore.QRect(290, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.summarylabel.setFont(font)
        self.summarylabel.setObjectName("summarylabel")
        summary_page.setCentralWidget(self.attendanceWizard)
        self.statusbar = QtWidgets.QStatusBar(summary_page)
        self.statusbar.setObjectName("statusbar")
        summary_page.setStatusBar(self.statusbar)
        self.retranslateUi(summary_page)
        QtCore.QMetaObject.connectSlotsByName(summary_page)

    def retranslateUi(self, summary_page):
        _translate = QtCore.QCoreApplication.translate
        summary_page.setWindowTitle(_translate("summary_page", "Attendance Wizard "))
        self.backButton.setText(_translate("summary_page", "Back"))
        self.summarylabel.setText(_translate("summary_page", "Summary"))
    @staticmethod
    def goback(self):
        report_page.show()
        only_def.close()


class Ui_mail_page(object):
    def setupUi(self, mail_page):
        mail_page.setObjectName("mail_page")
        mail_page.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(9)
        mail_page.setFont(font)
        mail_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mail_page.setToolTip("")
        mail_page.setWhatsThis("")
        mail_page.setAccessibleName("")
        mail_page.setAccessibleDescription("")
        self.attendanceWizard = QtWidgets.QWidget(mail_page)
        self.attendanceWizard.setObjectName("attendanceWizard")
        self.maillabel = QtWidgets.QLabel(self.attendanceWizard)
        self.maillabel.setGeometry(QtCore.QRect(130, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.maillabel.setFont(font)
        self.maillabel.setObjectName("maillabel")
        self.emailIdInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.emailIdInput.setGeometry(QtCore.QRect(320, 120, 381, 31))
        self.emailIdInput.setObjectName("emailIdInput")
        self.Passwordlabel = QtWidgets.QLabel(self.attendanceWizard)
        self.Passwordlabel.setGeometry(QtCore.QRect(120, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Passwordlabel.setFont(font)
        self.Passwordlabel.setObjectName("Passwordlabel")
        self.passwordInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.passwordInput.setGeometry(QtCore.QRect(320, 180, 381, 31))
        self.passwordInput.setObjectName("passwordInput")
        self.selectFileLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.selectFileLabel.setGeometry(QtCore.QRect(110, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.selectFileLabel.setFont(font)
        self.selectFileLabel.setObjectName("selectFileLabel")
        self.browseButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.browseButton.setGeometry(QtCore.QRect(410, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.browseButton.setFont(font)
        self.browseButton.setToolTip("")
        self.browseButton.setAccessibleName("")
        self.browseButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(112, 23, 195);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.browsefile)
        self.mailDefaultersButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.mailDefaultersButton.setGeometry(QtCore.QRect(330, 420, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mailDefaultersButton.setFont(font)
        self.mailDefaultersButton.setToolTip("")
        self.mailDefaultersButton.setToolTipDuration(2)
        self.mailDefaultersButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.mailDefaultersButton.setObjectName("mailDefaultersButton")
        self.mailDefaultersButton.clicked.connect(self.sendmail)
        self.backButton = QtWidgets.QCommandLinkButton(self.attendanceWizard)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 222, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.backButton.setFont(font)
        self.backButton.setToolTip("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("32-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.goback)
        mail_page.setCentralWidget(self.attendanceWizard)
        self.statusbar = QtWidgets.QStatusBar(mail_page)
        self.statusbar.setObjectName("statusbar")
        mail_page.setStatusBar(self.statusbar)

        self.retranslateUi(mail_page)
        QtCore.QMetaObject.connectSlotsByName(mail_page)

    def retranslateUi(self, mail_page):
        _translate = QtCore.QCoreApplication.translate
        mail_page.setWindowTitle(_translate("mail_page", "Attendance Wizard "))
        self.maillabel.setText(_translate("mail_page", "Email Id :"))
        self.Passwordlabel.setText(_translate("mail_page", "Password :"))
        self.selectFileLabel.setText(_translate("mail_page", "Select the file :"))
        self.browseButton.setStatusTip(_translate("mail_page", "select the csv file containing roll no and mail ids for perticular class"))
        self.browseButton.setWhatsThis(_translate("mail_page", "select the file containing roll no and mail ids for perticular class"))
        self.browseButton.setText(_translate("mail_page", "Browse"))
        self.mailDefaultersButton.setText(_translate("mail_page", "Mail Defaulters"))
        self.backButton.setText(_translate("mail_page", "Back"))
    def browsefile(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(report_page, 'Single File', QtCore.QDir.rootPath() , '*.csv')

    def sendmail(self):
        my_mail = self.emailIdInput.text()
        my_pwd = self.passwordInput.text()
        file = self.filename
        mail_students(create_connection(),rep_ui.tablename,my_mail,my_pwd,file)
    def goback(self):
        summary_page.show()
        mail_page.close()





class Ui_search_page(object):
    def setupUi(self, search_page):
        search_page.setObjectName("search_page")
        search_page.resize(811, 518)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        search_page.setFont(font)
        search_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        search_page.setToolTip("")
        search_page.setWhatsThis("")
        search_page.setAccessibleName("")
        search_page.setAccessibleDescription("")
        self.attendanceWizard = QtWidgets.QWidget(search_page)
        self.attendanceWizard.setObjectName("attendanceWizard")
        self.backButton = QtWidgets.QCommandLinkButton(self.attendanceWizard)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 222, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.backButton.setFont(font)
        self.backButton.setToolTip("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("32-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.goback)
        self.searchOutput = QtWidgets.QTextBrowser(self.attendanceWizard)
        self.searchOutput.setGeometry(QtCore.QRect(20, 60, 571, 401))
        self.searchOutput.setObjectName("searchOutput")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchOutput.setFont(font)
        self.searchButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.searchButton.setGeometry(QtCore.QRect(620, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setToolTip("")
        self.searchButton.setToolTipDuration(2)
        self.searchButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.search)
        self.applyButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.applyButton.setGeometry(QtCore.QRect(620, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.applyButton.setFont(font)
        self.applyButton.setAcceptDrops(True)
        self.applyButton.setToolTip("")
        self.applyButton.setToolTipDuration(2)
        self.applyButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.applyButton.setAutoDefault(False)
        self.applyButton.setDefault(False)
        self.applyButton.setFlat(False)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.applyclicked)
        # self.ScrollBar = QtWidgets.QScrollBar(self.attendanceWizard)
        # self.ScrollBar.setGeometry(QtCore.QRect(590, 60, 16, 401))
        # self.ScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.ScrollBar.setObjectName("ScrollBar")
        self.rolnoLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.rolnoLabel.setGeometry(QtCore.QRect(610, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rolnoLabel.setFont(font)
        self.rolnoLabel.setObjectName("rolnoLabel")
        self.rollnoInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.rollnoInput.setGeometry(QtCore.QRect(690, 140, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rollnoInput.setFont(font)
        self.rollnoInput.setObjectName("rollnoInput")
        self.nameInput = QtWidgets.QLineEdit(self.attendanceWizard)
        self.nameInput.setGeometry(QtCore.QRect(690, 70, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nameInput.setFont(font)
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.nameLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.nameLabel.setGeometry(QtCore.QRect(610, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.orLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.orLabel.setGeometry(QtCore.QRect(680, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.orLabel.setFont(font)
        self.orLabel.setObjectName("orLabel")
        self.toLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.toLabel.setGeometry(QtCore.QRect(690, 350, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.fromInput = QtWidgets.QSpinBox(self.attendanceWizard)
        self.fromInput.setGeometry(QtCore.QRect(630, 350, 42, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fromInput.setFont(font)
        self.fromInput.setObjectName("fromInput")
        self.toInput = QtWidgets.QSpinBox(self.attendanceWizard)
        self.toInput.setGeometry(QtCore.QRect(720, 350, 42, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        self.toInput.setFont(font)
        self.toInput.setMaximum(100)
        self.toInput.setObjectName("toInput")
        self.rangeLabel = QtWidgets.QLabel(self.attendanceWizard)
        self.rangeLabel.setGeometry(QtCore.QRect(620, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rangeLabel.setFont(font)
        self.rangeLabel.setObjectName("rangeLabel")
        search_page.setCentralWidget(self.attendanceWizard)
        self.statusbar = QtWidgets.QStatusBar(search_page)
        self.statusbar.setObjectName("statusbar")
        search_page.setStatusBar(self.statusbar)

        self.retranslateUi(search_page)
        QtCore.QMetaObject.connectSlotsByName(search_page)

    def retranslateUi(self, search_page):
        _translate = QtCore.QCoreApplication.translate
        search_page.setWindowTitle(_translate("search_page", "Attendance Wizard "))
        self.backButton.setText(_translate("search_page", "Back"))
        self.searchButton.setText(_translate("search_page", "Search"))
        self.applyButton.setText(_translate("search_page", "Apply"))
        self.rolnoLabel.setText(_translate("search_page", "Roll no:"))
        self.nameLabel.setText(_translate("search_page", "Name:"))
        self.orLabel.setText(_translate("search_page", "OR"))
        self.toLabel.setText(_translate("search_page", "to"))
        self.rangeLabel.setText(_translate("search_page", "Range:"))
    def goback(self):
        summary_page.show()
        search_page.close()
    def search(self):
        name = self.nameInput.text()
        rno = self.rollnoInput.text()
        
        data = data_querying(create_connection(),name,rno,rep_ui.tablename)
        self.searchOutput.append(data)
        stud_wise_graph(rep_ui.frame,rno,name,create_connection(),rep_ui.tablename)

    def applyclicked(self):
        from_val = self.fromInput.value()
        to_val = self.toInput.value()
        in_between = range_attendance(from_val,to_val,create_connection(),rep_ui.tablename)
        self.searchOutput.append(in_between)


class Ui_summary_page(object):
    def setupUi(self, summary_page):
        summary_page.setObjectName("summary_page")
        summary_page.resize(783, 640)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        summary_page.setFont(font)
        summary_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        summary_page.setToolTip("")
        summary_page.setWhatsThis("")
        summary_page.setAccessibleName("")
        summary_page.setAccessibleDescription("")
        self.attendanceWizard = QtWidgets.QWidget(summary_page)
        self.attendanceWizard.setObjectName("attendanceWizard")
        self.graphButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.graphButton.setGeometry(QtCore.QRect(20, 530, 161, 51))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        self.graphButton.setFont(font)
        self.graphButton.setToolTip("")
        self.graphButton.setToolTipDuration(2)
        self.graphButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.graphButton.setObjectName("graphButton")
        self.graphButton.clicked.connect(self.show_graph)
        self.backButton = QtWidgets.QCommandLinkButton(self.attendanceWizard)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 222, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.backButton.setFont(font)
        self.backButton.setToolTip("")
        self.backButton.clicked.connect(self.goback)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("32-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backButton.setObjectName("backButton")
        self.summaryOutput = QtWidgets.QTextBrowser(self.attendanceWizard)
        self.summaryOutput.setGeometry(QtCore.QRect(20, 100, 731, 401))
        self.summaryOutput.setObjectName("summaryOutput")
        global printstring
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Monospace")
        self.summaryOutput.setText(printstring)
        self.summaryOutput.setFont(font)
        self.searchButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.searchButton.setGeometry(QtCore.QRect(220, 530, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setToolTip("")
        self.searchButton.setToolTipDuration(2)
        self.searchButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.search)
        self.saveButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.saveButton.setGeometry(QtCore.QRect(410, 530, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveButton.setFont(font)
        self.saveButton.setToolTip("")
        self.saveButton.setToolTipDuration(2)
        self.saveButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.save)
        self.mailDefaultersButton = QtWidgets.QPushButton(self.attendanceWizard)
        self.mailDefaultersButton.setGeometry(QtCore.QRect(600, 530, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mailDefaultersButton.setFont(font)
        self.mailDefaultersButton.setToolTip("")
        self.mailDefaultersButton.setToolTipDuration(2)
        self.mailDefaultersButton.setStyleSheet("QPushButton{\n"
"    color:white ;\n"
"    background-color:rgb(87, 25, 149);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(127, 54, 186); }")
        self.mailDefaultersButton.setObjectName("mailDefaultersButton")
        self.mailDefaultersButton.clicked.connect(self.mail)
        # self.ScrollBar = QtWidgets.QScrollBar(self.attendanceWizard)
        # self.ScrollBar.setGeometry(QtCore.QRect(750, 100, 16, 401))
        # self.ScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.ScrollBar.setObjectName("ScrollBar")
        self.summarylabel = QtWidgets.QLabel(self.attendanceWizard)
        self.summarylabel.setGeometry(QtCore.QRect(290, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.summarylabel.setFont(font)
        self.summarylabel.setObjectName("summarylabel")
        summary_page.setCentralWidget(self.attendanceWizard)
        self.statusbar = QtWidgets.QStatusBar(summary_page)
        self.statusbar.setObjectName("statusbar")
        summary_page.setStatusBar(self.statusbar)

        self.retranslateUi(summary_page)
        QtCore.QMetaObject.connectSlotsByName(summary_page)

    def retranslateUi(self, summary_page):
        _translate = QtCore.QCoreApplication.translate
        summary_page.setWindowTitle(_translate("summary_page", "Attendance Wizard "))
        self.graphButton.setText(_translate("summary_page", "Graph"))
        self.backButton.setText(_translate("summary_page", "Back"))
        self.searchButton.setText(_translate("summary_page", "Search"))
        self.saveButton.setText(_translate("summary_page", "Save"))
        self.mailDefaultersButton.setText(_translate("summary_page", "Mail Defaulters"))
        self.summarylabel.setText(_translate("summary_page", "Summary"))
    @staticmethod
    def show_graph(self):
        division_graph(rep_ui.frame)
    @staticmethod
    def search(self):
        summary_page.close()
        search_page.show()
    @staticmethod
    def mail(self):
        summary_page.close()
        mail_page.show()
    @staticmethod
    def save(self):
        global printstring
        name = QtWidgets.QFileDialog.getSaveFileName( summary_page,'Save File')
        print(name[0])
        save_as_pdf(printstring,name[0])
    @staticmethod
    def goback(self):
        summary_page.close()
        report_page.show()






import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_page = QtWidgets.QMainWindow()
    report_page = QtWidgets.QMainWindow()
    summary_page = QtWidgets.QMainWindow()
    mail_page = QtWidgets.QMainWindow()
    only_def = QtWidgets.QMainWindow()
    search_page = QtWidgets.QMainWindow()
    login_ui = Ui_login_page()
    rep_ui = Ui_ReportSelection_page()
    
    search_ui = Ui_search_page()
    mail_ui = Ui_mail_page()

    login_ui.setupUi(login_page)
    search_ui.setupUi(search_page)
    mail_ui.setupUi(mail_page)
    rep_ui.setupUi(report_page)
    

    login_page.show()
    sys.exit(app.exec_())

