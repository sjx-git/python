'''
注意：
    如果在命令行或者Jenkins中，运行测试脚本，经常会遇到import找不到包的错误，需要在python中的site-package中新建一个xxx.pth的文件，里边的内容就写到找不到包的上一级，目录就好
        比如：
            ModuleNotFoundError: No module named 'GUI自动化'
            pth内容就写：/Users/sunjiaxing/sjx/python

完成ui自动化的demo
前提：
    1.安装selenium
        pip3 install selenium( selenium-3.141.0)
        查看 selenium 版本信息
            pip3 show selenium
    2.下载浏览器驱动，并将驱动存放到指定路径/usr/local/bin中，以便可以让程序能找到
        要注意 浏览器和驱动的对应关系
        IE：

        Firefox：

        Chrome：
            http://chromedriver.storage.googleapis.com/index.html
步骤
1.完成测试固件的框架搭建
    初始化openWebdriver类，达到启动浏览器，并做一些预处理的目的
2.写测试用例
3.完成测试用例合集
4.完成main启动类
5.设置报告路径

unittest case的运行流程：
    TestFixture指的是环境准备和恢复
    unittest中最核心的部分是：TestFixture、TestCase、TestSuite、TestRunner、TestResult

    写好一个完整的TestCase
    多个TestCase 由TestLoder被加载到TestSuite里面, TestSuite也可以嵌套TestSuite
    由TextTestRunner来执行TestSuite，测试的结果保存在TextTestResult中


数据和代码分离之读取Excel表 用到xlrd
xlrd在读取时，会将int变为float，但在ddt中会报错，解决办法就是在excel中，在数字那一栏加一个英文'  就可以了
'''


