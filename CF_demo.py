'''  老王开枪打老宋'''
class person():
    '''人的属性以及一些操作功能'''
    def __init__(self,name):
        super(person, self).__init__()
        self.name = name
        self.qiang = None
        self.hp = 100
    def anzhuang_zidan(self,dajia,zidan_temp):#将子弹安装在 弹夹中
        dajia.baocun_zidan(zidan_temp)
    def anzhaung_danjia(self,qiang_temp,danjia_temp):#将弹夹安装在 枪上
        qiang_temp.baocun(danjia_temp)
    def naqiang(self,qiang_temp):#人拿起 枪
        self.qiang = qiang_temp
    def gongji(self,person_temp):
        self.qiang.koubanji(person_temp)
    def __str__(self):
        if self.qiang:
             return '%s的血量还有%s,拿的%s'%(self.name,self.hp,self.qiang)
        else:
            if self.hp > 0:
                return '%s的血量还有%s, 没有枪'%(self.name,self.hp)
            else:
                return ('%s 挂了。。。'%self.name)
    def diaoxue(self,zidan_shanghai):
        self.hp -= zidan_shanghai
class gun():
    ''' 枪的属性'''
    def __init__(self,qiang):
        super(gun, self).__init__()
        self.qiang = qiang
        self.danjia = None
    def baocun(self,dajia_temp):
        self.danjia = dajia_temp
    def __str__(self):
        if self.danjia:
            return '枪的信息是：%s,%s'%(self.qiang,self.danjia)
        else:
            return '枪的信息是：%s,%s'%(self.qiang,self.danjia)
    def koubanji(self,diren):
        self.danjia.qudanjia(diren)

class danjia():
    ''' 弹夹的属性和用处'''
    def __init__(self,danjia1):
        super(danjia, self).__init__()
        self.maxlist = danjia1
        self.danjia_rongliang = []
    def baocun_zidan(self,zidan_temp):
        self.danjia_rongliang.append(zidan_temp)
    def __str__(self):
        if self.danjia_rongliang:
            return '弹夹的容量是：%d/%d'%(len(self.danjia_rongliang),self.maxlist)
        else:
            return '弹夹的容量是：%d/%d'%(len(self.danjia_rongliang),self.maxlist)
    def qudanjia(self,diren):
        if self.danjia_rongliang:
            pp =  self.danjia_rongliang.pop()
            pp.shanghai(diren)
        else:
            print('打空了，赶紧填弹。。。')
class zidan():
    '''子弹的属性和用处'''
    def __init__(self,zidan1):
        super(zidan, self).__init__()
        self.zidan1 = zidan1
    def __str__(self):
        return '子弹的杀伤力是：%d'%self.zidan1
    def shanghai(self,diren):
        diren.diaoxue(self.zidan1)
#创建拿枪的人
laowang = person('老王')
#创建抢
M4a1 = gun('m4a1')
#创建子弹的杀伤力
zidan = zidan(10)
#创建弹夹的数量
danjia1 = danjia(15)
#把子弹装到弹夹中 多次压弹
for i in range(15):
    laowang.anzhuang_zidan(danjia1,zidan)
#把弹夹装到抢中
laowang.anzhaung_danjia(M4a1,danjia1)
#拿起枪
laowang.naqiang(M4a1)
#查看人此时的状态
#print(laowang)

#创建敌人
laoli = person('老李')

for i in range(19):
    #攻击敌人
    laowang.gongji(laoli)
    #查看敌人此时的状态
    print(laoli)
    print(laowang)

