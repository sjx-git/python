'''  if的几种写法'''
def e():
    a = 1
    #  -->如果满足if 那么结果就是b = 0；如果不满足if也就是满足else 那么结果就是b = 2
    b = 0 if a<0 else 2
    print(b)
e()

c = 3
if c>0:
    print('c > 0')
elif c == 0:
    print('c = 0')
else:
    print('c < 0')
