from pymysql import connect
class create_tables_demo(object):
    def create_demo(self):
        #connection 建立数据库连接 需要注意的就是 这个用户名  必须是在数据库中允许外部链接访问的用户才可以
        db = connect(host='192.168.1.5', user='root', password="sjx@123A",database='test1', port=3306, charset='utf8')
        cursor1 = db.cursor()
        ''' sql = 'create table demo2(id int not null primary key auto_increment,' \
              'name varchar(10),isDelete bit default 1,' \
              'foreign key(id) references demo1(id));'''
        sql = 'create table demo3(id int );'
        cursor1.execute(sql)
        db.commit()
        cursor1.execute('desc demo3;')
        for i in cursor1.fetchall():
            print(i)

if __name__ == '__main__':
    create_tables_demo.create_demo('self')