from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from views import admin_ui


class Admin(QtWidgets.QWidget, admin_ui.Ui_AdminWindow):

    def fill_table(self):
        raw = 3
        self.users_info_table_widget.setRowCount(raw)
        self.users_info_table_widget.setColumnCount(5)

        self.users_info_table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Логін"))
        self.users_info_table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Прізвище"))
        self.users_info_table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Ім\'я"))
        self.users_info_table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Номер телефону"))
        self.users_info_table_widget.setHorizontalHeaderItem(4, QTableWidgetItem("Емейл"))

        for i in range(raw):
            self.users_info_table_widget.setItem(i, 0, QTableWidgetItem("login" + str(i)))
            self.users_info_table_widget.setItem(i, 1, QTableWidgetItem("last name"))
            self.users_info_table_widget.setItem(i, 2, QTableWidgetItem("name"))
            self.users_info_table_widget.setItem(i, 3, QTableWidgetItem("number"))
            self.users_info_table_widget.setItem(i, 4, QTableWidgetItem("email"))





