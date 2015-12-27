import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import user_new_cost_ui
from server_connection import add_new_cost
from validation import get_balance


class AddCost(QtWidgets.QWidget, user_new_cost_ui.Ui_NewCost):
    def check_data(self):
        if len(self.summary_price_lineEdit.text()) == 0:
            return False
        return True

    def add_cost(self, login):
        if self.check_data():
            summ = self.summary_price_lineEdit.text()
            category = self.category_comboBox.currentText()
            comment = self.comment_textEdit.toPlainText()
            summ = summ.lstrip("0")
            date = datetime.datetime.now()
            time = "{}:{}:{}".format(date.hour, date.minute, date.second)
            date = "{}-{}-{}".format(date.day, date.month, date.year)

            result = add_new_cost(login, summ, category, comment, date, time)
            if result["success"]:
                bal = get_balance(login)
                message = "витрату доданою\nваш баланс: {}".format(bal)
                QMessageBox.information(self, 'успіх', message)
                return True
            else:
                QMessageBox.information(self, 'Помилка', "спробуйте пініше")
        else:
            QMessageBox.information(self, 'Помилка', "Заповніть поле 'Сума витрати'!")
            return False
