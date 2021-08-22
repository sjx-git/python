"""Test Fixture
用于测试环境的准备和恢复还原, 一般用到下面几个函数。
setUp()：准备环境，执行每个测试用例的前置条件
tearDown()：环境还原，执行每个测试用例的后置条件
setUpClass()：必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次
tearDownClass()：必须使用@classmethod装饰器，所有case运行完后只运行一次"""