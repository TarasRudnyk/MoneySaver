from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import plan_ui
from validation import change_user_plan, get_user_plan


class Plan(QtWidgets.QWidget, plan_ui.Ui_PlanWindow):
    pass
    def change_plan(self, login):
        value = self.money_lineEdit.text()
        change_user_plan(login, value)

    def show_user_plan(self, login):
        message = self.label.text()
        message += str(get_user_plan(login))
        self.label.setText(message)
