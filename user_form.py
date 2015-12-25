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

        self.costs_tableWidget.setItem(0, 0, QTableWidgetItem(year))



def translate_month(month):
    dictionary = {
        "Січень": 0,
        "Лютий": 1,
        "Березень": 2,
        "Квітень": 3,
        "Травень": 4,
        "Червнь": 5,
        "Липень": 6,
        "Серпень": 7,
        "Вересень": 8,
        "Жовтень": 9,
        "Листопад": 10,
        "Грудень": 11,
    }

    month = dictionary[month]
    return month

