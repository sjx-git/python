'''python既是面对过程也是面向对象的语言；   面向对象的三个基础要素：封装/继承/多态'''
'继承的方式  单继承和多继承（A，B）'
'1.A是父类--动物  B是子类--狗   c是基类--哮天犬'
class A(object):
    pass
class B(A):
    def bark(self):
        print('汪汪叫')
'''class C(B):  # C 有用A、B的所有属性和功能
    pass'''

'重写方式'
class C(B):
    def bark(self):  # 重写父类的方法
        print('狂叫')
        '调用父类的方法 第一种'
        #B.bark('self')
        '调用父类的方法 第二种 建议使用这种'
        #super().bark()
c = C()
#c.bark()
b = B()
class F():
    def bark(self):
        print('叫')
class D(B,F):#多继承
    '''def bark(self):
        print('叫')'''
'可以用__mro__ 查看 决定着调用父类时的顺序  是由C3算法得来的 这个算法不需要研究C语言写的'
print(D.__mro__)

'多态  1.当用一个函数，写好了调用一个方法，这个方法在父类和子类中都有一个相同的，设计好后，本身这个函数是不知道该调用哪儿个类的方法' \
'只能在 传入了某个类之后，才能知道调用这个类中的方法     这就是多态；'
def duotai(temp):
    temp.bark()
duotai(c)
duotai(b)

'私有方法和私有属性，' \
'1.在当前类也可以叫父类中，私有方法和私有属性 可以通过另一个公有的方法 进行调用使用' \
'2.在子类中，虽然即继承了父类，但父类里边的私有方法和私有属性 不可以直接调用；' \
'                           但是，可以通过父类A中的公有方法中先去调用A的私有方法和私有属性，进行间接的调用'
class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2
    def __Asiyou(self):
        return 'A的私有方法'
    def Jianjie(self):
        return self.__num2,self.__Asiyou()
class B(A):
    def B1(self):
        print('可以调用父类A的公有属性：%s'%self.num1)
    def B2(self):
        print('不可以调用父类A的私有属性和私有方法：%s'%self.__num2,self.__Asiyou())
    def B3(self):
        print('间接调用父类A的私有属性和私有方法：%s,%s'%self.Jianjie())

#B().B1()
#B().B2() 不能直接调用 会把错
B().B3()#可以通过调用A中共有方法，间接调用A的私有方法和私有属性

