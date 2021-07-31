list7 = ['hi', 'world', 'are', 'you', 'ok?', '11', '22', '33', '11', '22', '33', '44']
list1 = ['Good']
list10 = [{'name':'laowang','age':9},{'name':'wangzong','age':10},{'name':'xiaoming','age':11}]
'''  添加有 append、insert、extend、直接+号四种方法；
        能添加单个字符的append、insert；
        能加列表的append、'extend、+号'''
list7.append('yes')
print('添加单个字符或者列表 在最后%s'%list7)
#list8 = list7.append(list1)
#print('添加列表 在最后，[原有列表数据，[新加的列表]：%s'%list8)

list7.insert(0, 'haha')
print('按下标添加：%s'%list7)

'只能合并列表，不能添加单个字符，[新增的列表数据，合并数据]；与append不同的添加效果'
list3 = list1 + list7
print('+号相连：%s'%list3)

list7.extend(list1)
print('extend会合并成一个列表，不同于append的【旧，【新】】：%s'%list7)


'''  删除有 pop、remove、del  这三个在删除不存在的内容时，都会报错'''
list7.pop()
print('从末尾位置开始删除：%s'%list7)

list7.remove('hi')
print('删除关键字：%s'%list7)
#list7.remove('wwwwwww')
#print('删除不存在的关键字，会报错：%s'%list7)

del list7[2]
print('按下标删除：%s'%list7)
#del  list7[100]
#print('删除不存在的下标会报错 下标越界：%s'%list7)


'''  更改 按照下标位置作更改 当下标不存在的时，同样会报错'''
list7[1] = 'no'
print('按下标更改 %s'%list7)

'''  查询 in、not in、index--不存在会报错  三种方法 '''
'查询 in  或者  not in'
if 'yes' in list7:
    print('查到了')
if 'gun' not in list7:
    print('不在这里边')
print('index（要查询的关键字）：%s'%list7.index('11'))
print('index（要查询的关键字,起始位置、终止位置）：%s'%list7.index('11',0,7))

'''排序 当列表内容元素为数字的时候很好排序，但为字典的时候就需要用到lambda函数'''

list7.sort()
print('排序 从小到大：%s'%sorted(list7))
print('排序 从小到大：%s'%list7)

list7.sort(reverse=True)
print('排序 从大到小：%s'%list7)

list7.reverse()
print('排序 颠倒位置 第一种：%s'%list7)

list7[::-1]
print('排序 颠倒位置 第二种  切片实现：%s'%list7)

'''  内容是字典的排序 '''
list10.sort(key=lambda x:x['name'])
print('按照name从小到大排序的结果：%s'%list10)

list10.sort(key=lambda x:x['name'],reverse=True)
print('按照name从大到小排序的结果：%s'%list10)


'去重 第一种'
list4 = []
for i in list7:
    if i not in list4:
        list4.append(i)
print('list4的值为：%s'%list4)

'去重 第二种'
list5 = set(list7)#set会将list转变为无序的数值{} 很像是字典但看了类型为set类型
print('list5的值为：%s'%list5)
#list6 = list(list5)
#此处可以使用eval 原本是什么样的格式就转回什么样的格式
#list6 = eval(str(list5))
list6 = list(list5)
print('list6的数值是%s'%list6)

a = [123]
b = [132]
if a == b:
    print('1')


