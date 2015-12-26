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
        data = select_month_user_info(login, cost)
        raw = len(data["cost_sum"])

        self.costs_tableWidget.setColumnCount(4)
        self.costs_tableWidget.setRowCount(raw)
        self.costs_tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Категорія"))
        self.costs_tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Сума"))
        self.costs_tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Дата"))
        self.costs_tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Коментар"))

        for i in range(raw):
            self.costs_tableWidget.setItem(i, 0, QTableWidgetItem(data["cost_category"][i]))
            self.costs_tableWidget.setItem(i, 1, QTableWidgetItem(str(data['cost_sum'][i])))
            self.costs_tableWidget.setItem(i, 2, QTableWidgetItem(data['cost_date'][i]))
            self.costs_tableWidget.setItem(i, 3, QTableWidgetItem(data['cost_comment'][i]))



def translate_month(month):
    dictionary = {
        "Всі": "%",
        "Січень": "01",
        "Лютий": "02",
        "Березень": "03",
        "Квітень": "04",
        "Травень": "05",
        "Червнь": "06",
        "Липень": "07",
        "Серпень": "08",
        "Вересень": "09",
        "Жовтень": "10",
        "Листопад": "11",
        "Грудень": "12",
    }

    month = dictionary[month]
    return month

