def list():
    name = [1,2,3,'laowang','liming']
    '增'
    name.append(4)
    name.insert(3,'hh')
    name.extend(['a','d','c'])
    name.append(['j'])
    print(name)
    print('逆向')
    #a = name.reverse()
    print(name)
    print(name[::-1])



    '删'
    name.pop()
    name.remove('hh')
    del name[0]
    print(name)
    '改'
    name[1]=22
    print(name)
    '查'
    if 'laowang' in name:
        print('ok')

    b = [1,9,11,4,55,0]
    print('从小到大排序')
    b.sort()
    print(b)
    print(sorted(b))
    print('从大到小')
    print(sorted(b,reverse=1))
    b.sort(reverse=True)
    print(b)
    print('逆向')
    print(b[::-1])
    b.reverse()
    print(b)



list()