"""
os.path.join()函数
    函数用于路径拼接文件路径，可以传入多个参数。连接两个或更多的路径名组件
        如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾

        如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃;从倒数第一个，以‘/’开头的参数开始拼接，之前的参数全部丢弃。
            print os.path.join('/111','/222','/333') #/333
            print os.path.join('111','222','/333') #/333
            print os.path.join('111','/222','/333') #/333
            print os.path.join('/111','/222','/333') #/333
        如果各组件名首字母不包含’/’，则函数会自动加上
            print os.path.join('111/','222','333') #111/222/333
            print os.path.join('111/','222/','333') #111/222/333
            print os.path.join('111/','222/','333/') #111/222/333/

            print os.path.join('111','222','333')  #111/222/333
            print os.path.join('/111','222','333') #/111/222/333
            print os.path.join('/111','/222','333') #/222/333
        以‘/’结尾的，以及参数中间有‘/’的，斜杠仅作为参数的一部分。
            print os.path.join('111','222','./333') #111/222/./333
            print os.path.join('111','222','333/') #111/222/333/
            print os.path.join('111','222/','333/') #111/222/333/
            print os.path.join('111/','222/','333/') #111/222/333/

# 运行的时候如果输入完整的执行的路径，则返回当前.py文件的全路径；python c:/test/test.py 则返回路径 c:/test ，如果是python test.py 则返回空
    print(os.path.dirname(__file__))
# os.path.abspath(__file__)返回的当前.py文件的绝对路径
    print(os.path.dirname(os.path.abspath(__file__)))
"""
import os
import time
import HTMLTestRunner
from GUI自动化.test_suites import test_suites_demo
from GUI自动化.test_email.test_yagmail_demo import Yagmail


class Main_demo():
    """ 通过调用测试套件，进行测试用例脚本的执行，然后再通过调用发送邮件方法，发送测试报告到邮箱中"""
    def main1(self):
        '''此处，必须用wb二进制写入，不然会报错： TypeError: write() argument must be str, not bytes'''
        report_name = os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0],"test_reports",time.strftime('%Y_%m_%d_%H_%M_%S')+'resport.html')
        #print(report_name)
        file_name = open(report_name,'wb')
        # verbosity=*：指数粗错误情况下的信息--默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
        runner = HTMLTestRunner.HTMLTestRunner(stream=file_name,title='GUi自动化测试',description='简单的demo',verbosity=0)
        #runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
        runner.run(test_suites_demo.TestSuites().test_sutes())
        Yagmail().yagmail_send(report_name)

if __name__ == "__main__":
    Main_demo().main1()
