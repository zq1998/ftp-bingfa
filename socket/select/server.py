

import socket
import select,time
#
# sk=socket.socket()
# sk.bind(("127.0.0.1",8001))
# sk.listen(5)
#
# while True:
#     r,w,e=select.select([sk,],[],[],5)
#     for i in r:
#         conn,add=i.accept()
#         print(conn)
#         print(add)
#
#     print(">>>>>")
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',6667))
sk.listen(5)
sk.setblocking(False)
while True:
    try:
        print ('waiting client connection .......')
        connection,address = sk.accept()   # 进程主动轮询
        print("+++",address)
        client_messge = connection.recv(1024)
        print(str(client_messge,'utf8'))
        connection.close()
    except Exception as e:
        print (e)
        time.sleep(4)