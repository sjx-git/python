''' 过滤
结构：filter（表达式：判断--返回true的元素，可迭代对象）
'''
for te in filter(lambda x:x%2,[1,2,3,4]):
    print(te)
''' 如果第一个参数是false 等同于 disable 那么就意味着 不再过滤 全部取出'''
for te in filter(None,'hi'):
    print(te)