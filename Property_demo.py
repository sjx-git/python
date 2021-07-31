class Property_demo(object):
    '''使用装饰器 property  可以在实例对象后，直接自动调用 get和set方法 不需要人工判断'''

    def __init__(self):
        self.num = None

    @property
    def number_test(self):
        return self.num

    @number_test.setter
    def number_test(self, num):
        self.num = num


if __name__ == '__main__':
    t = Property_demo()
    t.num = 1000
    print(t.num)
