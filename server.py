#made by 12Dong
# -*- coding :utf-8 -*-
import socket
import threading
import sys
import time

host='localhost'
port=10000
addr = (host,port)
username = ''
clients =[]

print("Socket is creating")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(addr)
s.listen(2)
print("Socket is listening")
sock,addr = s.accept()
true = True
def rec(s,addr):
    global true
    while 1:
        try:
            print('waiting data')
            data = s.recv(1024).decode('utf-8')
            if not data or data=='Exit':
                break
            print(data)
        except:
            break
    clients.remove(sock)
    print("[%s : %s] leave"%addr[0],addr[1])
    print(clients)

trd = threading.Thread(target=rec,args=(sock,addr))
trd.start()

while true:
    t = input()
    sock.send(t.encode('utf-8'))
    if t=='Exit':
        true = False

s.close()

# #10/4 更新基本定型

#!/usr/bin/evn python
# coding:utf-8

# import socket
# import threading
#
# host = 'localhost'
# port = 9999
# username = ''
# clients = []
#
#
# def server(sock, addr):
#     while 1:
#         try:
#             print('waitting data...')
#             data = sock.recv(1024).decode('utf-8')
#             if not data:
#                 break
#             for c in clients:
#                 c.send(data)
#             print(data)
#         except:
#             break
#     clients.remove(sock)
#     sock.close()
#     print('[%s:%s] leave' % (addr[0], addr[1]))
#     print(clients)
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('Socket create')
# s.bind((host, port))
# s.listen(3)
# print('Socket is listenning...')
#
# while 1:
#     client, addr = s.accept()
#     username = client.recv(1024).decode('utf-8')
#     clients.append(client)
#     print('[%s:%s:%s] join!' % (addr[0], addr[1], username))
#     print (clients)
#
#     thread = threading.Thread(target=server, args=(client, addr))
#     thread.start()