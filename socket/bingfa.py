import threading,time
import queue

# li=[1,2,3,4,5]
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except Exception as e:
#             print('----',a,e)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=pri, args=())
#     t1.start()
#     t2 = threading.Thread(target=pri, args=())
#     t2.start()
# q=queue.LifoQueue()
#
# q.put(34)
# q.put(56)
# q.put(12)
#
# #优先级
# q=queue.PriorityQueue()
# q.put([5,100])
# q.put([7,200])
# q.put([3,"hello"])
# q.put([4,{"name":"alex"}])
# if __name__ == '__main__':
#     while 1:
#         data = q.get()
#         print(data)
# from contextlib import contextmanager
#
#
# @contextmanager
# def make_context():
#     print('enter')
#     try:
#         yield "ok"
#     except RuntimeError as err:
#         print( 'error', err)
#     finally:
#         print('exit')
# if __name__ == '__main__':
#     with make_context() as value:
#      print(value)

# def consumer(name):
#     print("--->ready to eat baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name,new_baozi))
#         #time.sleep(1)
#
# def producer():
#
#     r = con.__next__()
#     r = con2.__next__()
#     n = 0
#     while 1:
#         time.sleep(1)
#         print("\033[32;1m[producer]\033[0m is making baozi %s and %s" %(n,n+1) )
#         con.send(n)
#         con2.send(n+1)
#
#         n +=2
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()
# from  greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# if __name__ == '__main__':
#     gr1 = greenlet(test1)
#     gr2 = greenlet(test2)
#     gr1.switch()
import gevent
import requests,time

start=time.time()

def f(url):
    print('GET: %s' % url)
    resp =requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),

])
print("cost time:",time.time()-start)





