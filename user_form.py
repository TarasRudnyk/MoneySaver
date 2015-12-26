from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import user_info_ui


class User(QtWidgets.QWidget, user_info_ui.Ui_UserInfo):

    def fill_table(self, month, year):
        self.costs_tableWidget.clear()

        month = translate_month(month)
        raw = 2

        self.costs_tableWidget.setColumnCount(4)
        self.costs_tableWidget.setRowCount(raw)
        self.costs_tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Категорія"))
        self.costs_tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Сума"))
        self.costs_tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Дата"))
        self.costs_tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Коментар"))

        self.costs_tableWidget.setItem(0, 0, QTableWidgetItem(""))



def translate_month(month):
    dictionary = {
        "Всі": 0,
        "Січень": 1,
        "Лютий": 2,
        "Березень": 3,
        "Квітень": 4,
        "Травень": 5,
        "Червнь": 6,
        "Липень": 7,
        "Серпень": 8,
        "Вересень": 9,
        "Жовтень": 10,
        "Листопад": 11,
        "Грудень": 12,
    }

    month = dictionary[month]
    return month

