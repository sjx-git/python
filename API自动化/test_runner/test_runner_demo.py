import HTMLTestRunner
import os
import time
from API自动化.test_suite.test_suites_demo import TestSuites
from API自动化.test_mail.test_mail_demo import SendMail

class TestRunner():


    def main(self):
        """执行HTMlTestRunner程序"""

        # 获取报告路径及设定报告的名称，记得加后缀
        report_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'test_report',"test_report"+time.strftime("%y_%m_%d_%H_%M_%s")+'.html')
        # 写入报告内容
        with open(report_name,'wb') as fb:
            HTMLTestRunner.HTMLTestRunner(stream=fb,title='API自动化报告',description='接口自动化执行后的报告',verbosity=2).run(TestSuites().test_sutes())
        # 发送报告
        SendMail().send_mail(report_name)


if __name__ == '__main__':
    # 实例化对象
    test_runner_info = TestRunner()
    test_runner_info.main()