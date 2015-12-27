# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_new_cost.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewCost(object):
    def setupUi(self, NewCost):
        NewCost.setObjectName("NewCost")
        NewCost.resize(400, 298)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewCost.setWindowIcon(icon)
        self.summary_price_label = QtWidgets.QLabel(NewCost)
        self.summary_price_label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.summary_price_label.setObjectName("summary_price_label")
        self.category_label = QtWidgets.QLabel(NewCost)
        self.category_label.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.category_label.setObjectName("category_label")
        self.comment_label = QtWidgets.QLabel(NewCost)
        self.comment_label.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.comment_label.setObjectName("comment_label")
        self.save_button = QtWidgets.QPushButton(NewCost)
        self.save_button.setGeometry(QtCore.QRect(230, 240, 131, 23))
        self.save_button.setObjectName("save_button")
        self.back_button = QtWidgets.QPushButton(NewCost)
        self.back_button.setGeometry(QtCore.QRect(20, 240, 131, 23))
        self.back_button.setObjectName("back_button")
        self.summary_price_lineEdit = QtWidgets.QLineEdit(NewCost)
        self.summary_price_lineEdit.setGeometry(QtCore.QRect(150, 30, 113, 20))
        self.summary_price_lineEdit.setObjectName("summary_price_lineEdit")
        self.summary_price_lineEdit.setInputMask("999999")
        self.category_comboBox = QtWidgets.QComboBox(NewCost)
        self.category_comboBox.setGeometry(QtCore.QRect(150, 80, 111, 22))
        self.category_comboBox.setObjectName("category_comboBox")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.comment_textEdit = QtWidgets.QTextEdit(NewCost)
        self.comment_textEdit.setGeometry(QtCore.QRect(150, 140, 241, 61))
        self.comment_textEdit.setObjectName("comment_textEdit")

        self.retranslateUi(NewCost)
        QtCore.QMetaObject.connectSlotsByName(NewCost)

    def retranslateUi(self, NewCost):
        _translate = QtCore.QCoreApplication.translate
        self.summary_price_label.setText(_translate("NewCost", "Costs sum (grn)"))
        self.category_label.setText(_translate("NewCost", "Category"))
        self.comment_label.setText(_translate("NewCost", "Comment"))
        self.save_button.setText(_translate("NewCost", "Save"))
        self.back_button.setText(_translate("NewCost", "Back"))
        self.category_comboBox.setItemText(0, _translate("NewCost", "Food"))
        self.category_comboBox.setItemText(1, _translate("NewCost", "Journey"))
        self.category_comboBox.setItemText(2, _translate("NewCost", "Clothes"))
        self.category_comboBox.setItemText(3, _translate("NewCost", "Entertainments"))
        self.category_comboBox.setItemText(4, _translate("NewCost", "Gifts"))
        self.category_comboBox.setItemText(5, _translate("NewCost", "Internet"))
        self.category_comboBox.setItemText(6, _translate("NewCost", "Phone"))
        self.category_comboBox.setItemText(7, _translate("NewCost", "Other"))

