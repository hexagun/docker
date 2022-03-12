#!/usr/bin/python3

import socket

# HOST = '0.0.0.0'
HOST = socket.gethostbyname('ipc_dns')
PORT = 9898

with socket.socket(socket.AF_INET, \
    socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # conn.sendall(data)
            print(data.decode("utf-8"))