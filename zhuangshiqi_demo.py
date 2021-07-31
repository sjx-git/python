import random


def WW(log):
    def w1(func):
        def f1(*args,**kwargs):
            print(log)
            return func(*args,**kwargs)
        return f1
    return w1
@WW('日志')
def test(a,b):
    return (a+b)

c = test(1,2)
print(c)

