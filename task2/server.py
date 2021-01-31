#!/usr/bin/env python3

import socket
IP = "127.0.0.1" #loopback
PORT = 8090   #non-privileged ports > 1023
AMT_DATA = 1024

#socket created socket()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as myServerSocket:
    #bind the socket with proper:IP and a port bind()
    myServerSocket.bind((IP,PORT)) #bind done
    
    #listening socket listen() limiting it to 2 as there are only 2 clients
    myServerSocket.listen(2)
    tmpint = 0
    while True: 
        #blocking mode accfept()
        clientConn, clientAddr = myServerSocket.accept()   
      #  print("Accepted a connection from client: ",clientAddr)
        receivedDataFromClient = clientConn.recv(AMT_DATA)
      #   print("Received data from client: ",receivedDataFromClient)
        if(len(receivedDataFromClient.decode())==1):
            tmpint=int(receivedDataFromClient.decode('utf8'))
            clientConn.close()
        else :
            clientConn.send(str(tmpint+1).encode('utf8'))
            clientConn.close()
            break;
#send recev data
