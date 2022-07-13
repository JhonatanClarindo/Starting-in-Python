#!/usr/bin/python3
import socket;


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

serverSocket.bind((host, port))

serverSocket.listen(3)

while True:
    clientsocket, address = serverSocket.accept()

    print("received connection from " % str(address))

    message = "hello! Tks u for connecting to the server " + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()