# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:14:16 2019

@author: SIQILI
"""
from socket import *

tcpSerSocket = socket(AF_INET,SOCK_STREAM)

address = ('',8080)
tcpSerSocket.bind(address)
 
tcpSerSocket.listen(5)
 
while True:
    
    newSocket,clientSocket = tcpSerSocket.accept()
   
    while True:
     
        recvData = newSocket.recv(1024)
 
        if len(recvData) > 0:
            print("192.168.1.105:\n"+recvData.decode('utf8'))
        else:
            break
        
        sendData = input("127.0.0.1:\n")
        newSocket.send(sendData.encode('utf8'))
newSocket.close()
