"""Test Case
参数verbosity可以控制错误报告的详细程度：默认为1。0，表示不输出每一个用例的执行结果；2表示详细的执行报告结果。
    Verbosity=1情况下成功是 .，失败是 F，出错是 E，跳过是 S
    Verbosity=2情况下会打印测试的注释
测试的执行跟方法的顺序没有关系, 默认按字母顺序
    每个测试方法均以 test 开头
数据驱动：
    @ddt.ddt作为装饰器要放在测试类上
    @ddt.data(*data)和@ddt.unpack作为装饰器，要放在具体的测试用例方法上
        @ddt.data(*data)    data 可以是单个值，列表，字典或者元祖
        @ddt.unpack()   data只能是列表或者元祖，一定要注意！！！

"""