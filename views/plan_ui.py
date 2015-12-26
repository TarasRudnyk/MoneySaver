# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlanWindow(object):
    def setupUi(self, PlanWindow):
        PlanWindow.setObjectName("PlanWindow")
        PlanWindow.resize(377, 205)
        PlanWindow.setMinimumSize(QtCore.QSize(377, 205))
        PlanWindow.setMaximumSize(QtCore.QSize(377, 205))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlanWindow.setWindowIcon(icon)
        self.money_label = QtWidgets.QLabel(PlanWindow)
        self.money_label.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.money_label.setObjectName("money_label")
        self.money_lineEdit = QtWidgets.QLineEdit(PlanWindow)
        self.money_lineEdit.setGeometry(QtCore.QRect(180, 70, 171, 20))
        self.money_lineEdit.setObjectName("money_lineEdit")
        self.money_lineEdit.setInputMask("D99999")
        self.back_button = QtWidgets.QPushButton(PlanWindow)
        self.back_button.setGeometry(QtCore.QRect(40, 140, 110, 23))
        self.back_button.setObjectName("back_button")
        self.save_button = QtWidgets.QPushButton(PlanWindow)
        self.save_button.setGeometry(QtCore.QRect(240, 140, 110, 23))
        self.save_button.setObjectName("save_button")
        self.label = QtWidgets.QLabel(PlanWindow)
        self.label.setGeometry(QtCore.QRect(50, 20, 250, 16))
        self.label.setObjectName("label")

        self.retranslateUi(PlanWindow)
        QtCore.QMetaObject.connectSlotsByName(PlanWindow)

    def retranslateUi(self, PlanWindow):
        _translate = QtCore.QCoreApplication.translate
        PlanWindow.setWindowTitle(_translate("PlanWindow", "План"))
        self.money_label.setText(_translate("PlanWindow", "Введіть суму (грн)"))
        self.back_button.setText(_translate("PlanWindow", "Назад"))
        self.save_button.setText(_translate("PlanWindow", "Зберегти"))
        self.label.setText(_translate("PlanWindow", "Ваш поточний фінансовий план: "))

