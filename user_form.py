from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import user_info_ui
from server_connection import select_month_user_info


class User(QtWidgets.QWidget, user_info_ui.Ui_UserInfo):

    def fill_table(self, login, month, year):
        self.costs_tableWidget.clear()

        month = translate_month(month)
        cost = "%" + str(month) + "%" + year[-2:]
        print(cost)
        try:
            data = select_month_user_info(login, cost)
        except Exception as E:
            data = {
                "cost_sum": []
            }
        raw = len(data["cost_sum"])

        self.costs_tableWidget.setColumnCount(4)
        self.costs_tableWidget.setRowCount(raw)
        self.costs_tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Category"))
        self.costs_tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Sum"))
        self.costs_tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Date"))
        self.costs_tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Comment"))

        for i in range(raw):
            datetime = data["cost_date"][i]
            datetime = str(datetime).split(" ")[0] + " " + str(data["cost_time"][i])
            self.costs_tableWidget.setItem(i, 0, QTableWidgetItem(data["cost_category"][i]))
            self.costs_tableWidget.setItem(i, 1, QTableWidgetItem(str(data['cost_sum'][i])))
            self.costs_tableWidget.setItem(i, 2, QTableWidgetItem(datetime))
            self.costs_tableWidget.setItem(i, 3, QTableWidgetItem(data['cost_comment'][i]))



def translate_month(month):
    dictionary = {
        "All": "%",
        "January": "JAN",
        "February": "FEB",
        "Mart": "MAR",
        "April": "APR",
        "May": "MAY",
        "June": "JUN",
        "Julie": "JUL",
        "August": "AUG",
        "September": "SEP",
        "October": "OCT",
        "November": "NOV",
        "December": "DEC",
    }

    month = dictionary[month]
    return month

