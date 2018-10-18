
import time,os
from multiprocessing import  Process,Lock,Pool

# def f(l,i):
#     l.acquire()
#     print(i)
#     l.release()
#
# if __name__ == '__main__':
#     lock=Lock()
#     for num in range(10):
#         Process(target=f,args=(lock,num)).start()

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100
def Bar(arg):
    print("asss")


if __name__ == '__main__':
    pool = Pool(10)
    for i in range(100):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
    pool.close()
    pool.join() #join,close顺序固定
    print("end")

