from pymysql import connect
class mysql_demo(object):
    def mysql_open(self):
        #connection 建立数据库连接 需要注意的就是 这个用户名  必须是在数据库中允许外部链接访问的用户才可以
        db = connect(host='192.168.52.137', user='sjx', password="sjx@123A",database='test', port=3306, charset='utf8')
        cour = db.cursor()#用于执行sql语句并返回结果
        sql =  'select * from test1'
        #影响的行数

        '''
        ff = cour.fetchone()# 获取查询结果集的第一行元组数据  这个地方要注意，如果放在fetchall下方 就会返回none 因为all把数据都取出来了  就不会再有数据
        gg = cour.nextset()#获取查询结果集的当前行的下一行元组数据
        ll = cour.fetchmany(10)#暂时没搞明白
        dd = cour.fetchall()#获取所有结果集的数据，一行构成一个元组，然后将这些元组集合到一个大元组中返回   注意上方如果有fetchone把值都取出来了 同样是只会返回none
        
        #修改数据
        up = 'update test1 set name = "王6" where id =1 '
        update1 = cour.execute(up)
        print(update1)
        
        #插入数据
        insert1 = 'insert into test1(name) value("gg") '
        cour.execute(insert1)
        
        #删除数据
        delete1 = 'delete from test1 where id = 5'
        cour.execute(delete1)  
        
        #查询表中的所有数据
        cour.execute(sql)
        
        #新增表字段
        sql2 = 'alter table test1 add  column phone int not null default "110" '
        cour.execute(sql2)
        
        
                '''


        #修改后，需要提交数据才能生效
        db.commit()
        #查询表中的所有数据
        cour.execute(sql)
        dd = cour.fetchall()
        print(dd)







        cour.close()#先关闭执行结果得引用cour
        db.close()#最后关闭数据库连接

if __name__ == '__main__':
    mysql_demo.mysql_open('self')