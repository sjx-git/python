import os
from multiprocessing import Pool,Manager
#将旧文件夹中的内容，拷贝到新的文件夹中
def newfiles(filename,oldfile,newfile):
    fr = open(oldfile+'/'+filename,'r')
    context = fr.readlines()
    fw = open(newfile+'/'+filename,'w')
    fw.write(context)

    fw.close()
    fr.close()


def main():
    #获取当前所出文件夹路径
    pwd = os.getcwd()

    #列出当前文件夹下的所有文件
    listdir  = os.listdir()

    #输入要被copy的文件夹名称
    oldfile  = input('输入要创建的文件夹：')

    #新的文件夹名称
    newfile = pwd+'/..'+'/'+oldfile+'复件'
    os.mkdir(newfile)

    #设置多线程，完成文件的拷贝功能
    p = Pool(3)
    queue = Manager().Queue()
    for i in listdir:
        p.apply_async(newfiles,args=(i,pwd,newfile))
        queue.put(i)
    y = 1
    for i in range(queue.qsize()):
        print('第%d次获取的文件名为：%s'%(y,queue.get()))
        y +=1

    p.close()
    p.join()

if __name__ == '__main__':
    main()