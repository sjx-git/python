'''set集合{}
1.可去重
2.举例：A为上个月 来访用户列表   B为这个月来访用户列表  可查看他们的交并差集'''
a = 'abcdef'
A = set(a)
b = 'ackgldf'
B = set(b)

print(A&B)#交集 AB都有的部分
print(A|B)#并集 AB合并后且无重复的部分
print(A^B)#对称差集 A和B 除交集外的部分
print(A-B)#差集 以A为标准，查看B中没有的部分 类似左连接 非查看所有不相同的部分 只需要看A有B没有的部分