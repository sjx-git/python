from socket import *

#创建套接字
clientSocket = socket(AF_INET,SOCK_STREAM)
#链接服务端进行通信
clientSocket.connect(('192.168.1.5',7780))
#给服务端发送信息
datas = input('输入要发送的内容：')
clientSocket.send(datas.encode('utf-8'))#发送内容，并指定解码方式为utf8
#接受对方发送过来的 一次最大接受是1024个字节
res = clientSocket.recv(1024).decode('utf-8')#接收内容，并指定解码方式为utf8
print(res)
#关闭客户端套接字的连接
clientSocket.close()