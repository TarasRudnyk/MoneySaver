import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtWidgets

import authorization_form
import registration_form
import admin_form


class Window(authorization_form.Authorization):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.show_admin)
        self.pushButton_2.clicked.connect(self.show_registration)

    def show_registration(self):

        self.reg = registration_form.Registration()
        self.dialog_reg = QtWidgets.QDialog()
        self.reg.setupUi(self.dialog_reg)
        self.reg.RegisterPushButton.clicked.connect(self.validate_registration)

        self.close()
        self.dialog_reg.show()
        self.dialog_reg.exec()
        self.show()

    def validate_registration(self):
        result = self.reg.validate_reg_data()
        if result:
            self.dialog_reg.close()

    def show_admin(self):
        if self.validate_auth_data():
            self.adm = admin_form.Admin()
            self.dialog_adm = QtWidgets.QDialog()
            self.adm.setupUi(self.dialog_adm)

            self.close()
            self.dialog_adm.show()
            self.dialog_adm.exec()
            self.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
