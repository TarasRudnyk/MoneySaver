from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views import authorization

from validation import auth_request


class Authorization(QtWidgets.QWidget, authorization.Ui_Authorization):

    def validate_auth_data(self):
        result = True

        self.LoginError.setText("")
        self.PasswordError.setText("")

        login = self.LoginlineEdit.text()
        password = self.PasswordlineEdit_2.text()

        if len(login) == 0:
            self.LoginError.setText("This field can't be empty!")
            result = False

        if len(password) == 0:
            self.PasswordError.setText("This field can't be empty!")
            result = False

        if result:
            auth = auth_request(login, password)
            if not auth["result"]:
                QMessageBox.information(self, 'Error', auth["message"])
                return {"result": False}
            return auth
        return {"result": False}