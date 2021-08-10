from socket import *

serverSockets = socket(AF_INET,SOCK_STREAM)#创建套接字，协议类型是tcp

serverSockets.bind(('',7780))#绑定IP地址(不写具体的ip代表只要是属于这个服务器的任意ip都可以通信)和端口号，以便能让对方准确找到,注意端口只能绑定一次，再次运行 就需要写新的端口号

serverSockets.listen(1)#变主动套接字为被动套接字,里边的值随便写 只要是正数就可以

# (<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.5', 7781), raddr=('192.168.1.5', 60933)> ('192.168.1.5', 60933))
newSocket,addr = serverSockets.accept()#创建的新的套接字，给到这个用户一对一的对话；因为返回的是元祖，所以以此解包为新的客户端套接字，客户端的ip和端口号
#print(newSocket,addr)

res = newSocket.recv(1024).decode('utf-8')#接受对方发送过来的 一次最大接受是1024个字节，并指定解码方式为utf8
print(res)

newSocket.send(res.encode('utf-8'))#发送内容，并指定解码方式为utf8

newSocket.close()#关闭这个客户断的套接字

serverSockets.close()#关闭服务端的套接字，不在接受任何服务


