import time

import yagmail
class SendMail():
    def send_mail(self,*args):

        # 为了是此方法 在不传递测试报告的情况下仍可用，做一个判断
        if args == ():
            attachments = None
        else:
            # 因为args是个元组，所以，需要单个值取出来，用下标
            args = args[0]
            attachments = [args]
        # 实例化yagmail对象
        yagmail_info = yagmail.SMTP(user="18612747509@163.com",password='DPOMWRPVZICRWMHK',host="smtp.163.com",port=465,encoding='utf-8')
        yagmail_info.send(to="18612747509@163.com",
                          subject='这是标题'+time.strftime('%Y_%m_%d_%H_%M_%S'),
                          contents="这是内容",
                          attachments=attachments)


if __name__ == '__main__':
    SendMail().send_mail()