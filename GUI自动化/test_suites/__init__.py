"""
Test Suite
一般通过addTest()或者addTests()向suite中添加。case的执行顺序与添加到Suite中的顺序是一致的
        suite = unittest.TestSuite()
        #此处注意，测试用例必须要先将测试的方法放到 用test方法中，然后通过addTest：类名+（'测试用例的名称'）的方式加入到suite中
        '''第一种添加方法
        test2 = [Test_Suite('test_post'),Test_Suite('test_get')]
        suite.addTests(test2)
        return suite
        '''
        '''第二种添加方法
        suite.addTest(Test_Suite('test_post'))
        suite.addTest(Test_Suite('test_get'))
        return suite
        '''
        '''
        第三种添加方法，貌似这个牛逼 可以自动查找所有测试用例'''
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(APi_Test_Package.Auto_TestUnitest.Auto_test))
        return suite

@unittest.skip(reason)：无条件跳过单个用例或测试类，reason是跳过的原因。
@unittest.skipIf(condition, reason)：if条件成立则跳过单个用例或测试类，reason是跳过的原因。
@unittest.skipUnless(condition, reason)：条件为False则跳过单个用例或测试类，reason是跳过的原因。
@unittest.expectedFailure：标记测试用例为失败，不会出现在统计结果中。
exception unittest.SkipTest(reason)：跳过用例并抛出异常。
TestSuite和TestCase都有如下方法：
countTestCases()：返回测试用例的数量。
run(result)：运行套件相关的测试用例，收集测试结果到result对象中并传给result

Test Loder
TestLoadder用来加载TestCase到TestSuite中。
loadTestsFrom*()方法从各个地方寻找testcase，创建实例，然后addTestSuite，再返回一个TestSuite实例
defaultTestLoader() 与 TestLoader()功能差不多，复用原有实例
loadTestsFromTestCase(testCaseClass)：从unittest.TestCase的子类即测试类中加载用例并返回测试套。
loadTestsFromName(name,module=None)：从特定的字符串说明符中加载用例并返回测试套。
loadTestsFromNames(names,module=None)：用法和 loadTestsFromName(name,module=None)类似，不同的是它可以接受字符串说明符列表，而不是一个。
loadTestsFromModule(module, pattern=None)：从模块中加载所有测试用例，返回一个测试套件。
getTestCaseName(testCaseClass)：返回一个有序的包含在testCaseClass中的方法名列表
unittest.TestLoader().discover(start_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../test_case'),pattern='test*.py'):设定测试用例的执行路径，然后自动查找所有测试用例

"""