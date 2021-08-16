import time

import yagmail


class Yagmail():
    """yagmail发送邮件实例，比smtp要简单的多"""

    def yagmail_send(self,*args):
        # 实例化smtp对象
        yag_info = yagmail.SMTP(user='18612747509@163.com', password='DPOMWRPVZICRWMHK', host="smtp.163.com", port=465,
                                encoding="utf-8")
        # 写正文内容
        contents = ['正文详情']
        # 为了是此方法 在不传递测试报告的情况下仍可用，做一个判断
        if args == ():
            attachments = None
        else:
            # 因为args是个元组，所以，需要单个值取出来，用下标
            args = args[0]
            attachments = [args]
        # 发送邮件
        email_info = '18612747509@163.com'
        #email_info = '1064200847@qq.com'
        yag_info.send(to=email_info, subject='GUI测试'+time.strftime('%Y_%m_%d_%H_%M_%S'), contents=contents,
                      #attachments=[r"../test_file/工作簿1.xlsx"]
                        #attachments=[r"../test_file/孙尚香.html"]
                      attachments=attachments,prettify_html=False
                      )
        yag_info.close()


if __name__ == '__main__':

    Yagmail().yagmail_send(r"/Users/sunjiaxing/sjx/python/GUI自动化/test_reports/2021_08_16_18_19_11resport.html")
