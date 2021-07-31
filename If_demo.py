'''  if的几种写法'''
def e():
    a = -1
    b = 0 if a<0 else 2# 格式是：  if成立的情况下的操作  if的条件  else即不成立的情况下的操作
    print(b)
e()

c = 3
if c>0:
    print('c > 0')
elif c == 0:
    print('c = 0')
else:
    print('c < 0')
