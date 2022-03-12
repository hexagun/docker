#!/usr/bin/python3

import socket
import json
import time

# HOST = '0.0.0.0'
HOST = socket.gethostbyname('ipc_dns')
PORT = 9898

with socket.socket(socket.AF_INET, \
    socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        str = json.dumps({'4': 5, '6': 7})
        s.sendall(bytes(str, 'utf-8'))
        time.sleep(1)

    # s.sendmsg(str)
    
    # s.sendall(b'Hello, World. IPC success!')
    # s.sendall(bytes(str, 'utf-8'))
    # data = s.recv(1024)

# print('Received', repr(data))