'匿名函数的使用'
'将匿名函数作为参数传入函数中'
def test(a,b,func):
    res = func(a,b)
    return res
result = test(11,22,lambda x,y:x+y)
print(result)


'为了实现 可以自由输入任何表达式 都可以使之得到想要的结果，可以用input 任意输入匿名函数表达式，将匿名函数作为参数传入函数中' \
'但要注意，因为Python3 的input是个字符串，需要使用 eval 转换成 Python2的input对应的表达式 '
def test(a,b,func):
    res = func(a,b)
    return res
result = eval(input('请输入一个表达式：'))
re = test(11,22,result)
print(re)