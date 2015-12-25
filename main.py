import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QMessageBox

import authorization_form
import registration_form
import admin_form
import user_form
import plan_form
import add_cost_form

from validation import delete_user_request

login = ""

class Window(authorization_form.Authorization):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.show_user_or_admin_form)
        self.pushButton_2.clicked.connect(self.show_registration)

    def show_registration(self):

        self.reg = registration_form.Registration()
        self.dialog_reg = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.reg.setupUi(self.dialog_reg)
        self.reg.RegisterPushButton.clicked.connect(self.validate_registration)
        self.reg.BackPushButton.clicked.connect(self.dialog_reg.close)

        self.close()
        self.dialog_reg.show()
        self.dialog_reg.exec()
        self.show()

    def validate_registration(self):
        result = self.reg.validate_reg_data()
        if result:
            self.dialog_reg.close()

    def show_user_or_admin_form(self):
        result = self.validate_auth_data()
        if result["success"]:
            if result["role"] == "admin":
                self.show_admin()
            else:
                self.show_user_info()

    def show_admin(self):
        self.adm = admin_form.Admin()
        self.dialog_adm = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.adm.setupUi(self.dialog_adm)
        self.adm.fill_table()

        self.adm.back_button.clicked.connect(self.dialog_adm.close)
        self.adm.remove_user_button.clicked.connect(self.delete_user)

        self.close()
        self.dialog_adm.show()
        self.dialog_adm.exec()
        self.show()

    def delete_user(self):
        row = self.adm.users_info_table_widget.currentRow()
        if row != -1:
            login = self.adm.users_info_table_widget.item(row, 0).text()
            try:
                if delete_user_request(login):
                    QMessageBox.information(self, 'Видалення', "Користувач видалений")
            except Exception as delete_exception:
                QMessageBox.information(self, 'Видалення', "Виникли проблеми при видаленні.\nБудь ласка,"
                                                           " спробуйте повторити пізніше.")
        else:
            QMessageBox.information(self, 'Помилка', "Виберіть користувача")

        self.adm.users_info_table_widget.setCurrentCell(-1, -1)

    def show_user_info(self):
        self.user = user_form.User()
        self.dialog_usr = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.user.setupUi(self.dialog_usr)
        self.user.confirm_button.clicked.connect(self.show_user_history)
        self.user.back_button.clicked.connect(self.dialog_usr.close)
        self.user.refresh_data_button.clicked.connect(self.show_user_history)
        self.user.edit_plane_button.clicked.connect(self.show_plan)
        self.user.add_new_cost_button.clicked.connect(self.show_cost)

        self.close()
        self.dialog_usr.show()
        self.dialog_usr.exec()
        self.show()

    def show_user_history(self):
        month = self.user.month_comboBox.currentText()
        year = self.user.year_comboBox.currentText().split(" ")[0]
        self.user.fill_table(month, year)

    def show_plan(self):
        global login
        self.plan = plan_form.Plan()
        self.dialog_pln = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.plan.setupUi(self.dialog_pln)
        self.plan.back_button.clicked.connect(self.dialog_pln.close)
        self.plan.show_user_plan(login)

        self.dialog_pln.show()

    def show_cost(self):
        global login
        self.cost = add_cost_form.Add_cost()
        self.dialog_cst = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.cost.setupUi(self.dialog_cst)

        self.dialog_cst.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
