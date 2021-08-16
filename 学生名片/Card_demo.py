print('===============================')
print('学生信息系统')
print('1 新增 2 删除 3 查询 4.修改 5.退出 ')
print('===============================')


card = []

while True:
    num = input('请输入要查询的代号: ')
    if num.isdigit():
        if int(num) == 1:
            name = input('请输入姓名：')
            phone = int(input('请输入电话：'))
            address = input('请输入地址：')
            sex = input('请输入性别：')
            card_infor = {}
            card_infor['name'] = name
            card_infor['phone'] = phone
            card_infor['address'] = address
            card_infor['sex'] = sex
            #print(card_infor)  #for test
            card.append(card_infor)
            print(card)
        if num == 2:
            pass
        if int(num) == 3:
            num = 0
            name_id= input('请输入要查找的姓名： ')
            for temp in card:
                #print(temp[name])
                if name_id == temp['name']:
                    print('姓名\t地址\t手机号\t性别')
                    print('%s\t%s\t%d\t%s'%(temp['name'],temp['address'],temp['phone'],temp['sex']))
                    num += 1
                    break
            else:#方法二
                print('查无此人')
            '''方法一
            if num == 0:
                print('查无此人')
            '''


        if num == 4:
            name_new = input('请输入要修改的名字')
        if int(num) == 5:
            break
    elif num.isalpha():
        print('不要输入字母，请输入数字：')
    elif num.isalnum():
        print('输入不正确，请输入数字：')
    else:
        print('输入不正确，仅能输入数字：')

