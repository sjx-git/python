''''
不带参数的装饰器
对有参数，有返回值的函数，进行装饰即，做一个 通用装饰器
1.要注意在装饰器中，传入对应的形参，可以用不定长参数代替
2.在原来的函数中，该怎么调用还是怎么调用
3.装饰器执行顺序：先装饰，而不是等到执行的时候才进行装饰
'''

'''通用装饰器'''
import functools
def A(func):
    @functools.wraps(func)#如果不加此方法，再用help查看B的说明时，会打印装饰器A的说明
    def A(*args,**kwargs):
        '函数A的说明'
        print('A装饰器')
        return func(*args,**kwargs)#有返回值的时候，记得最后要讲返回的数据给 return
    return A
@A# 等价于 B=A(B)
def B(a,b,c):
    '函数B的说明'
    return ('B的函数a=%d,b=%d,c=%d'%(a,b,c))
print(B(11,22,33))

print('-----------------华丽的分割线----------------------')

'''带有参数的装饰器
1.只需要在闭包的外层再加一个闭包就可以，最外层函数记得需要加个 形参'''
def AAA(temp):
    def A(func):
        def A_A(*args,**kwargs):
            print('A装饰器---%s'%temp)
            return func(*args,**kwargs)#有返回值的时候，记得最后要讲返回的数据给 return
        return A_A
    return A
@AAA('你瞅啥')# 等价于 先自动调用AAA，然后呢将返回值 A返回来，也就变成了  @A  这样子就是我们熟悉的装饰器了
def B(a,b,c):
    return ('B的函数a=%d,b=%d,c=%d'%(a,b,c))
print(B(11,22,33))


'''
今天的作业，装饰器实现单例
1.声明一个装饰器，装饰器内部作用域声明一个变量，用来存实例化后的对象
2.装饰器调用时，判断内部声明的变量中是否已有该类的实例化对象，如果有，直接返回对象，如果没有，则实例化、储存，并返回

'''
def task_demo(func):

    class Task(object):
        __instance = None
        __res = False

        def __new__(cls, *args, **kwargs):
            if cls.__instance == None:
                cls.__instance = object.__new__(cls)
                return cls.__instance
            else:
                return cls.__instance

        def __init__(self,name):

            if self.__res == False:
                self.name = name
                self.__res = True
    return Task


@task_demo
class Temp(object):
    def __init__(self,name):
        self.name = name


dog = Temp('汤姆')
print(dog.name)
dog1 = Temp('啸天犬')
print(dog1.name)
if id(dog) == id(dog1):
    print('对象单例设置成功，dog对象的id地址是：%d，dog1对象的id地址是：%d'%(id(dog),id(dog1)))
else:
    print('对象单例设置失败')