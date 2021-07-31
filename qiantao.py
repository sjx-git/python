'''   while 循环嵌套'''

i = 1

while i <= 10:
    print('站起来第%d次'%i)
    a = 1
    while a <= i:
        print('转第%d个圈'%a)
        a += 1
    i += 1