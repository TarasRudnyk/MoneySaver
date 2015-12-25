# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(378, 182)
        Authorization.setMinimumSize(QtCore.QSize(378, 182))
        Authorization.setMaximumSize(QtCore.QSize(378, 182))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Authorization.setWindowIcon(icon)
        self.loginLabel = QtWidgets.QLabel(Authorization)
        self.loginLabel.setGeometry(QtCore.QRect(20, 23, 67, 16))
        self.loginLabel.setObjectName("loginLabel")
        self.passwordLabel = QtWidgets.QLabel(Authorization)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 83, 78, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.LoginlineEdit = QtWidgets.QLineEdit(Authorization)
        self.LoginlineEdit.setGeometry(QtCore.QRect(131, 23, 201, 20))
        self.LoginlineEdit.setObjectName("LoginlineEdit")
        self.PasswordlineEdit_2 = QtWidgets.QLineEdit(Authorization)
        self.PasswordlineEdit_2.setGeometry(QtCore.QRect(131, 83, 201, 20))
        self.PasswordlineEdit_2.setObjectName("PasswordlineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Authorization)
        self.pushButton.setGeometry(QtCore.QRect(128, 140, 90, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Authorization)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 140, 90, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.LoginError = QtWidgets.QLabel(Authorization)
        self.LoginError.setGeometry(QtCore.QRect(131, 49, 238, 16))
        self.LoginError.setText("")
        self.LoginError.setObjectName("LoginError")
        self.PasswordError = QtWidgets.QLabel(Authorization)
        self.PasswordError.setGeometry(QtCore.QRect(131, 109, 238, 16))
        self.PasswordError.setText("")
        self.PasswordError.setObjectName("PasswordError")

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Form"))
        self.loginLabel.setText(_translate("Authorization", "Введіть логін"))
        self.passwordLabel.setText(_translate("Authorization", "Введіть пароль"))
        self.pushButton.setText(_translate("Authorization", "Увійти"))
        self.pushButton_2.setText(_translate("Authorization", "Реєстрація"))

