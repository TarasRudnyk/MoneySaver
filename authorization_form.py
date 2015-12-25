from PyQt5 import QtWidgets

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
            self.LoginError.setText("Це поле не може бути пустим!")
            result = False

        if len(password) == 0:
            self.PasswordError.setText("Це поле не може бути пустим!")
            result = False

        if result:
            if auth_request(login, password):
                return {"success": True,
                        "role": "admin"}

        return {"success": False}
