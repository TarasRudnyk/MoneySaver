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
