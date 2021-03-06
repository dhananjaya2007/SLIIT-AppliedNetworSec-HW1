#!/usr/bin/env python3

import socket
import struct

IP = "127.0.0.1" #loopback
PORT = 8091   #non-privileged ports > 1023
AMT_DATA = 64

#socket () function

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as mySocket:
    #connect
    mySocket.connect((IP,PORT))
    data = struct.pack('!d', 55.5)  
    mySocket.sendall(data)
    data = mySocket.recv(AMT_DATA)
    outData=struct.unpack('!d', data)
print("Received data from server: ", outData)
