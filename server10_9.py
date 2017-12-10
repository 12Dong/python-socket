import socket
import threading
import pymysql

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9999))
sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'listening ...')

mydict = dict()
mylist = list()

conn=pymysql.connect(host='localhost',user='root',passwd='HanDong85',db='nickname',port=3306)
# 创建游标
cursor = conn.cursor()

# 把whatToSay传给除了exceptNum的所有人
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass


def subThreadIn(myconnection, connNumber,cursor):
    nickname = myconnection.recv(1024).decode()

    sql = "SELECT * FROM Nickname WHERE name = '%s'" % (nickname)
    cursor.execute(sql)
    results = cursor.fetchall()
    if results is not None:
        print("Error")

    sql = """INSERT INTO Nickname(name)
             VALUES ('%s')"""%(nickname)
    cursor.execute(sql)
    conn.commit()


    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('connection', connNumber, ' has nickname :', nickname)
    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 进入聊天室】')
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            if recvedMsg:
                print(mydict[connNumber], ':', recvedMsg)
                tellOthers(connNumber, mydict[connNumber] + ' :' + recvedMsg)

        except (OSError, ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
            tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 离开聊天室】')

            # SQL 删除语句
            sql = "DELETE FROM Nickname WHERE name = '%s'" % (nickname)
            cursor.execute(sql)

            # 提交，不然无法保存新建或者修改的数据
            conn.commit()

            myconnection.close()
            return

address = ('127.0.0.1', 31500)
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.bind(address)


while True:
    connection, addr = sock.accept()
    print('Accept a new connection', connection.getsockname(), connection.fileno())

    try:
        # connection.settimeout(5)
        buf,addr = Sock.recvfrom(1024)
        if buf.decode('utf-8') == '1':
            connection.send(b'welcome to server!')

            # 为当前连接开辟一个新的线程
            mythread = threading.Thread(target=subThreadIn, args=(connection, connection.fileno(),cursor))
            mythread.setDaemon(True)
            mythread.start()

        else:
            connection.send(b'please go out!')
            connection.close()
    except:

        pass

conn.close()
#10/8 解决多人聊天问题