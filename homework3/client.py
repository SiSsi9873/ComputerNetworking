# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:19:57 2019

@author: SIQILI
"""

from socket import *
 
'''
    客户端
'''

tcpClientSocket = socket(AF_INET,SOCK_STREAM)
 

serAddr = ("127.0.0.1",8080)
tcpClientSocket.connect(serAddr)
 
while True:

    sendData = input("请输入内容:")
    if len(sendData) > 0:
        tcpClientSocket.send(sendData.encode('utf8'))
    else:
        break
 

    recv = tcpClientSocket.recv(1024)
    print("127.0.0.1:\n" + recv.decode('utf8'))

socket.close()