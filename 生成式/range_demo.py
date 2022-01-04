'''  range 和切片一样的操作'''

a = []
for i in range(1,10,2):#同样可以支持跳步
    a.append(i)
print(a)

'''  列表生成式'''
b = [i for i in range(1,20)]# i是谁就打印谁，如果是个数字 那么就会一直打印这个数字；后面的for 只控制循环次数
print(b)

'''  加if'''
b = [i for i in range(1,20) if i%2 == 0]
print(b)

''' 嵌套生成式'''
b = [(i,j,q) for i in range(2) for j in range(3) for q in range(2)]
print(b)