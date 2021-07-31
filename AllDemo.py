#coding:utf-8

'''
此demo 包含 基本架构及各种使用方法
'''

import time as  tt#列别名  当模块名很长的时候  可以用as 重新命名
#先导入标准库，第三方库，本地库   并用空行隔开
#os,sys,time,random,re
#xlrd,htmlRunner,panda,re,request,selenium

tt.sleep(1)
class Demo(object):#类方法的命名，大驼峰的方式
    #第一行，用来描述这是干嘛用的意义所在
    #类属性
    num = 0
    #实例方法

    def __fun_demo__(self):  # 实例方法的命名方式，下划线    __名字__私有方法      方法self 必须写上     函数可以不写
        pass
    #类方法
    @classmethod
    def all_demo(cls):
        pass
    #静态方法
    @staticmethod
    def print_menu():# 可以不写self
        pass
    """装饰器
    def b(name2):
        def c(name3):
            print(name2+name3)
            a()
        return c
        
    #闭包
    def d(name4):
        def e(name5):
            print(name5+name4)
            a()
        return e
    
    @b#等价于a=b(a)
    @d#等价于a=d(a)
    def a(name1):
        print("底层方法")
    a()
    """
    """装饰器 对有参数的&&不定长参数 装饰
    def b(name2):
        def c(*args,**kwargs):
            print(name2+name3)
            a(*args,**kwargs)
        return c
        
    @d#等价于a=d(a)
    def a(a,b):
        print("a= %d,b=%d"%(a,b))
    a(11,22)
    """
    """装饰器 对带有参数的&&有返回值&&不定长参数 装饰
    def b(name2):
        def c(*args,**kwargs):
            print(name2+name3)
           ret =  a(*args,**kwargs)
           return ret
        return c
        
    @d#等价于a=d(a)
    def a(a,b):
        print("a= %d,b=%d"%(a,b))
        return  "ret"
    a(11,22)
    """
    """装饰器 通用装饰器
   def b(name2):
       def c(*args,**kwargs):
           print(name2+name3)
          ret =  a(*args,**kwargs)
          return ret
       return c       
   @d#等价于a=d(a)
   def a(a,b):
       print("a= %d,b=%d"%(a,b))
       return  "ret"
   a(11,22)
   """
"""装饰器 有参数的装饰器
   def f(arg) 
       def b(name2):
           def c(*args,**kwargs):
               print(name2+name3)
              ret =  a(*args,**kwargs)
              return ret
           return c
       return b
   @f("heihei")
   def a(a,b):
       print("a= %d,b=%d"%(a,b))
       return  "ret"
   a(11,22)
   """
if __name__ == '__main_':
    #调用类方法 第一种
    demo = Demo()
    demo.all_demo()
    #调用类方法，第二种
    Demo.all_demo()


'''
http请求demo 包含post和get

import requests
class tester(object):
    def get_url(self):
        url = requests.get('http://192.168.8.240:8088/api/json')
        json_res = url.json()["jobs"][0]
        js = dict(json_res).values()
        print(js)
        print(dict(json_res).keys())
    def post_url(self):
        url = "http://192.168.8.240:8088/j_acegi_security_check"
        post_data = requests.post(url,data={"j_username":"sjx","j_password":"sjx@123A","from":"/","Submit":"登录"},json={})
        #print(post_data.text)
        r = post_data.status_code
        print(r)
if __name__ == '__main__':
    tester.get_url('self')
    tester.post_url('self')
'''

'''
单元测试  unittest 使用demo

import requests
import unittest
class API_Test(unittest.TestCase):
    Appkey = "959e4fc1aa5787e67ae143901b2d2673"
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    def test01(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        #city = input("请输入要查询的城市名称：")
        par = {"city":"北京","key":API_Test.Appkey}
        res = requests.get(url,params=par).json()
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])#assertIn 判断时候包含
    def test02(self):
        url = "http://apis.juhe.cn/simpleWeather/wids"
        post_res = requests.post(url,data ={"key":API_Test.Appkey}).json()
        print(post_res['reason'])
        self.assertEqual(post_res['reason'],'查询成功')#assertEqual 判断是否一致
    def re_session(self):
        pass
        """
        当有需要验证信息比如：session的时候，就需要用
        s = request.session() 来保持和下一个接口建立相同的链接通道
        res = s.get(url) 正常用就好了
        导入正则包 re 
        usersession = re.findall(r'正则表达式(.+？)'，res)
        此时的session就可以用了  取出的是列表  用usersession[0]
        """
if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    unittest.main()
'''
'''
改进版 Post_demo
import requests
import unittest

class Api_test1(unittest.TestCase):
    key = '959e4fc1aa5787e67ae143901b2d2673'
    url = 'http://apis.juhe.cn/simpleWeather/query'
    def test_post(self,city):
        #判断city是否为数字或者为汉字  （是否为字母 (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a')）
        if (city >= u'\u4e00' and city <=u'\u9fa5') or (city >= u'\u0030' and city<=u'\u0039' ) :
            par = {'key':self.key,'city':city}
            rets = requests.post(self.url,data=par).json()
            #print(rets)
 
if rets['error_code'] == 207301:
    print('暂不支持该城市')
else:
    eq = rets['result']['city']
    if self.assertTrue(eq,city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
        print('查询成功')
try:
    eq = rets['result']['city']
    if self.assertTrue(eq,city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
        print('查询成功')
except:
    #print(rets)
    if rets['error_code'] == 207301:
        print('暂不支持该城市')
    else:
        print('输入不正确')
if __name__ == '__main__':
f = Api_test1()
f.test_post(input('请输入要查询的城市名称或者数字：'))
'''

'''
数据和代码分离之读取Excel表 用到xlrd 使用demo

import xlrd
import requests
import unittest
class API_Test(unittest.TestCase):
    city = ''
    key = ''
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    @classmethod
    def setUpClass(self):
        book = xlrd.open_workbook("../data/data1.xlsx")#所要读取的Excel表所在地址 同级用/  非同级用..   另外Excel表需要是xlsx格式,并且内容需要文本格式
        res = book.sheet_by_name("Sheet1")#定位读取的表格 可以用name 也可以用index
        #print(res.nrows)#统计有多少行
        #print(res.ncols)#统计有多少列
        #print(res.row_values(1)[0])
        global city
        city = res.row_values(1,0,3)#读取下标1的行数据 ，并且是从下标0的列到下标3的列，所有的下标都不包含其本身，即 这个是从除去列名所在的第一行  从表格第二行开始 
        global key
        key = res.col_values(1,1,3)#读取下标1的列数据 ，并且是从下标0的行到下标3的行，所有的下标都不包含其本身，即 这个是从除去列名所在的第一列  从表格第二行开始 
        #print(city)
        #print(key)
    def test01(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        #print(city)
        #print(key)
        par = {"city":city,"key":key}
        res = requests.get(url,params=par).json()
        print(res)
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])
    def test02(self):
        url = "http://apis.juhe.cn/simpleWeather/wids"
        post_res = requests.post(url,data ={"key":key}).json()
        print(post_res['reason'])
        self.assertEqual(post_res['reason'],'查询成功')
if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    unittest.main()
    #API_Test.xlsx("self")

'''

'''
在字符串中,取出汉字,
import re
class test(object):
    def demo(self):
        a = '!@$你&......*好&^*未(0)kill来~!%$,./'
        str = re.sub("[A-Za-z0-9\%\(\)\,\。\.\@\$\&\*\~\^\/]", "",a)
        print(str.lstrip("!"))
if __name__ == '__main__':
    test.demo('self')
'''

'''
os.path.abspath(__file__)#获取当前脚本所在路径  F:\bbd.com\Csrc_tobelist\Tobelist_ETl\Etl_file.py
current_path = os.path.dirname(os.path.abspath(__file__))#将当前获取到的脚本路径，去除脚本后，只保留文件名 F:\bbd.com\Csrc_tobelist\Tobelist_ETl
result_path =current_path  + os.sep + 'result'   #os.sep根据你所处的平台，自动采用相应的分隔符号 linux用/  windows用\
sys.path.append(current_path) #将文件夹 放到系统变量中 以便全局使用
'''