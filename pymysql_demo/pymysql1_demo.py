from pymysql import connect

class fengzhuang():
    #将数据库常用配置及方法进行封装，以便其他模块调用
    def __init__(self,host,port,username,password,database,chatset='utf8'):
        #数据库配置
        self.host = host
        self.port =port
        self.username = username
        self.password= password
        self.database = database
        self.charset = chatset

    def connect_fuc(self,*args):
        #完成数据库的连接以及游标初始化
        self.connect1 = connect(host=self.host,port=self.port,user=self.username,password=self.password,database=self.database,charset=self.charset)
        self.cursor1 = self.connect1.cursor()

    def select1(self,sql):
        self.cursor1.execute(sql)

    def fetchAll_func(self):
        res = self.cursor1.fetchall()
        return res

    def fetchOne_func(self):
        res = self.cursor1.fetchone()
        #print(self.cursor1.fetchone())
        return res

    def closed(self):
        self.cursor1.close()
        self.connect1.close()

