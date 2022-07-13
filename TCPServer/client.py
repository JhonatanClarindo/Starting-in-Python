#!/usr/bin/python3

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

clientSocket.connect(('192.168.0.1', port))

message = clientSocket.recvfrom(1024)

clientSocket.close()

print(message.decode('ascii'))