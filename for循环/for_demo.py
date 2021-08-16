'''
    in后面跟的是一个序列，如列表、元组、字符串,字典
    序列都有一个特征，就是可以进行索引操作

'''
class maopao():
    def maopao_demo(self):
        # a = [22,11,55,6,8,9,58]
        # #此处用range是因为，单纯的 len是个数字，不能遍历,此外 需要遍历的轮数是 len(a)-1
        # for i in range(len(a)-1):
        #     #每轮中，是比较了len(a) - i次
        #     for j in range(0,len(a)-i-1):
        #         if a[j] < a[j+1]:
        #             a[j],a[j+1] = a[j+1],a[j]
        # print(a)

        #面试题 组成【***%%%】 第一种办法
        # a = ['*','%','*','%','*','%','*','*','%']
        # a.sort(reverse=True)
        # print(a)

        #面试题 组成【***%%%】 第二种办法
        a = ['*','%','*','%','*','%','*','*','%']
        #此处用range是因为，单纯的 len是个数字，不能遍历,此外 需要遍历的轮数是 len(a)-1
        for i in range(len(a)-1):
            #每轮中，是比较了len(a) - i次
            for j in range(0,len(a)-i-1):
                if a[j] < a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
        print(a)

if __name__ == '__main__':
    maopao().maopao_demo()