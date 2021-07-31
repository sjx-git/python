'''  映射函数：我给你个东西 你给我个结果
结构：map(一个函数的引用/匿名函数也行，可迭代对象)
'''
'''将列表中的元素 相乘   单个参数'''
for tep in map(lambda x:x*x,[1,2,3]):
    print(tep)

'''将列表中的元素 相乘   两个参数'''
for tep in map(lambda x,y:x*y,[1,2,3],[5,6,7]):
    print(tep)