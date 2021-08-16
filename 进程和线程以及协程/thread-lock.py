'''
线程和互斥锁
'''

'''#第一种方法，在线程共享一个全局变量时，会因为调度算法的问题，导致，最后的结果不正确--本应该是两万
from threading import Thread
num = 0
def test1():
    for i in range(10000):
        global num
        num += 1
        print(num)
def test2():
    for i in range(10000):
        global num
        num += 1
        print(num)
if __name__ == '__main__':
    thred1 = Thread(target=test1)
    thred1.start()
    thred2 = Thread(target=test2)
    thred2.start()'''

'''#为了解决上班的问题，第一种办法
from threading import Thread
num = 0
tmp = 0
def test1():
    global tmp
    if tmp == 0:
        for i in range(10000):
            global num
            num += 1
        print(num)

        tmp = 1
def test2():
    if tmp != 0:
        for i in range(10000):
            global num
            num += 1
            print(num)
if __name__ == '__main__':
    thred1 = Thread(target=test1)
    thred1.start()
    thred2 = Thread(target=test2)
    thred2.start()'''

#为了解决上班的问题，第二种办法,互斥锁
from threading import Thread,Lock
num = 0
def test1():
    lock.acquire()#上锁
    for i in range(10000):
        global num
        num += 1
    print(num)
    lock.release()#解锁

def test2():
    lock.acquire()
    for i in range(10000):
        global num
        num += 1
        print(num)
    lock.release()
if __name__ == '__main__':
    lock = Lock()
    thred1 = Thread(target=test1)
    thred1.start()
    thred2 = Thread(target=test2)
    thred2.start()

