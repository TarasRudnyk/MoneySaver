import re


def auth_verification(login, password):
    return True


def reg_verification(login, password, repeat_password, phone, name, last_name, email):
    return True


def check_email(email):
    if re.match("^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$", email):
        return True
    return False
