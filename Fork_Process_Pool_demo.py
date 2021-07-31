''' 多进程 fork--仅能在linux上运行，因此仅作为了解
父进程结束后，不会等着子进程一起结束，各自结束自己的

当有多个fock的时候  进程数是2的n次方
'''

'''import os

num = 0#变量在多进程中 不共享 各自用自己的
tem = os.fork()
#fork默认会生成两个进程，主进程是>0的，子进程是=0的
if tem == 0:
    num += 1
    print('子进程---%d'%num)

else:
    print('主线程---%d'%num)'''


'''  进程的创建--第一种方法：
与fork不一样的是，主进程会等待子进程结束后 主进程才结束
process 可以在windows和linux中运行，（数量少的时候可以用这个，进程数量多的时候用进程池pool）
    参数：
    target：表示这个进程实例所调用对象；
    args：表示调用对象的位置参数元组；
    kwargs：表示调用对象的关键字参数字典；
    name：为当前进程实例的别名；
    group：大多数情况下用不到；
    常用方法：
    is_alive()：判断进程实例是否还在执行；
    join([timeout])：是否等待进程实例执行结束，或等待多少秒；
    start()：启动进程实例（创建子进程）；
    run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；
    terminate()：不管任务是否完成，立即终止；
'''
# from multiprocessing import Process
# def test():
#    for i in range(5):
#         print(1)
#
#
# if __name__ == '__main__':#此处如果不用if main，会报错
#
#     p = Process(target=test)#指定一个要执行的方法也就是test方法
#     p.start()#主进程会等待子进程结束后再结束，有区别与fork
#     p.join(1)#堵塞，等待子进程结束后 ，主进程才继续执行；1是等待时间 可写可不写
#     print('等待子进程结束后 ，主进程才打印这个')


'''进程的创建--第二种方法
进程的创建-Process子类
创建新的进程还能够使用类的方式，可以自定义一个类，继承Process类，每次实例化这个类的时候，就等同于实例化一个进程对象，请看下面的实例：

from multiprocessing import Process
import time
import os

#继承Process类
class Process_Class(Process):
    #因为Process类本身也有__init__方法，这个子类相当于重写了这个方法，
    #但这样就会带来一个问题，我们并没有完全的初始化一个Process类，所以就不能使用从这个类继承的一些方法和属性，
    #最好的方法就是将继承类本身传递给Process.__init__方法，完成这些初始化操作
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    #重写了Process类的run()方法
    def run(self):
        print("子进程(%s) 开始执行，父进程为（%s）"%(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))

if __name__=="__main__":
    t_start = time.time()
    print("当前程序进程(%s)"%os.getpid())
    p1 = Process_Class(2)
    #对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
    p1.start()#因为重写了run方法，所以这里会自动调用
    p1.join()
    t_stop = time.time()
    print("(%s)执行结束，耗时%0.2f"%(os.getpid(),t_stop-t_start)'''

'''创建进程更简单的方法 进程池pool  特点就是：默认不会等待子进程结束 所以用jion作为等待，并且  一般都是子进程做事情 主进程只负责等待不做任何事情

当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。

初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行，请看下面的实例：
'''
from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

po=Pool(3) #定义一个进程池，最大进程数3
for i in range(0,10):
    #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    #每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker,(i,))#非堵塞模式运行   注意此处要用元祖，元祖是需要在后面加一个，的
    #po.apply(worker,(i,))几乎不用 #堵塞方式运行 

print("----start----")
po.close() #关闭进程池，关闭后po不再接收新的请求
po.join() #等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
