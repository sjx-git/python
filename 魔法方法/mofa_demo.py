''' new方法 + init方法 等价于 构造方法'''

class A():
    def __new__(cls, *args, **kwargs):#cls是 A类对象
         print('第一步 自动调用new方法 来创建对象 它只负责创建对象')
         return super().__new__(cls)

    def __init__(self):
        print('第二步 自动调用是init  它只负责初始化')

    def __str__(self):
        print('第三步 自动调用是str')

    def __del__(self):
        print('最后一步 自动调用是del')

a = A()
'''  
1、调用new方法创建一个对象，传入参数cls--代表A()  然后找了一个变量C来接收new return的返回值，这个返回值就是 创建出来的对象的引用     
2、调用init方法 传入参数self 也就是C   进行初始化对象
3、返回对象的引用 给到a






'''