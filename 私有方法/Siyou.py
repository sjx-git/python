'''  私有方法'''

class Siyou():
    def __siyou(self):#私有方法
        print('发送短信ing')
    def siyou_demo(self,money):#共有方法
        if money>0:
            self.__siyou()
        else:
            print('余额不足')
if __name__ == '__main__':
    pass
    #Siyou().siyou_demo(-1)
    #Siyou().__siyou()  类的私有方法 不允许调用，但可以在实例中调用

''' property 将方法进行简单的封装  已完成私有方法的和私有属性的调用 '''

'''   第一种'''

class Money():
    def __init__(self):
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money1):
        self.__money = money1

T = Money()
T.money = 200
print(T.money)


'''
#第二种
class Money1():
    def __init__(self):
        self.__money = 0

    def getData(self):
        return self.__money

    def setData(self, money):
        self.__money = money
    money1 = property(getData, setData)#进行简单的封装
t = Money1()
t.money = 100#相当于 t.setData(100)
print(t.money)#相当于 t.getData()
'''