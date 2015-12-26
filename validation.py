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


def reg_request(login, password, repeat_password, phone, name, last_name, email):
    return True


def delete_user_request(login):
    return False


def select_month_user_info(login, cost_date):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "get_user_info",
                 "cost_date": cost_date,
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data



def change_user_plan(login, value):
    return True

def get_user_plan(login):
    return 825