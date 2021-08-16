''' 创建模块'''
def xxx():
    print(1)

'''  导入模块  第一种'''
#from xxx import  xx 或者 from xxx import  * 这个*慎用，只需要导入想用的就好；此外会依据就近原则覆盖其他同名的方法
#xx() #直接调用里边的方法

'''  导入模块  第二种'''
#import  xxx
xxx.xx() #用模块名调用里边的方法

''' __all__ 用来控制这个模块中，哪儿些内容可以让其他模块导入并使用'''
__all__ = ['允许访问的方法比如test']
def test():
    pass
num = 1#all中不写，无法被调用
''' 常用的标准块
builtins	        内建函数默认加载
os	                操作系统接口
sys	                Python自身的运行环境
functools	        常用的工具
json	            编码和解码 JSON 对象
logging 	        记录日志，调试
multiprocessing	    多进程
threading	        多线程
copy	            拷贝
time	            时间
datetime	        日期和时间
calendar	        日历
hashlib	            加密算法
random	            生成随机数
re	                字符串正则匹配
socket	            标准的 BSD Sockets API
shutil	            文件和目录管理
glob	            基于文件通配符搜索
'''
'''常用 拓展库
requests	            使用的是 urllib3，继承了urllib2的所有特性
urllib	                基于http的高层库
scrapy	                爬虫
beautifulsoup4	        HTML/XML的解析器
celery	                分布式任务调度模块
redis	                缓存
Pillow(PIL)	            图像处理
xlsxwriter	            仅写excle功能,支持xlsx
xlwt	                仅写excle功能,支持xls ,2013或更早版office
xlrd	                仅读excle功能
elasticsearch	        全文搜索引擎
pymysql	                数据库连接库
mongoengine/pymongo	    mongodbpython接口
matplotlib	            画图
numpy/scipy	            科学计算
django/tornado/flask	web框架
xmltodict	            xml 转 dict
SimpleHTTPServer	    简单地HTTP Server,不使用Web框架
gevent	                基于协程的Python网络库
fabric	                系统管理
pandas	                数据处理库
scikit-learn	        机器学习库
'''