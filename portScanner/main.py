#!/usr/bin/python3

import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.timeout(7)

host = input("Enter the IP u want to scan: ")
port = int(input("Enter the port u want to scan: "))

def portScanner(port):
    if skt.connect_ex((host, port)):
        print("Port is open")
    else:
        print("Port is closed")

portScanner(port)