import unittest,os


class TestSuites():
    """完成测试用例套件的组装"""
    def test_sutes(self):
        # 拼接处测试用例的绝对路径所在:os.path.join(os.path.dirname(os.path.abspath(__file__)),"../test_case")
        # 获取当前脚本的路径：os.path.abspath(__file__)
        # 获取当前脚本所在路径的 文件夹 也就是脚本的上一层：os.path.dirname(os.path.abspath(__file__)，dirname方法中，必须要传入一个参数，所以干脆就传入当前脚本的路径就好了

        # 创建测试套件对象 并获取所有测试用例
        testSute = unittest.defaultTestLoader.discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case'),
            pattern='test*.py')
        return testSute

if __name__ == "__main__":
    TestSuites().test_sutes()