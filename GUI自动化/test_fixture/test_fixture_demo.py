import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class WebUnittest(unittest.TestCase):
    """完成测试固件的框架搭建"""
    @classmethod
    def setUpClass(cls):
        print("执行测试前的准备工作即将开始完成chrome浏览器的启动以及配置")
        # 初始化浏览器的driver
        cls.chrome_webdriver = webdriver.Chrome(executable_path=r'/opt/homebrew/lib/python3.9/site-packages/chromedriver')
        # 将浏览器最大化
        cls.chrome_webdriver.maximize_window()
        # 修改页面加载策略
        desired_capabilities = DesiredCapabilities.CHROME
        # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        desired_capabilities["pageLoadStrategy"] = "none"
        cls.a = [1]

    def setUp(self):
        print("开始执行 第%d条 测试用例" % len(self.a))

    def tearDown(self):
        print("执行完成 第%d条 测试用例" % len(self.a))
        self.a.append(1)

    @classmethod
    def tearDownClass(cls):
        print('执行测试结束的收尾工作，即将关闭浏览器')
        cls.chrome_webdriver.quit()


if __name__ == "__main__":
    unittest.main()
