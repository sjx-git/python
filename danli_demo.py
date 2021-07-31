'''单例的创建'''


class OnlyOne(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


a = OnlyOne()
b = OnlyOne()
if id(a) == id(b):
    print('单例设置成功，a对象的id地址是：%d，b对象的id地址是：%d'%(id(a),id(b)))
else:
    print('单例设置失败')

''' 只初始化一次对象 也就是说不论是哪儿个对象传的值  只会在第一次进行初始化，
                  也就意味着后续的所有的对象的实参都不再生效，return的都是第一次传的那个实参数'''

class Only(object):
    __instance = None
    __temp = False
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if self.__temp == False:
            self.name = name
            self.__temp = True



A = Only('旺财')
print(A.name)#旺财
B = Only('汤姆')

print(B.name)#旺财
if id(A) == id(B):
    print('对象单例设置成功，a对象的id地址是：%d，b对象的id地址是：%d'%(id(a),id(b)))
else:
    print('对象单例设置失败')