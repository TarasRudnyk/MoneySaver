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

from validation import delete_user_request, check_plan
from server_connection import get_plane, create_plane
login = ""
cost = 0


class Window(authorization_form.Authorization):

    def __init__(self):
        global login
        super().__init__()

        self.setupUi(self)
        self.show()
        login = ""
        self.pushButton.clicked.connect(self.show_user_or_admin_form)
        self.pushButton_2.clicked.connect(self.show_registration)
        self.LoginlineEdit.returnPressed.connect(self.pushButton.click)
        self.PasswordlineEdit_2.returnPressed.connect(self.pushButton.click)

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
        global login
        result = self.validate_auth_data()
        if result["result"]:
            login = self.LoginlineEdit.text()
            if result["role"] == "admin":
                self.show_admin()
            else:
                self.show_user_info()


    def show_admin(self):
        global login
        self.adm = admin_form.Admin()
        self.dialog_adm = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_adm.setWindowTitle("MoneySaver - admin page - " + login)
        self.adm.setupUi(self.dialog_adm)

        self.adm.fill_table()

        self.adm.back_button.clicked.connect(self.dialog_adm.close)
        self.adm.pushButton.clicked.connect(self.adm.fill_table)
        self.adm.remove_user_button.clicked.connect(self.delete_user)

        self.close()
        self.dialog_adm.show()
        self.dialog_adm.exec()
        self.show()

    def delete_user(self):
        global login
        row = self.adm.users_info_table_widget.currentRow()
        if row != -1:
            login1 = self.adm.users_info_table_widget.item(row, 0).text()
            reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to delete user {0}?".format(login1),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                try:
                    if delete_user_request(login1):
                        self.adm.fill_table()
                        QMessageBox.information(self, 'Deleting', "User has been removed successfully")
                    else:
                        QMessageBox.information(self, 'no', "There is problems with server.\n Please, try later.")

                except Exception as delete_exception:
                    QMessageBox.information(self, 'Deleting', "Error.\nPlease,"
                                                               " try later.")
            else:
                QMessageBox.information(self, 'Deleting', "Deleting has been canceled")
        else:
            QMessageBox.information(self, 'Error', "Please select any user")

        self.adm.users_info_table_widget.setCurrentCell(-1, -1)

    def show_user_info(self):
        global login
        self.user = user_form.User()
        self.dialog_usr = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_usr.setWindowTitle("MoneySaver - user page - " + login)
        self.user.setupUi(self.dialog_usr)
        self.user.confirm_button.clicked.connect(self.show_user_history)
        self.user.back_button.clicked.connect(self.dialog_usr.close)
        self.user.refresh_data_button.clicked.connect(self.show_user_history)
        self.user.edit_plane_button.clicked.connect(self.show_plan)
        self.user.add_new_cost_button.clicked.connect(self.show_cost)

        check_plan(login)

        self.close()
        self.dialog_usr.show()
        self.dialog_usr.exec()
        self.show()

    def show_user_history(self):
        global login
        month = self.user.month_comboBox.currentText()
        year = self.user.year_comboBox.currentText().split(" ")[0]
        self.user.fill_table(login, month, year)

    def show_plan(self):
        global login
        self.plan = plan_form.Plan()
        self.dialog_pln = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_pln.setWindowTitle("MoneySaver - plan page - " + login)
        self.plan.setupUi(self.dialog_pln)
        self.plan.back_button.clicked.connect(self.dialog_pln.close)
        self.plan.save_button.clicked.connect(self.update_pln)
        self.plan.show_user_plan(login)

        self.dialog_pln.show()

    def update_pln(self):
        global login
        result = self.plan.update_plan(login)
        if result:
            QMessageBox.information(self, 'ok', "plane has been changed")
            self.dialog_pln.close()

    def show_cost(self):
        global login
        self.cost = add_cost_form.AddCost()
        self.dialog_cst = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.dialog_cst.setWindowTitle("MoneySaver - adding cost page - " + login)
        self.cost.setupUi(self.dialog_cst)
        self.cost.back_button.clicked.connect(self.dialog_cst.close)
        self.cost.save_button.clicked.connect(self.adding_cost)

        self.dialog_cst.show()

    def adding_cost(self):
        global login
        result = self.cost.add_cost(login)
        if result:
            self.dialog_cst.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
