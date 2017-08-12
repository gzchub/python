#!/usr/bin/python

from socket import *
from time import ctime
import sys

HOST  = '192.168.0.103'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.bind(ADDR)


while True:
    print "waiting for connection....."

    data,addr = sockfd.recvfrom(BUFSIZE)

    print "connected fr om :",addr

    while True:
        data = connfd.recv(BUFSIZE)
        print "data:",data
        if data[:4] == "quit":
            break
            connfd.send("[%s] : %s"%(ctime(),data))

sockfd.close()
connfd.close()
