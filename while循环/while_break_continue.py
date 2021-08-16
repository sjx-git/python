'''  break  退出当前while循环，此处遵循就近原则的最近的那个while  其他while不受影响
      实例：打印20个偶数'''

i = 1
num = 0
while i<=100:
    if i%2 == 0:#取商：a//b  取余：a%b   除以：a/b
        #print(i)
        num += 1
        print("第%d个的偶数是：%d"%(num,i))
    if num == 20:
        break
    i +=1

print('='*100)

'''  continue  跳出当前while循环，在此后面的部分都不在执行
      实例：打印20个偶数'''
j = 1
num1 = 0
while j<=100:
    j += 1
    if j%2 != 0:#取商：a//b  取余：a%b   除以：a/b
        continue
    else:
        num1 += 1
        print("第%d个的偶数是：%d"%(num1,j))
    if num1 == 20:
        break

