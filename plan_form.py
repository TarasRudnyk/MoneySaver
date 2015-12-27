from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import plan_ui
from validation import update_user_plan, get_user_plan, get_balance


class Plan(QtWidgets.QWidget, plan_ui.Ui_PlanWindow):
    def update_plan(self, login):
        value = self.money_lineEdit.text()
        new_money = update_user_plan(login, value)
        if new_money["success"]:
            return True
        QMessageBox.information(self, 'Error', new_money["message"])
        return False


    def show_user_plan(self, login):
        try:
            message = "Yours current financial plane: {0} (balance: {1})"\
                .format(str(get_user_plan(login)), get_balance(login)["bal"])
        except:
            message = "Yours current financial plane: {0} (balance: {0})".format(str(get_user_plan(login)))

        self.label.setText(message)
