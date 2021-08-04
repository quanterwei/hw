import threading
from threading import Lock,Thread
import time,os

def run(n):
    print('task',n)
    time.sleep(1)
    print('2s',n)
    time.sleep(1)
    print('1s',n)
    time.sleep(1)
    print('0s',n)
    time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=('t1',))     # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    t2 = threading.Thread(target=run,args=('t2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3=threading.Thread(target=run,args=('t3',))
    t3.start()

