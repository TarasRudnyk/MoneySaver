import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtWidgets
import authorization_form
import registration_form


class Window(authorization_form.Authorization):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.validate_auth_data)
        self.pushButton_2.clicked.connect(self.show_registration)

    def show_registration(self):

        self.reg = registration_form.Registration()
        self.dialog = QtWidgets.QDialog()
        self.reg.setupUi(self.dialog)
        self.reg.RegisterPushButton.clicked.connect(self.validate_registration)

        self.close()
        self.dialog.show()
        self.dialog.exec()
        self.show()

    def validate_registration(self):
        result = self.reg.validate_reg_data()
        if result:
            self.dialog.close()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
