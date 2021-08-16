'''  异常的捕获及处理   可以自己自定一个一个异常 用raise 抛出'''

def yichang():
    try:
        '''open('xxx.txt')
        print(name)
        print(1/0)'''

    except (NameError,SyntaxError):#在捕获异常时，python2中可以不加括号，3必须要加括号
        print('需要先指明 异常的具体名称是什么在打印出，出现异常')
    #except Exception:
        #print('无论异常是什么 都会捕获到，不用和上面一样 需要写明异常的名字是什么')
    except Exception as ret:
        print('无论异常是什么 都会捕获到，并且打印出异常的名字是什么:%s'%ret)
    else:
        print('只有当没有异常的时候才会打印出else')
    finally:
        print('无论有没有异常，都会执行finally')
yichang()

