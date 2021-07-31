class house():

    def __init__(self,mj,addr,gj):
        self.mj = mj
        self.gj = gj
        self.addr = addr
        self.dq = []

    def dianqi(self,bed1):
        self.mj1 =self.mj - bed1.ares
        self.dq.append(bed1.name)
    def __str__(self):
        return print('房子总面积为：%d，剩余面积为：%d，格局为：%s，地址为：%s,家具家电有：%s'%(self.mj,self.mj1,self.gj,self.addr,str(self.dq)))

class bed():

    def __init__(self,name,ares):
        self.name = name
        self.ares = ares
    def __str__(self):
        return print('%s的大小为：%d'%(self.name,self.ares))




if __name__ == '__main__':
    home = house(120,'天安门','三室一厅')

    bed1 = bed('双人床',4)
    #print(bed1)

    home.dianqi(bed1)

    home.__str__()