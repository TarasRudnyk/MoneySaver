from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import plan_ui
from validation import update_user_plan, get_user_plan


class Plan(QtWidgets.QWidget, plan_ui.Ui_PlanWindow):
    def update_plan(self, login):
        value = self.money_lineEdit.text()
        new_money = update_user_plan(login, value)
        if new_money:
            return True
        return False


    def show_user_plan(self, login):
        try:
            message = "Ваш поточний фінансовий план: " + str(get_user_plan(login))
        except:
            message = "Ваш поточний фінансовий план: 0"

        self.label.setText(message)
