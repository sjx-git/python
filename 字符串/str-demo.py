def str():
    str = '    ==  a  d  b  \t  hhahah         ggregerhgerh   llllllllll \t  ===   '
    '查'
    print(str.find('ha'))
    print(str.rfind('ha'))
    print(str.index('ha'))
    print(str.rindex('ha'))
    if 'd' in str:
        print('ok')
    '替换'
    print(str.replace('a','aa'))
    '大写'
    print(str.upper())
    '小写'
    print(str.lower())
    '去前空格  后空格  所有空格'
    print(str.lstrip())
    print(str.rstrip())
    print(str.strip())

    print('切割后，关键字不存在')
    print(' '.join(str.split()))
    print(' '.join(str.split('\n')))
    print(' '.join(str.split('\t')))
    print(' '.join(str.rsplit('\t')))
    print('左对齐，右对齐，中间对齐')
    print(str.ljust(100))
    print(str.rjust(100))
    print(str.center(100))

    print('分割后，关键词存在 一分为三 ')
    print(str.partition('b'))
    print(str.rpartition('b'))

    a = '12'
    print('是否是数字。字母或者字母数据组合')
    print(a.isalpha())
    print(a.isdigit())
    print(a.isalnum())
    '首字母大写'
    print(str.capitalize())
    '所有单词首字母大写'
    print(str.title())



















str()