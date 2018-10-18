
import queue,time
from  multiprocessing import Process,Pipe,Manager


# def foo(q):
#     print("son",id(q))
#     q.put(123)
#     q.put("ass")
#
#
# if __name__ == '__main__':
#     # q = queue.Queue() 线程队列
#     q=multiprocessing.Queue()
#     p = multiprocessing.Process(target=foo,args=(q,))
#
#     p.start()
#     # p.join()
#     print(q.get())
#     print(q.get())
#     print("main",id(q))

# def f(conn):
#     conn.send("123")
#     print(conn.recv())
#     conn.close()
#     print("id2",id(conn))
# if __name__ == '__main__':
#     parent_conn,child_conn=Pipe()
#     print("id1",id(child_conn))
#     p=Process(target=f,args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     parent_conn.send("hello")
#     p.join()

def f(d,l,n):
    d[n]='1'
    d['2']=2
    d[0.25]=None
    l.append(n)
    print("son",id(d),id(l))

if __name__ == '__main__':
    with Manager() as manager:
        d=manager.dict()
        l=manager.list(range(5))
        print("main",id(d),id(l))
        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(d,l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)

