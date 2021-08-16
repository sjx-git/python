import time
# xlrd 最新版本2.1.0不支持xlsx格式，需要用到旧版1.2.0
import ddt,xlrd

from GUI自动化.test_fixture.test_fixture_demo import *

@ddt.ddt
class Send(WebUnittest):
    """完成test用例集合"""
    url = 'http://www.baidu.com'
    # 所要读取的Excel表所在地址 同级用/  非同级用..   另外Excel表需要是xlsx格式,并且内容需要文本格式
    xlsx = xlrd.open_workbook('/Users/sunjiaxing/sjx/python/GUI自动化/test_file/工作簿1.xlsx','r')
    # 定位读取的表格 可以用name 也可以用index
    #table = xlsx.sheet_by_name("Sheet1")
    table = xlsx.sheet_by_index(0)
    # # 统计有多少行
    # print(table.nrows)
    # # 统计有多少列
    # print(table.ncols)
    # # 读取第几行的数据 从0开始
    # print(table.row_values(1))
    # print(table.row_values(1)[1])
    # # 读取第几列的数据 从0开始
    # print(table.col_values(1))
    # 读取时，可以用开始和结束位置（不是从0开始的）限制获取值内容
    data = []
    # 根据总行数，遍历出所有值，加入到列表中 组成data数据
    for i in range(1,table.nrows):
        data.append(table.row_values(rowx=i,end_colx=None))
    #print(data)

    @ddt.data(*data)
    @ddt.unpack
    def test_send_kword(self,usr,passwd,phone):
        # 发送请求url
        self.chrome_webdriver.get(self.url)
        # 用id方法 定位
        self.chrome_webdriver.find_element_by_id('kw').send_keys(usr)
        # 使用id方法定位后，进行点击操作
        self.chrome_webdriver.find_element_by_id('su').click()
        time.sleep(1)
        self.assertIs(1,1)
    @ddt.data(*data)
    @ddt.unpack
    def test_send_kword1(self,usr,passwd,phone):
        # 发送请求url
        self.chrome_webdriver.get('http://www.baidu.com')
        # 用id方法 定位
        self.chrome_webdriver.find_element_by_id('kw').send_keys(phone)
        # 使用id方法定位后，进行点击操作
        self.chrome_webdriver.find_element_by_id('su').click()
        #time.sleep(1)
        self.assertIn(2,[2,3,4])


if __name__ == '__main__':
    # 实例化类
    unittest.main()
