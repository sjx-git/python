'''
Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。
介绍is 和 == 一些注意点

== 用来比较判断两个对象的value(值)是否相等
is 判断的是对象间的唯一身份标识，也就是id是否相同

如果是int或者str类型的对象，值相等的对象(python一切皆对象)，id也相等，所以如果==为True的话，使用is判断也是True；
虽然tuple，list，dict，或set的值相等，使用==返回的True，但是他们的id是不同的，使用is返回的是False

'''
''' 只要是在-5~256之间的整形，也叫小整数对象池，python不会给变量初始化新的内存空间，但是一旦超出256，则会分配新的空间。
    但是！！！上边这个说法 没有验证成功，现在的现象是，只要对比 id is id  结果都是false！  
    目前的理解，只能用id超过了256数值来解释了 为撒是false--已经明确了 就是因为超出了小整数对象池的范围导致的
 '''
a = 2
b = 2
print(a == b)#True
print(a is b)#True

c = a
print(a == c)#True
print(a is c)#True

print(id(a) == id(c))#True
print(id(a) == id(b))#True

print(id(a) is id(b))#False
print(id(a) is id(c))#False
print(id(a))
