#coding:utf-8
import re
class Re_demo(object):
    '''
        .	匹配任意1个字符（除了\n）
        [ ] 匹配[ ]中列举的字符           #[0-9] 等同于\d  [^0-9]等同于\D   以此类推
        \d	匹配数字，即0-9
        \D	匹配非数字，即不是数字
        \s	匹配空白，即 空格，tab键
        \S	匹配非空白
        \w	匹配单词字符，即a-z、A-Z、0-9、_
        \W	匹配非单词字符

        *	匹配前一个字符出现0次或者无限次，即可有可无:(\d*,'aaa')结果是对的哦，因为是意味着数子是可以不出现的
        +	匹配前一个字符出现1次或者无限次，即至少有1次
        ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
        {m}	匹配前一个字符出现m次
        {m,}	匹配前一个字符至少出现m次
        {m,n}	匹配前一个字符出现从m到n次

        ^	匹配字符串开头
        $	匹配字符串结尾
        \b	匹配一个单词的边界
        \B	匹配非单词边界

        |	匹配左右任意一个表达式
        (ab)	将括号中字符作为一个分组
        \num	引用分组num匹配到的字符串
        (?P<name>)	分组起别名
        (?P=name)	引用别名为name分组匹配到的字符串

        match方法从头开始找，找到就返回，否则为None，只匹配一次
        search从头依次搜索，只匹配一次
        findall方法：返回列表，匹配所有
        sub 替换
        split 根据匹配进行切割字符串，并返回一个列表
        在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。

    '''

    def re_demos(self):
        self.itcast = 'itcast'
        s = self.itcast
        A = 'itcastDEMO'
        res = re.match(s,A)  # match(匹配的格式，匹配的字符串)，从左到右开始匹配并且是需要完全匹配才可以。
                             # 当匹配正确的时候，只要前部分完全匹配 后边的无论是什么  都算是正确的；并将匹配格式或者说是匹配到的那部分数据返回，并不是会将 匹配对象全部返回；
                             # 当匹配错误的时候，返回None
        #print(res.group())  # 用group 将结果展示出来，当res为none的时候 会报错

        #原始字符串 r
        # s = '/nabc'
        # re.match('\\\\n/w',s)#当出现\后 往往是在正则表达式中需要转义的，为了解决这种问题麻烦的写法  直接在最前边加个r
        # re.match(r'\n\w',s)

        # 验证手机号
        #phone = re.match('\d\d\d\d\d\d\d\d\d\d\d','18612747509jjjjj')#第一种   虽然可以满足十一位，但是后边是字母也可以演通过
        #phone = re.match('\1[35678]','18jjjj')#括号中的不用逗号隔开就可以，效果是匹配其中任意一个就可以
        #phone = re.match('\1[35678]\d{9}','18612747509jjjj')# 同样是虽然可以满足以1开头，第二位是从中选取一位，然后后面补全9位凑够11位，但仍然不能限制最后的字母
        phone = re.match(r'1[3568]\d{9}$','18612747509')#正确写法，开头 中间数 个数及结尾 实现
        #print(phone)

        #匹配0-100
        num = re.match(r'[1-9]?\d?$|100','0')#个位数出现就是1-9 不出现就是匹配后边的\d 再用 管道加上100
        #print(num)

        #匹配邮箱
        mail = re.match(r'\w+@(163|qq|gmail)\.(com|net|cn)$','10642002847@qq.com')
        #print(mail)
        mail = re.match(r'\w+@(163|qq|gmail)\.(com|net|cn)$','10642002847@qq.com')
        #正则提取
        mail = re.match(r'(?P<key>\w+)@(163|qq|gmail)\.(com|net|cn)$','10642002847@qq.com')#起列别名的时候，P是大写的
        #print(mail.group('key'))
        #获取接口
        # url = 'http://baidu.com/name/login?id=1'
        # l = re.sub(r'^http://.+?/','',url)
        # print(l)
        #获取域名 第一种方式
        # url = 'http://baidu.com/name/login?id=1'
        # l = re.match(r'(?P<name>^http://.+?/)',url)
        # print(l.group('name'))
        #获取域名 第二种方式
        # url = 'http://baidu.com/name/login?id=1'
        # print(type(url))
        # l = re.sub(r'(?P<name>^http://.+?/).*',lambda name:name.group(1),url) # sub 将匹配到的数据进行替换
        # print(l)
        #获取域名 第三种方式
        # url = 'http://baidu.com/name/login?id=1'
        # l = re.search(r'^http://.+?/',url)
        # print(l.group())
        #获取多个域名 不能用 ^ 开头 不然只能匹配到第一个就结束了
        # url = 'http://baidu.com/name/login?id=1,http://sougou.com/name/login?id=1'
        # l = re.findall(r'http://.+?/',url)
        # print(l)
        #split 切割
        # url = 'http://baidu.com/name/login?id=1,http://sougou.com/name/login?id=1'
        # sp = re.split(r':|/|,|=|\.|\?',url)
        # # print(sp)
        # s = 'This text is displayed if your browser does not support the Canvas HTML element.利用业务经验整理的指标体系评价公司，触发阈值的指标越多，风险值越高。'
        # l = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.','',s)
        # print(l)
        t = '主板、中小板：风险拟上市公司数量/总数'
        print(re.match(r'\w+、\w+',t))
if __name__ == '__main__':
    Re_demo().re_demos()