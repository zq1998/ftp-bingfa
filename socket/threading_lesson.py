

import  threading #线程
import  time
def Hi(num):
    print("hello %d"%num)
    time.sleep(3)

if __name__ == '__main__':
    t1=threading.Thread(target=Hi,args=(10,))
    t1.start()
    t2=threading.Thread(target=Hi,args=(9,))
    t2.start()



