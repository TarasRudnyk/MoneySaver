from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views import registration

from validation import check_email, reg_verification


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
            self.loginError.setText("Логін має бути не менше 5 символів!")
            result = False
        if len(login) == 0:
            self.loginError.setText("Це поле не може бути пустим!")
            result = False

        if len(password) < 8:
            self.passwordError.setText("Пароль має бути не менше 8 символів!")
            result = False
        if len(password) == 0:
            self.passwordError.setText("Це поле не може бути пустим!")
            result = False

        if password != repeat_password:
            self.repeatPassworError.setText("Введіть однакові паролі!")
            result = False

        if len(name) < 2:
            self.nameError.setText("Ім'я не може бути менше 2 символів!")
            result = False

        if len(last_name) < 2:
            self.lastNameError.setText("Прізвище не може бути менше 2 символів!")
            result = False

        if len(email) > 0 and not check_email(email):
            self.EmailError.setText("Ви ввели некоректний емайл!")
            result = False

        if result:
            if reg_verification(login, password, repeat_password, phone, name, last_name, email):
                QMessageBox.information(self, 'Зареєстровано', "Користувача успішно зареєстровано!")
                return True

        return False