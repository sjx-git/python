from pymysql_demo import pymysql1_demo

def tel():
    #调试 封装方法后的效果是否正常
    db = pymysql1_demo.fengzhuang('192.168.1.5', 3306, 'root', 'sjx@123A', 'test1')
    db.connect_fuc()#此处需要新调用connect初始化方法

    sql = 'select * from cj;'
    db.select1(sql)
    #a = db.fetchOne_func()
    a = db.fetchAll_func()
    print(a)


if __name__ == '__main__':
    tel()