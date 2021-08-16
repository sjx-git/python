'''面试题 组成【***%%%】 第一种办法'''
a = ['*','%','*','%','*','%','*','*','%']
a.sort(reverse=True)
print(a)

'''面试题 组成【***%%%】 第二种办法'''
a = ['*','%','*','%','*','%','*','*','%']
#此处用range是因为，单纯的 len是个数字，不能遍历,此外 需要遍历的轮数是 len(a)-1
for i in range(len(a)-1):
    #每轮中，是比较了len(a) - i次
    for j in range(0,len(a)-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
for i in range(9):
    print(i)


'''给出两个列表，以a为姓，b为名进行名字的组合'''
'''第一种'''
num = 0
a = ['赵','钱','孙','李']
b = ['一','二','三','四']
for i in a:
    for j in  b:
        num += 1
        print('第%d次组合：%s'%(num,(i+j)))
'''第二种'''
g = [(i1,j1) for n1,i1 in enumerate(a) for m1,j1 in enumerate(b)]#enumrate 会返会列表的下标和对应值；可以加第二个参数，控制从哪儿个位置开始
print(g)


'''给定一个int类型的数字123，要求编写一个函数，返回1+2+3的值'''
def demo_01(A):
    tem = 0
    while A != 0:
        tem += A % 10
        A = A // 10
    return tem
print(demo_01(123))

''' 给定2个int类型的参数x和y，要求编写一个函数，用加法和减法实现x*y '''
pass

'''  交换两个数据的值  第一种 借用第三个参数'''
a = 1
b = 2
c = a
a = b
b = c
print('a的值是：%d，b的值是：%d'%(a,b))

'''  交换两个数据的值  第二种 不借用第三个参数'''
a = 1
b = 2
a = a+b
b = a-b
a = a-b
print('a的值是：%d，b的值是：%d'%(a,b))

'''  交换两个数据的值  第三种 不借用第三个参数'''
a = 1
b = 2
a,b = b,a
print('a的值是：%d，b的值是：%d'%(a,b))

'''  这个方法有可用  不过好像还有个set函数可以直接找出相同的部分，待研究'''
class key_demo:
    ''' 用来找出重构后，新的json中不正确的key和value值'''
    old_json = [{'a':2,'b':3},{'e':4,'f':5,'q':{'w':7,'r':8}}]
    new_json = [{'a':2, 'b':3},{'e':4,'F':5,'Q':{'w':7,'r':8}}]
    o3 = []
    o2 = []
    L = []

    def xx(self):
        for temp in self.old_json:
            for o,p in temp.items():
                self.o3.append(o)
        else:
            return self.o3

    def new_jsons(self):
        for temp1 in self.new_json:
            for o1,p1 in temp1.items():
                self.o2.append(o1)
        else:
            return self.o2

    def if_demos(self):
        for A in self.new_jsons():
            if A not in self.xx():
                self.L.append(A)
        else:
            print('不正确的key为：%s'%self.L)


if __name__ == '__main__':

    #key_demo.if_demos('self')   在使用类名.方法名('self')时，会导致程序无法运行,是因为我在调用类属性时，用的是self而没有用类名调用才出现的问题
    ''' f = key_demo()
     f.if_demos()#调用的时候 需要先创建对象即f 再去调用方法；'''

'''上面的程序是个错误使用调用类属性的demo，下面才是正确的写法 唯一的区别就在于类属性的调用'''
class key_demo:
    ''' 用来找出重构后，新的json中不正确的key和value值'''
    old_json = [{'a':2,'b':3},{'e':4,'f':5,'q':{'w':7,'r':8}}]
    new_json = [{'a':2, 'b':3},{'e':4,'F':5,'Q':{'w':7,'r':8}}]
    o3 = []
    o2 = []
    L = []
    def xx(self):
        for temp in key_demo.old_json:#类属性 需要用类名去调用
            for o,p in temp.items():
                key_demo.o3.append(o)
        else:
            return key_demo.o3
    def new_jsons(self):
        for temp1 in key_demo.new_json:
            for o1,p1 in temp1.items():
                key_demo.o2.append(o1)
        else:
            return key_demo.o2
    def if_demos(self):
        for A in key_demo.new_jsons('self'):
            if A not in key_demo.xx('self'):
                key_demo.L.append(A)
        else:
            print('不正确的key为：%s'%key_demo.L)
if __name__ == '__main__':
    '''这两种调用方法都可以 不过还是建议选择先去初始化对象再去调用方法名'''
    #key_demo().if_demos()#调用的时候 需要先初始化创建对象即f 再去调用方法
    key_demo.if_demos('self')