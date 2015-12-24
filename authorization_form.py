from PyQt5 import QtWidgets

from views import authorization

from validation import auth_verification


class Authorization(QtWidgets.QWidget, authorization.Ui_Authorization):

    def validate_auth_data(self):

        self.LoginError.setText("")
        self.PasswordError.setText("")

        login = self.LoginlineEdit.text()
        password = self.PasswordlineEdit_2.text()

        if len(login) == 0:
            self.LoginError.setText("Це поле не може бути пустим!")

        if len(password) == 0:
            self.PasswordError.setText("Це поле не може бути пустим!")

        if auth_verification(login, password):
            pass
