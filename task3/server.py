#!/usr/bin/env python3

import socket
import struct
IP = "127.0.0.1" #loopback
PORT = 8091   #non-privileged ports > 1023
AMT_DATA = 1024

#socket created socket()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as myServerSocket:
    #bind the socket with proper:IP and a port bind()
    myServerSocket.bind((IP,PORT)) #bind done
    
    #listening socket listen() limiting it to 2 as there are only 2 clients
    myServerSocket.listen(2)
    tmpfloat = 0
    
    while True: 
        #blocking mode accfept()
        clientConn, clientAddr = myServerSocket.accept()   
        receivedDataFromClient = clientConn.recv(AMT_DATA)
        var1 = struct.unpack('!d', receivedDataFromClient)[0]
      
        if(int(var1)==55):
          data = struct.pack('!d', pow(tmpfloat,1.5))
          clientConn.send((data))
          clientConn.close()
          break;           
        else:
          tmpfloat = struct.unpack('!d', receivedDataFromClient)[0]
          clientConn.close()
          
