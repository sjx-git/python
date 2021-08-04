from pymysql import connect
class mysql_demo(object):
    def mysql_open(self):
        #connection 建立数据库连接 需要注意的就是 这个用户名  必须是在数据库中允许外部链接访问的用户才可以
        db = connect(host='192.168.1.5', user='root', password="sjx@123A",database='test1', port=3306, charset='utf8')
        cour = db.cursor()# 使用cursor()方法获取操作游标

        sql = 'select * from cj'
        cour.execute(sql)#使用execute方法执行SQL语句
        data = cour.fetchone()# 使用 fetchone() 方法获取一条数据
        dd = cour.fetchall() #h获取执行sql语句的所有结果
        print(dd,end=' ')#打印返回结果

        cour.close()#先关闭执行结果得引用cour
        db.close()#最后关闭数据库连接

if __name__ == '__main__':
    mysql_demo.mysql_open('self')