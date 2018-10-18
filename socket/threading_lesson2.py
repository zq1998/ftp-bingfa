
import threading
import time
from multiprocessing import Process

# def music():
#     print("b %s"%time.ctime())
#     time.sleep(3)
#     print("s %s"%time.ctime())
#
# def game():
#     print("bb %s" % time.ctime())
#     time.sleep(5)
#     print("ss %s" % time.ctime())
# threads=[]
# t1=threading.Thread(target=music)
# t2=threading.Thread(target=game)
# threads.append(t1)
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True) #随主线程一起退
#         t.start()
# print("sfd")
class MyProcess(Process):
    def run(self):
        time.sleep(1)
        print("hello",self.name,time.ctime())
if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p=MyProcess()
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()

    print("end")
