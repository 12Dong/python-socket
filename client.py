#made by 12Dong
import socket
import threading

host = "127.0.0.1"
port = 9999
addr = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
true = True

def rec(s):
    global true
    while true:
        t = s.recv(1024).decode('utf-8')
        if t == 'Exit':
            true = False
        print(t)

trd = threading.Thread(target=rec,args=(s,))
trd.start()

while true:
    t = input()
    s.send(t.encode('utf-8'))
    if t == "Exit":
        true = False
s.close()

#10/4 更新基本定型