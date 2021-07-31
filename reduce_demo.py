'''  累加
结构：reduce（表达式，任意）
'''
from functools import reduce
'''  累加起来：默认x没有值，将1给到y，x+y的值 给到x；然后将2的值给到y，x+y的值再给到x。。。。'''
print(reduce(lambda x,y:x+y,[1,2,3]))

'''  累加起来：默认x设定为5，将1给到y，x+y的值 给到x；然后将2的值给到y，x+y的值再给到x。。。。'''
print(reduce(lambda x,y:x+y,[1,2,3],5))

'''  累加起来：默认x设定为dd，将aa给到y，x+y的值 给到x；然后将bb的值给到y，x+y的值再给到x。。。。'''
print(reduce(lambda x,y:x+y,['aa','bb','cc'],'dd'))