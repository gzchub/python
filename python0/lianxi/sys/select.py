#!/usr/bin/python
#coding=utf-8

HOST = '192.168.0.104'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.bind(ADDR)
sockfd.listen(5)

inputs = [sockfd]

while True:
    rs,wa,es = select(inputs,[].[])
    for r in rs:
        if r is sockfd:
            connfd,adddr = sockfd.accept()
            print("connected from :",addr)
            inputs.append(connfd)
        else:
            try:
                data = r.recv(BUFSIZE).decode()
                disconnect = not data
            except socket.error:
                disconnect = True
            if disconnect:
                print (r.getpeername(),'daisconnected')
                inputs.remove(r)
                r.close()
            else:
                r.send(('[%s] :%s'%(ctime(),data)).encode())
