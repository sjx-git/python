def file():
    old_name = input('输入你要打开的文件名称：')
    f = open('hi.txt','r+')
    content = f.read()
    tmp = old_name.partition('.')
    new_name = tmp[0] +'[复件]'+tmp[1]+tmp[2]
    f1 = open(new_name,'w+')
    f1.write(content)
    f1.close()
    f.close()


file()