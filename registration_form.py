import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views import registration

from validation import reg_request


class Registration(QtWidgets.QWidget, registration.Ui_Registration):

    def validate_reg_data(self):

        result = True

        self.loginError.setText("")
        self.passwordError.setText("")
        self.repeatPassworError.setText("")
        self.phoneNumberError.setText("")
        self.nameError.setText("")
        self.lastNameError.setText("")
        self.EmailError.setText("")

        login = self.loginLineEdit.text()
        password = self.passwordLineEdit.text()
        repeat_password = self.repeatPasswordLineEdit.text()
        phone = self.phoneNumberLineEdit.text()
        name = self.nameLineEdit.text()
        last_name = self.lastNameLineEdit.text()
        email = self.emailLineEdit.text()

        if len(login) < 5:
            self.loginError.setText("Login should be not less than 5 symbols!")
            result = False
        if len(login) == 0:
            self.loginError.setText("This field can't be empty")
            result = False

        if len(password) < 5:
            self.passwordError.setText("Password should be not less than 5 symbols!")
            result = False
        if len(password) == 0:
            self.passwordError.setText("This field can't be empty")
            result = False

        if password != repeat_password:
            self.repeatPassworError.setText("Password and repeated password is not match!")
            result = False
        if len(repeat_password) == 0:
            self.repeatPassworError.setText("This field can't be empty!")
            result = False

        if len(phone) == 0:
            self.phoneNumberError.setText("This field can't be empty!")
            result = False

        if not name.isalpha():
            self.nameError.setText("Please enter only letters!")
        if len(name) < 2:
            self.nameError.setText("First name can't be lass than 2 letters")
            result = False

        if not last_name.isalpha():
            self.lastNameError.setText("Please enter only letters!")
            result = False
        if len(last_name) < 2:
            self.lastNameError.setText("Last name can't be less than 2 letters")
            result = False

        if not check_email(email):
            self.EmailError.setText("Please enter correct email address")
            result = False
        if len(email) == 0:
            self.EmailError.setText("This field can't be empty!")
            result = False

        if result:
            request = reg_request(login, password, phone, name, last_name, email)
            if request["result"]:
                QMessageBox.information(self, 'Success', "user registered successfully")
                return True
            else:
                QMessageBox.information(self, 'Error', request["message"])
        return False


def check_email(email):
    if re.match("^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$", email):
        return True
    return False