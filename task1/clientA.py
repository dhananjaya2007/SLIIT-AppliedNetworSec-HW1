#!/usr/bin/env python3

import socket


IP = "127.0.0.1" #loopback
PORT = 8090   #non-privileged ports > 1023
AMT_DATA = 64

#socket () function

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as mySocket:
    #connect
    mySocket.connect((IP,PORT))
    mySocket.sendall("A".encode())
    data = mySocket.recv(AMT_DATA)

print("Received with thanks: ", repr(data))

