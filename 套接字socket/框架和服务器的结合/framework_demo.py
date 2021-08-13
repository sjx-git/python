import time
from 套接字socket.框架和服务器的结合.http_server_demo import HttpServer
class application(object):
    ''' 路由类，根据不同的environ 出入的请求文件不同，调用不同的实例方法'''
    # 设置文件所在路径
    HTML_ADDR = '/Users/sunjiaxing/sjx/python/套接字socket'

    def __init__(self,urls):
        # 保存路由信息
        self.urls = urls

    def __call__(self, environ, start_response):
        # call魔法方法可以在其他脚本中，直接当方法调用
        # environ = {
        # 'Path_Info':filename
        # 'Method':addr
        # }
        # 判定请求文件和路由信息是否匹配
        fileName = environ.get('Path_Info')
        if fileName.startswith('/static'):
            try:
                # 读取静态文件中的内容
                file1 = open(self.HTML_ADDR + fileName, 'rb')
                temp = file1.read(1024)
                responseStatus = 'http/1.1 200 ok\r\n'
                responseHeader = []
                responseBody = temp.decode('utf-8')
                # print(responseBody)
            except:
                # 错误情况下 给出结果
                responseStatus = 'http/1.1 404 NOT found\r\n'
                responseHeader = []
                responseBody = '静态资源 没找到'
            else:
                # 关闭文件
                file1.close()
            start_response(responseStatus,responseHeader)
            return responseBody
        else:
            for name,func in self.urls:
               # 等于路由信息的话，直接调用相对应的函数
               #print(name,func,fileName)
               if name == fileName:
                   # return body，直接结束函数的运行，下面的都不在继续运行
                    return func(environ,start_response)
            else:
                # 文件不在路由中 返回404的提示
                responseStatus = '404 Not Found'
                responseHeader = []
                start_response(responseStatus,responseHeader)
                return '没有找到与 %s 相关的资源'%fileName

def ctime(environ,start_response):
    #因为application只能规定只能返回，response body部分，但是还需要请求头和请求行，所以这个时候就得用到第二个参数了
    status = '200 ok'
    response_headers = [
        ('content-type','text/html')#需要用元祖
    ]
    start_response(status,response_headers)
    return time.ctime()

def ctime1(environ,start_response):
    #因为application只能规定只能返回，response body部分，但是还需要请求头和请求行，所以这个时候就得用到第二个参数了
    status = '404 Not Found'
    response_headers = [
        #需要用元祖
    ]
    start_response(status,response_headers)
    return '404的请求'

if __name__ == '__main__':
    urls = [
        ('/ctime',ctime),
        ('/ctime1',ctime1)
    ]
    # 创建app对象
    app = application(urls)
    # 使用服务器调用app对象，也可以理解为将这个app对象和服务器绑定
    httpserver = HttpServer(app)
    # 绑定端口
    httpserver.bind(8112)
    # 开启服务器
    httpserver.starts()