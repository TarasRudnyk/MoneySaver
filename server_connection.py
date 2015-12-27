import socket
import json

import db_connection


def auth(login, password):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": True,
                 "login": login,
                 "password": password,
                 "action": "authorization"
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


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


def add_new_cost(login, summ, category, comment, date, time):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "add_new_cost",
                 "cost_data": {
                     "cost_category": category,
                     "cost_money_summ": summ,
                     "cost_comment": comment,
                     "cost_date": date,
                     "cost_time": time
                 },
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    print(data)
    data = json.loads(data.decode('utf-8'))
    return data


def get_plane(login, month, year):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "get_plane",
                 "month": month,
                 "year": year
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    return data


def create_plane(login, month, year):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "create_plane",
                 "month": month,
                 "year": year
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    return data


def update_plane(login, month, year, money):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "update_plane",
                 "month": month,
                 "year": year,
                 "money": money
                 }
    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    print(data)
    return data


def registration(login, password, first_name, last_name, phone_number, email):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "action": "registration",
                 "user_data": {
                     "user_login": login,
                     "user_password": password,
                     "user_first_name": first_name,
                     "user_last_name": last_name,
                     "user_phone_number": phone_number,
                     "user_email": email,
                     "user_role": "user"
                     }
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    return data


def get_all_users():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "action": "get_all_users",
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    return data


def delete_selected_user(login):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "delete_selected_user",
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    data = json.loads(data.decode('utf-8'))
    print(data)
