'''迭代器：一个可以记住遍历位置的对象，也叫迭代对象
可用来for循环的对象，统称为迭代对象，比如：列表/字典/集合/元祖/字符串/yield的生成器

'''

'''判断是否可以迭代'''
from  collections import Iterable
print(isinstance([],Iterable))#true

'''迭代器:可以用next（）函数调用并不断返回下一个值的对象称为迭代器：iterator'''

from collections import Iterator

print(isinstance([],Iterator))#False，因为都不是迭代对象
print(isinstance((x for x in range(3)),Iterator))#true 除了生成器都是false
print(isinstance(iter([]),Iterator))#可以用iter函数 转换成迭代对象 就可以变成迭代器


