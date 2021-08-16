'1.缺省参数：形参有默认值，可不传默认数据，但不能放在第一位 '
def test(a,b=2):
    pass
test(1)
'2.形参有默认值，想改变默认值,但是要改值 那么实参的名字一定要和形参一致'
def test1(a,b=2):
    pass
test(1,b=3)#命名参数
'3.实参传入的位置写错了，可用形参一致的名字标识 即只需要指定参数的名字和值 就可以做到想要的效果'
def test2(a,b=2):
    pass
test(b = 3,a=1)


'默认形参取33；不定长参数（必须放在最后） *args 保存实参中的44,55,66,A的内容数据（先拆包）       最后以元组展示；'
'                                  **kwargs 保存77,88,B的数据（先拆包）          最后以字典展示'
A =(1,2)
B = {'name':'liming','sex':'nan'}
def test3(a,b,c=33,*args,**kwargs):
    '取值args,以加法举例'
    result= a + b
    for temp in args:
        result += temp
    print(result)
    print(args)
    print(kwargs)
test3(11,22,33,44,55,66,age=88,id=77,*A,**B )#如果此处不加*和** 那么所有的值都会被当作一个整体放入，*args中


'''给程序传参 sys.argv'''
import  sys
def aaa(a):
    sys.argv.append(a)
    print('你好%s'%sys.argv[1])
aaa(1)
