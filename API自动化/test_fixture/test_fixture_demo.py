import unittest


class ApiUnittest(unittest.TestCase):
    """完成测试固件的框架搭建"""
    @classmethod
    def setUpClass(cls):
        print("执行测试前的准备工作即将开始进行接口相关的配置")
        cls.url = 'http://apis.juhe.cn/simpleWeather/life'
        cls.key = '959e4fc1aa5787e67ae143901b2d2673'
        cls.a = [1]

    def setUp(self):
        print("开始执行 第%d条 测试用例" % len(self.a))

    def tearDown(self):
        print("执行完成 第%d条 测试用例" % len(self.a))
        self.a.append(1)

    @classmethod
    def tearDownClass(cls):
        print('执行测试结束的收尾工作，即将关闭接口相关配置')


if __name__ == "__main__":
    unittest.main()
