'''  深拷贝和浅拷贝  栈中存放的是变量；堆中存放的是id地址和值;
        深/浅拷贝 可用于 列表/元组/字符串/字典/数字；
        深/浅拷贝 用于不可变类型时，地址和值都是一样的；比如元祖、字符串、数字
        深/浅拷贝 用于可变类型时，=浅拷贝 地址和值都是一样的；copy浅拷贝 地址不同，值相同；deepcopy深拷贝，地址和值都不同。


'''
import copy
'''浅拷贝：拷贝第一层的关系，深一点的关系不会被拷贝
        copy会新开一个栈内存，用来存放新的变量，也就会导致id 不同；
        但值仍然是指向被拷贝对象的值,因此当原变量值被修改后，新变量值也会随着更改。   
        =不会新开一个栈内存，用来存放新的变量，也就会导致id 相同；
        但值仍然是指向被拷贝对象的值,因此当原变量值被修改后，新变量值也会随着更改。 
'''

''' copy浅拷贝   也就是第一种浅拷贝  id不一样 值一样'''
a = [1]
b = [10]
c = [a,b]
e = copy.copy(c)
a.append(3)
print(c,e)
print(id(c),id(e))

''' =浅拷贝   第二种浅拷贝  id一样，值一样'''

a = [1]
b = a
a.append(3)
print(a,b)
print(id(a),id(b))


'''深拷贝：拷贝所有的层级关系
        会新开一个栈内存，用来存放新的变量，也就会导致id 不同；
        此时的值 不会 再指向被拷贝对象的值,而是再堆中新开一片内存；也因此当原变量值被修改后，新变量值 不会随着更改
'''
a1 = [1]
b1 = [10]
c1 = [a1,b1]
e1 = copy.deepcopy(c1)
a1.append(2)
print(c1,e1)
print(id(c1),id(e1))



