import  random

def caiquan():
    num = int(input('请输入 序号 1剪刀 2布 3 锤头:'))
    res= random.randint(1,3)
    if (num == 1 and res == 1)  or (num == 2 and res == 2) or(num == 3 and res==3) :
        print('平局')
    elif (num == 2 and res == 3)  or (num ==1 and res== 2)  or (num == 3 and res ==1):
        print('你赢了')
    elif (num == 3 and res == 2) or (num == 1 and res == 3) or (num == 2 and res == 1) :
        print('你输了')
    else:
        print('输入错误',res)




while True:
    caiquan()