'递归的用法'
'4! 4的阶乘  4*3*2*1'
i =1
res =1
while i<5:
    res = res *i
    i +=1
print(res)

'递归'
def recursion(num):
    if num>1:
        return num *recursion(num -1)
    else:
        return num
print(recursion(4))