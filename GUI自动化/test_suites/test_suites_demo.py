import unittest,os


class TestSuites():
    """完成启动程序"""
    def test_sutes(self):
        # 拼接处测试用例的绝对路径所在
        # print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../test_case"))
        # 创建测试套件对象 并获取所有测试用例
        testSute = unittest.defaultTestLoader.discover(
            start_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../test_case'),
            pattern='test*.py')
        return testSute

if __name__ == "__main__":
    TestSuites().test_sutes()