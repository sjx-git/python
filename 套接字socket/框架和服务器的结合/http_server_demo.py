from socket import *
from multiprocessing import Process
import re
'''
Python Web Server Gateway Interface (或简称 WSGI，读作“wizgy”)。
WSGI允许开发者将选择web框架和web服务器分开。可以混合匹配web服务 器和web框架，选择一个适合的配对。比如,可以在Gunicorn 或者 Nginx/uWSGI 或者 Waitress上运行 Django, Flask, 或 Pyramid。真正的混合 匹配，得益于WSGI同时支持服务器和架构:
web服务器必须具备WSGI接口，所有的现代Python Web框架都已具备WSGI 接口，它让你不对代码作修改就能使服务器和特点的web框架协同工作。
WSGI由web服务器支持，而web框架允许你选择适合自己的配对，但它同样 对于服务器和框架开发者提供便利使他们可以专注于自己偏爱的领域和专⻓ 而不至于相互牵制。其他语言也有类似接口:java有Servlet API，Ruby 有 Rack。
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应 HTTP请求。我们来看一个最简单的Web版本的“Hello World!”:
    def application(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return 'Hello World!'
    上面的 application() 函数就是符合WSGI标准的一个HTTP处理函数，它 接收两个参数:
        environ:一个包含所有HTTP请求信息的dict对象; 
        start_response:一个发送HTTP响应的函数。
整个 application() 函数本身没有涉及到任何解析HTTP的部分，也就是 说，把底层web服务器解析部分和应用程序逻辑部分进行了分离，这样开发 者就可以专心做一个领域了
不过，等等，这个 application() 函数怎么调用?如果我们自己调用，两 个参数environ和start_response我们没法提供，返回的str也没法发给浏览 器。
所以 application() 函数必须由WSGI服务器来调用。有很多符合WSGI规 范的服务器。而我们此时的web服务器项目的目的就是做一个极可能解析静 态网⻚还可以解析动态网⻚的服务器
'''

class HttpServer(object):
    """完成浏览器用http协议，请求简单服务器的 动态请求以及静态资源请求的demo
        实现原理是，通过关联不同的框架，达到访问不同的方法
        这个demo主要是为了展示 框架和服务器结合的概念，这就是demo的目的
    """
    def __init__(self,app):
        # 初始化套接字
        self.serviers = socket(AF_INET, SOCK_STREAM)
        self.app = app

    def bind(self, port):
        # 绑定端口和ip
        self.serviers.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serviers.bind(('', port))

    def starts(self):
        # 将主动监听变为被动
        self.serviers.listen(10)
        while True:
            # 创建新的一对一 套接字以便使用
            clientSocket, addr = self.serviers.accept()
            # 创建子进程
            P = Process(target=self.http_demo, args=(clientSocket,))
            P.start()
            P.join()
            clientSocket.close()
    def start_response(self,status,response_headers):
        #print(response_headers)
        responseHeader = 'http/1.1 '+status+'\r\n'
        for i in response_headers:
            responseHeader += '%s:%s\r\n'%i
            #print(responseHeader)
        self.response_header = responseHeader

    def http_demo(self,clientSocket):
        # 处理客户端请求
        res = clientSocket.recv(1024).decode('utf-8')
        # print(res)
        # 提取请求行中的路径  GET /  HTTP/1.1
        fileName = re.match(r'\w+\s+(/[^\s]*)\s+', res).group(1)
        addr = re.match(r'(\w+)\s+/[^\s]*\s+', res).group(1)
        # 组建 environ 字典
        environ = {
        'Path_Info':fileName,
        'Method':addr
        }
        body = self.app(environ,self.start_response)
        responses = self.response_header+'\r\n'+body  # 组成最终的response  此处注意，不要忘了空行
        clientSocket.send(bytes(responses.encode('gb2312')))  # 注意要写明编码类型.utf-8 会导致浏览器乱码
        #print(responses)


def main():

    # 创建服务器对象
    httpSocket = HttpServer()
    httpSocket.bind(8112)
    httpSocket.starts()


if __name__ == "__main__":
    main()
