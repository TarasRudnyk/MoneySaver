from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from views import admin_ui
# from validation import get_all_users
from server_connection import get_all_users


class Admin(QtWidgets.QWidget, admin_ui.Ui_AdminWindow):

    def fill_table(self):
        self.users_info_table_widget.clear()

        try:
            request = get_all_users()
        except:
            request = {
                'users_logins': []
            }
        raw = len(request['users_logins'])
        self.users_info_table_widget.setRowCount(raw)
        self.users_info_table_widget.setColumnCount(5)

        self.users_info_table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Login"))
        self.users_info_table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Last name"))
        self.users_info_table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("First name"))
        self.users_info_table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Phone number"))
        self.users_info_table_widget.setHorizontalHeaderItem(4, QTableWidgetItem("Email"))

        for i in range(raw):
            self.users_info_table_widget.setItem(i, 0, QTableWidgetItem(request["users_logins"][i]))
            self.users_info_table_widget.setItem(i, 1, QTableWidgetItem(request["users_last_names"][i]))
            self.users_info_table_widget.setItem(i, 2, QTableWidgetItem(request["users_first_names"][i]))
            self.users_info_table_widget.setItem(i, 3, QTableWidgetItem(request["users_phone_numbers"][i]))
            self.users_info_table_widget.setItem(i, 4, QTableWidgetItem(request["users_emails"][i]))





