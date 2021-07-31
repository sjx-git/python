'key 可以是字符串、数字、元组，不可变类型都可以；但 列表、字典 可变类型 不可以做'
'因为字典在存储时，会将key进行哈希算法加密，一旦key可以发生改变，那么再也找不到value的值'
dict = {'name':'liming','age':11}

'''  新增'''
dict['sex']="男"
print('新增的结果：%s'%dict)

''' 修改  和新增几乎一样，数据存在就修改，数据不存在就新增'''
dict['sex']="女"
print('修改的结果：%s'%dict)

''' 查询'''
print('get key方式获取到value：%s'%dict.get('name'))#即便没有数据存在也不会报错
print('获取到value：%s'%dict['name'])#若key不存在就会报错，建议用get方式去获取
print('获取到所有key：%s'%dict.keys())
print('获取到所有value：%s'%dict.values())
print('获取到所有的key和value：%s'%dict.items())

'for循环遍历，并用元祖的拆包方式，取出key value的值'
for key,value in dict.items():
    print('key:%s,value:%s'%(key,value))


'''  删除'''
dict['sex']
print('删除后的结果：%s'%dict)#若不存在就会报错


