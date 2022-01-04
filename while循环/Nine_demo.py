'while嵌套实例   99乘法表  正三角'
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d * %d = %d'%(j,i,j*i),end='\t')
        j += 1
    print('')
    i += 1

'''   倒三角'''
print('*'*150)
i = 9
while i>=1:
    j = 1
    while j<=i:
        print('%d * %d = %d'%(j,i,j*i),end='\t')
        j += 1
    print('')
    i -= 1
