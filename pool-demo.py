import random
import time
from multiprocessing import Pool
from multiprocessing import Manager

def write(q):
    f = 1
    for i in range(random.randint(1,3)):
        q.put(i)
        print('put的第%d次推送的内容为：%s'%(f,i))
        time.sleep(0.5)
        f += 1

def read(q):
    u = 1
    '''
    while True:
        if not q.empty():
            print('第%d次读取的内容为：%d'%(u,q.get()))
        else:
            break'''
    if not q.empty():
        for i in range(q.qsize()):
            print('第%d次读取的内容为：%d'%(u,q.get()))
            u += 1


if __name__ == '__main__':

    q = Manager().Queue()
    p = Pool()
    p.apply(write, (q,))
    p.apply(read, (q,))
    p.close()
    p.join()