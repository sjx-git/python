def digui(num):
    if num>1:
        return num*digui(num-1)
    else:
        return num
res = digui(4)
print(res)