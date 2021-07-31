'''
进程与进程之间是无法直接通信的；
可以用队列(先进先出) 实现不同进程间的通信

'''
'''  queue第一种 用与process创建的进程'''

from multiprocessing import Queue
from multiprocessing import Process


def write(q):
    print(1)
    if q.full() :
        print('满了 别再put了')
    else:
        q.put('qqqq')#发送一条数据
        q.put('wwww')
        # print(q.qsize()) #mac上不支持此方法
def read(q):
    if q.empty():#如果内容为空，get会报错
        print('空的')
    else:
        print(q.get())#获取一条数据，先进先出的获取
if __name__ == '__main__':
    q = Queue(3)
    pro = Process(target=write,args=(q,))
    pro1 = Process(target=read,args=(q,))
    pro.start()
    pro.join()
    pro1.start()
    pro1.join()


