#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
双色球由红球和蓝球两部份组成，从33个红球号码(01~33)中选择6个，再从16个蓝球号码(01~16)中选择1个。开奖时，在红色球中随机摇出六个红号，在蓝色球中随机摇出一个蓝号
要求：

生成一组或多组彩票号码
附加题1：模拟开奖结果，用你自己手选的号码，去计算中奖的概率
附加题2：加入购买费用（2元一注）和奖金返还，算算看你玩一百年彩票能赚（kui）多少钱

'''
import random
# print random.choice(range(1,4))
class DcBall(object):
    def __init__(self):
        self.money = 30000
        chooseNumber = self.chooseNumber()
        print chooseNumber
        i = 0
        while i < 15600:
            lotteryNumber = self.lotteryNumber()
            # print lotteryNumber
            self.money = self.result(lotteryNumber,chooseNumber)
            i += 1
        print '最后余额：',self.money
    def lotteryNumber(self):
        redBall = random.sample(range(1,34),6)
        # print '红色开奖球为：',redBall
        blueBall = random.choice(range(1,17))
        # print '蓝色开奖球为：',blueBall
        lotteryNumber = redBall
        lotteryNumber.append(blueBall)
        # print lotteryNumber
        return lotteryNumber

    def chooseNumber(self):
        print '请挑选6个红色球:'
        chooseBall = []
        for i in xrange(6):
            print '请选择第%d个球的号码'%(i+1)
            chooseBall.append(input())
        print '请挑选1个蓝色球:'
        chooseBall.append(input())
        return chooseBall

    def result(self,lottery,choose):
        redMacth = []
        for red_l in lottery[:6]:
            for red_c in choose[:6]:
                if red_l == red_c:
                    redMacth.append(red_l)
        if lottery[6] == choose[6]:
            if len(redMacth)==6:
                self.money += 10000000-2
                print lottery,
                print '+10000000'
            elif len(redMacth)==5:
                self.money += 3000-2
                print lottery,
                print '+3000'
            elif len(redMacth)==4:
                self.money += 200-2
                print lottery,
                print '+200'
            elif len(redMacth)==3:
                self.money += 10-2
                print lottery,
                print '+10'
            elif (len(redMacth)==2 or len(redMacth)==1 or len(redMacth)==0):
                self.money += 5-2
                print lottery,
                print '+5'
            else:
                self.money -= 2
        else:
            if len(redMacth)==6:
                self.money += 5000000-2
                print lottery,
                print '+5000000'
            elif len(redMacth)==5:
                self.money += 200 - 2
                print lottery,
                print '+200'
            elif len(redMacth)==4:
                self.money += 10 - 2
                print lottery,
                print '+10'
            else:
                self.money -= 2
        return self.money

if __name__ == '__main__':
    db = DcBall()