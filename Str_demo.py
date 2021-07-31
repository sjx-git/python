str = "   This is a demo for str         "
str1= ['hi','world']
str2 = 'abdeEFGH'
str3 = 'zz\nnn'
str4 = input('输入')

''' 字符串的切片    起始位置：终止位置（不包含最后一个，也就是取出-1的值）：跳步  '''
print('正向 取出全部的值：%s'%str2[0:])
print('正向 取出全部的值：%s'%str2[0:len(str2)])
print('正向 取出全部的值：%s'%str2[:])

print('正向 取出部分的值：%s'%str2[1:-1])
print('正向 取出部分的值：%s'%str2[:-1])
print('正向 取出倒数第一个的值：%s'%str2[-1:])
print('正向 取出倒数第一个的值：%s'%str2[-1])

print('倒序 取出倒数第一/二个的值：%s'%str2[-1:-3:-1])
print('倒序 取出全部的值：%s'%str2[::-1])
print('倒序 取出 隔一个的值：%s'%str2[::-2])

'''   查找 find和index的区别只在找不到的时候 index会抛出异常；find会返回-1，可以用此方法进行if 首条件的判断； '''
print('find从左查找到返回第一个字母的下标：%s'%str.find('demo'))
print('find从左查找找不到的时候返回-1：%s'%str.find('ssss'))
print('rfind从右查找到返回第一个字母的下标：%s'%str.rfind('demo'))
print('rfind从右查找找不到的时候返回-1：%s'%str.rfind('ssss'))

print('index从左查找到返回第一个字母的下标：%s'%str.index('demo'))
print('rindex从右查找到返回第一个字母的下标：%s'%str.rindex('demo'))
#print('index从左查找不到会抛出异常：%s'%str.index('ssss'))
#print('rindex从右查找不到会抛出异常：%s'%str.rindex('ssss'))

print('按下标查询：%s'%str[0])
print('统计该关键字出现的次数：%s'%str.count('a'))

'旧值，新值 替换   但因字符是不可变类型，所以不会改变原有数据;'
print('从左到右依次全部替换里边的内容：%s'%str.replace('is','xxx'))
print('从左到右 只替换一次里边的内容：%s'%str.replace('is','xxxx',1))


'''  split 可以用来分割/去除空格等字段'''
print('去除空格 \t等的字段  只保留字符，并以列表的形式展示:%s'%str.split())
print('以填写的关键字 进行分割，并以列表的形式展示：%s'%str.split(' '))
print('以\n 进行 行的分割，并以列表的形式展示：%s'%str3.splitlines())


'''  字母大写 capitalize和title '''
print('首字母大写，其他不不变：%s'%str.capitalize())
print('所有首字母大写：%s'%str.title())

''' 开头和结尾的判断 startwith 和 endwith'''
print('判断开头：%s'%str2.startswith('a'))
print('判断结尾：%s'%str2.endswith('H'))

#因变为元组后，变为了多个字符串，因此接收时需要用多个%s
print('以关键字 为中心从左开始将  左右的分割成三部分字符串，并以元组的形式展示：%s,%s,%s'%(str.partition('a')))
print('以关键字 为中心从右开始将  左右的分割成三部分字符串，并以元组的形式展示：%s,%s,%s'%(str.rpartition('a')))

print('居中显示:%s'%str.center(10))
print('靠左显示:%s'%str.ljust(10))
print('靠右显示:%s'%str.rjust(10))

print('删除 头尾的空格:%s'%str.strip())
print('删除右边空格:%s'%str.rstrip())
print('删除左边空格:%s'%str.lstrip())

print('全部小写：%s'%str.lower())
print('全部大写：%s'%str.upper())

print('判断是不是字母：%s'%str2.isalpha())
print('判断是不是数字：%s'%str4.isdigit())
print('判断是不是字母和数字都有：%s'%str2.isalnum())

print('合并：%s'%str.join(str1))

'去除全部的空格 第一种方法'
A=['我', '的', '收', '藏']
#G =' '.join(A)#此处用空格去join 有点多此一举，直接用''就可以join 以免还要用replace去替换一遍
#print(G.replace(' ',''))
G =''.join(A)
print(G)

'join()方法+split()方法，去除全部空格 第二种方法 '
a = " a \n b \t c "
b = a.split()  # 字符串只保留字符 并以列表b ['a', 'b', 'c']展示
c = "".join(b) # 使用一个空字符串合成列表内容生成新的字符串
print(c)


#字符串大小对比的实现原理是根据ASCII码进行对比，详细可见 for_demo的面试题