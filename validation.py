from PyQt5.QtWidgets import QMessageBox
from datetime import datetime

from server_connection import *


def auth_request(login, password):
    try:
        result = auth(login, password)
        if not result["success"]:
            return {
                "result": False,
                "message": "Перевірте правильність логіна і пароля."
            }
        return {
            "result": True,
            "role": result["role"]
        }
    except Exception as auth_exception:
        return {
            "result": False,
            "message": "Виникли проблеми з сервером.\nБудь ласка, спробуйте пізніше."
        }


def reg_request(login, password, phone, name, last_name, email):
    try:
        result = registration(login, password, name, last_name, phone, email)
        if not result["success"]:
            return {
                "result": False,
                "message": "Такий логін вже є в базі"
            }
        return {
            "result": True,
            "message": ""
        }

    except Exception as reg_exception:
        return {
            "result": False,
            "message": "Виникли проблеми з сервером.\nБудь ласка, спробуйте пізніше."
        }


def delete_user_request(login):
    try:
        delete_selected_user(login)
    except Exception as E:
        QMessageBox.information(self, 'no', "Виникли проблеми з сервером.\nБудь ласка, спробуйте пізніше.")
        return False
    return True


def update_user_plan(login, value):
    date = datetime.now()
    month = date.month
    year = date.year
    year = str(year)[-2:]
    try:
        result = update_plane(login, month, year, value)
    except Exception as E:
        QMessageBox.information(self, 'no', "Виникли проблеми з сервером.\nБудь ласка, спробуйте пізніше.")
        result = {
            "success": False
        }
    return result["success"]


def get_user_plan(login):
    date = datetime.now()
    month = date.month
    year = date.year
    year = str(year)[-2:]

    result = get_plane(login, month, year)
    return result["plane"]


def check_plan(login):
    date = datetime.now()
    month = date.month
    year = date.year
    year = str(year)[-2:]

    try:
        exists = get_plane(login, month, year)
    except Exception as E:
        exists = {
            "plane": -2
        }
    if exists["plane"] == -1:
        try:
            create_plane(login, month, year)
        except:
            QMessageBox.information(self, 'помилка', "помилка на сервері")



def get_balance(login):
    date = datetime.now()
    month = date.month
    year = date.year
    year = str(year)[-2:]

    date = "%{}%{}".format(month, year)
    try:
        costs = select_all_user_costs(login, date)
    except Exception as E:
        QMessageBox.information(self, 'помилка', "помилка на сервері")
        costs = {
            "sum_cost": [0]
        }
    try:
        plane = get_plane(login, month, year)
    except Exception as E:
        QMessageBox.information(self, 'помилка', "помилка на сервері")
        plane = {
            "plane": 0
        }

    balance = plane["plane"] - costs["sum_cost"][0]

    return balance
