def num():
    '''  打印一到一百 第一种方法
   i =1
    while i<=100:
        print(i)
        i += 1
'''
    '''打印一到一百 第二种方法
    for i in (range(1,101)):
     print(i)'''


    '''打印一到一百 的偶数 第一种方式
    i = 0
    while i<=100:
        if i%2 == 0:
            print(i)
        i += 1'''

    # 打印一到一百 的偶数 第二种方式
    i =0
    while i<=100:
        i +=1
        if i%2!=0:
            continue
        print(i)


num()