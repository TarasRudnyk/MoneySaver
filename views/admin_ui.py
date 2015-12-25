# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(1360, 700)
        AdminWindow.setMinimumSize(QtCore.QSize(1360, 700))
        AdminWindow.setMaximumSize(QtCore.QSize(1360, 700))
        self.gridLayout = QtWidgets.QGridLayout(AdminWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.back_button = QtWidgets.QPushButton(AdminWindow)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 1, 0, 1, 1)
        self.remove_user_button = QtWidgets.QPushButton(AdminWindow)
        self.remove_user_button.setObjectName("remove_user_button")
        self.gridLayout.addWidget(self.remove_user_button, 1, 1, 1, 1)
        self.users_info_table_widget = QtWidgets.QTableWidget(AdminWindow)
        self.users_info_table_widget.setObjectName("users_info_table_widget")
        # self.users_info_table_widget.setColumnCount(5)
        # self.users_info_table_widget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.users_info_table_widget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.users_info_table_widget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.users_info_table_widget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.users_info_table_widget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.users_info_table_widget.setHorizontalHeaderItem(4, item)
        self.users_info_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.users_info_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.users_info_table_widget.horizontalHeader().setDefaultSectionSize(245)
        self.users_info_table_widget.horizontalHeader().setStretchLastSection(True)
        self.users_info_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.users_info_table_widget, 0, 0, 1, 2)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Сторінка адміністратора"))
        self.back_button.setText(_translate("AdminWindow", "Вийти"))
        self.remove_user_button.setText(_translate("AdminWindow", "Видалити"))
        self.users_info_table_widget.setSortingEnabled(True)
        # item = self.users_info_table_widget.horizontalHeaderItem(0)
        # item.setText(_translate("AdminWindow", "Логін"))
        # item = self.users_info_table_widget.horizontalHeaderItem(1)
        # item.setText(_translate("AdminWindow", "Прізвище"))
        # item = self.users_info_table_widget.horizontalHeaderItem(2)
        # item.setText(_translate("AdminWindow", "Ім\'я"))
        # item = self.users_info_table_widget.horizontalHeaderItem(3)
        # item.setText(_translate("AdminWindow", "Номер телефону"))
        # item = self.users_info_table_widget.horizontalHeaderItem(4)
        # item.setText(_translate("AdminWindow", "Емейл"))

