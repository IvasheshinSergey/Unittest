# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Вторая практика\Dff\file2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 177)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: qconicalgradient(cx:0.505773, cy:0.517, angle:317.8, stop:0.0852273 rgba(65, 103, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(66, 7, 198, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(66, 35, 275, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 34, 49, 22))
        self.label.setStyleSheet("#label{\n"
"font: 12pt \"Matura MT Script Capitals\";\n"
"color: #000000;\n"
"background:#3a09e8;\n"
"border-radius: 10px;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 101, 36))
        self.pushButton.setStyleSheet("#pushButton {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"color: #000000;\n"
"background: #3a09e8;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"background: #2d7391;\n"
"color: #000000;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(11, 6, 49, 22))
        self.label_3.setStyleSheet("#label_3{\n"
"font: 12pt \"Matura MT Script Capitals\";\n"
"color: #000000;\n"
"background:#3a09e8;\n"
"border-radius: 10px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 80, 71, 36))
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"color: #000000;\n"
"background: #3a09e8;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"background: #2d7391;\n"
"color: #000000;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 80, 171, 31))
        self.pushButton_3.setStyleSheet("#pushButton_3 {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"color: #000000;\n"
"background: #3a09e8;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"font: 20pt \"Matura MT Script Capitals\";\n"
"background: #2d7391;\n"
"color: #000000;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.pushButton.setText(_translate("MainWindow", "ok"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.pushButton_2.setText(_translate("MainWindow", "cansel"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Image"))
