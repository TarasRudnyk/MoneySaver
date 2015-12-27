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
    return False


def update_user_plan(login, value):
    date = datetime.now()
    month = date.month
    year = date.year
    year = str(year)[-2:]

    result = update_plane(login, month, year, value)
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

    exists = get_plane(login, month, year)
    if exists["plane"] == -1:
        create_plane(login, month, year)
