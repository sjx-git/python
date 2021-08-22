import requests
import unittest
from API自动化.test_fixture.test_fixture_demo import *


class Request(ApiUnittest):
    """完成接口请求的demo"""
    '''
    接口地址：http://apis.juhe.cn/simpleWeather/query
    返回格式：json
    请求方式：http get/post
    请求示例：http://apis.juhe.cn/simpleWeather/query?city=%E8%8B%8F%E5%B7%9E&key=
    接口备注：通过城市名称或城市ID查询天气预报情况 
    '''

    def test_request_send(self):
        # {'reason': '查询成功!', 'result': {'city': '北京', 'realtime': {'temperature': '29', 'humidity': '41', 'info': '多云', 'wid': '01', 'direct': '西北风', 'power': '1级', 'aqi': '33'}, 'future': [{'date': '2021-08-17', 'temperature': '20/29℃', 'weather': '多云转阴', 'wid': {'day': '01', 'night': '02'}, 'direct': '东南风转东风'}, {'date': '2021-08-18', 'temperature': '22/29℃', 'weather': '阴转小雨', 'wid': {'day': '02', 'night': '07'}, 'direct': '南风转东南风'}, {'date': '2021-08-19', 'temperature': '22/25℃', 'weather': '大雨转小雨', 'wid': {'day': '09', 'night': '07'}, 'direct': '东南风'}, {'date': '2021-08-20', 'temperature': '21/29℃', 'weather': '多云', 'wid': {'day': '01', 'night': '01'}, 'direct': '南风转西南风'}, {'date': '2021-08-21', 'temperature': '22/30℃', 'weather': '多云转阴', 'wid': {'day': '01', 'night': '02'}, 'direct': '东南风'}]}, 'error_code': 0}
        city = '北京'
        res = requests.get(self.url,params={'key':self.key,'city':city}).json() # 获取json格式的响应体
        # print(res['result'])# 得到的是字典，那么就可以用下标获取值，也可以像下面一样，用字典的get获取
        info = res.get('reason')
        print(info)
        self.assertEqual('查询成功!',info)

    def test_response_recv(self):
        data = {'city':'北京','key': self.key}
        headers = {'Content-Type':'application/json'}
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).headers# 获取响应头
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).status_code# 获取响应代码
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).request# 获取请求方式
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).apparent_encoding# 获取响应编码
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).reason# 获取响应状态
        #response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).request.body# 获取响应体，如果用json=xxx，那结果就是r'xxxx',会转换为标准的json字符串，放在请求正文中
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',data=data).request.body# 获取响应体，不用json说明的，就还是原来请求的样子与上边成对比
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).cookies# 获取cookie
        response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',params=data).json()# 获取json格式的响应体
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).raw# 获取原始响应体
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).content# 获取字节方式的响应体，自动解码gzip和deflate压缩
        # response1 = requests.post(url='http://apis.juhe.cn/simpleWeather/life',json=data).text# 获取字符串方式的响应体，根据headers信息自动解码
        info1 = response1.get('reason')
        print(info1)
        self.assertIn('查询成功',info1)


if __name__== "__main__":
    unittest.main()