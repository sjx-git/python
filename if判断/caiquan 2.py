import random


class caiqan():
    def caiquan(self):
        player = int(input('请输入 0拳头 1剪刀 2布：'))
        computer = random.randint(0, 2)  # 随机生成括号中范围的数
        if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
            print('获胜')
        elif player == computer:
            print('平局')
        else:
            print('输了')


if __name__ == '__main__':
    caiqan().caiquan()
