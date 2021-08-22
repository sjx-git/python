'''
框架
    1.创建testfixture的
        setupClass：做一些预执行准备，比如设置url链接啊 数据准备啊等；用classmethod装饰
        teardownClass：最后收尾工作：用classmethod装饰
        setup：每一条用例执行前的打印工作
        teardown：每一条用例执行后的打印操作
    2.创建测试用例
        先要导入testfixture方法，以便可以继承其中的一些方法和属性
        每一条用例都用test开头了，并且记得assertEqual断言
    3.创建测试套件
        目前用的有：unittest.defaultTestLoader.discover(里边写路径还有，具体的test开头的py脚本)
        并return套件引用
    4.创建main执行程序
        首先要导入测试套件
        目前用HTMlTestRunner(
            stream =测试报告名称(需要实现写明测试报告的存放路径以及名称)，title=测试报告title，description=描述，verbosity =报告明细度，1是默认。0是不输出具体每条用例执行结果，2是最详细，
        )执行.run方法(测试套件模块.测试套件了类名().测试套件方法())
    5.发送邮件

'''

