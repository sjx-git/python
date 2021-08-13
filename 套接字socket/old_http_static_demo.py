from socket import *
from multiprocessing import Process
import re


class serverSoket(object):
    """完成浏览器用http协议，请求简单服务器的 动态请求以及静态资源请求的demo
        实现原理是，通过获取不同的请求文件，指定不同的py文件中，但是如果有1k个路径就要有1k个py文件，非常冗余
        这个demo主要是为了引出 高级版的框架概念，需要先理解最初的 设计理念是什么 这就是demo的目的
    """
    # 设置文件所在路径
    HTML_ADDR = '/Users/sunjiaxing/sjx/python/套接字socket'

    def __init__(self):
        # 初始化套接字
        self.serviers = socket(AF_INET, SOCK_STREAM)

    def bind(self, port):
        # 绑定端口和ip
        self.serviers.setsockopt(SOL_SOCKET, SO_REUSEADDR, 10)
        self.serviers.bind(('', 8112))

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

    def http_demo(self,clientSocket):
        # 处理客户端请求
        res = clientSocket.recv(1024).decode('utf-8')
        # print(res)
        # 提取请求行中的路径  GET /  HTTP/1.1
        fileName = re.match(r'\w+\s+(/[^\s]*)\s+', res).group(1)
        if '/' == fileName:
            fileName = 'index.html'
        try:
            # 读取静态文件中的内容
            file1 = open(self.HTML_ADDR + fileName, 'rb')
            temp = file1.read(1024)
            responseStatus = 'http/1.1 200 ok\r\n'
            responseHeader = 'server my servsre\r\n'
            responseBody = temp.decode('utf-8')
            # print(responseBody)
        except:
            # 错误情况下 给出结果
            responseStatus = 'http/1.1 404 NOT found\r\n'
            responseHeader = 'server my servsre\r\n'
            responseBody = '没找到资源'
        else:
            # 关闭文件
            file1.close()
        finally:
            # 返回信息给客户端
            responses = responseStatus + responseHeader + '\r\n' + responseBody
            clientSocket.send(bytes(responses.encode('gb2312')))  # 注意要写明编码类型.utf-8 会导致浏览器乱码


def main():
    # 创建对象
    httpSocket = serverSoket()
    httpSocket.bind(8000)
    httpSocket.starts()


if __name__ == "__main__":
    main()
