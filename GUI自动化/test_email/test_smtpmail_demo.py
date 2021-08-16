import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Email():
    """完成邮件的构建"""
    def __init__(self):
        # 设置邮箱服务器
        self.smtp_server = 'smtp.163.com'
        # 设置发件人账号
        self.user = '18612747509@163.com'
        # 设置发件人密码 这个密码是授权码
        self.password = 'DPOMWRPVZICRWMHK'
        # 设置收件人账号
        self.rev_user = '18612747509@163.com'
        # 设置邮件服务器端口号
        self.port = 465
    def send_email(self):
        # 创建一个带附件的实例，并说明邮件是由多部分构成的
        msg = MIMEMultipart()
        # 设置发件人名称
        msg['from'] = '本人发送'
        # 设置收件人名称
        msg['to'] = '本人接收'
        # 设置邮件主题
        msg['subject'] = '带附件的邮件实例'
        # 设置邮箱正文格式及编码方式
        boby = MIMEText('正文。。。。','plain','utf-8')
        msg.attach(boby)
        # 构造附件，传送当前目录下的 test.txt 文件
        with open(r'../../__init__.py','rb') as fb:
            body1 = fb.read()
        att = MIMEText(body1,'base64','utf-8')
        att["Content-Type"] = 'application/octet-stream'

        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="test.html"'
        msg.attach(att)
        # 创建发送邮件服务实例化对象
        smtp_info = smtplib.SMTP_SSL(self.smtp_server,self.port)
        # 发件人登录
        smtp_info.login(self.user,self.password)
        # 发送邮件
        smtp_info.sendmail(self.user,self.rev_user,msg.as_string())
        # 关闭发件服务
        smtp_info.quit()


if __name__ == "__main__":
    Email().send_email()