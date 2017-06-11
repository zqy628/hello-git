# -*- coding: utf-8 -*-
# 制作一个骰子游戏：假想有3个6面骰子，可以掷出3~18的数，
# 其中3~10为小，11~18为大。起始为100分，每掷一次之前先押注，
# 可押大小或数字，可重复下注。掷出结果后，押中大小，所押分数翻倍返还；
# 押中数字，所押分数10倍返还。
# 增加电脑玩家，同你一起进行游戏(未实现）
import random

f = file('fen','r')
fenshu = int(f.read())
f.close()
# fenshu = 100
def tou():
    num1 =  random.randint(1,7)
    num2 =  random.randint(1,7)
    num3 =  random.randint(1,7)
    return num1+num2+num3

def bm(fenshu,gamefen):#比大小
    # global gamefen
    print '选择大小：1.大，2.小'
    choice = input()
    print '最终点数：%d'%tou()
    if choice == 1:
        if tou()>10:
            print 'you win！'
            fenshu += 2*gamefen
            print fenshu
        else:
            print 'you lost'
    if choice == 2:
        if tou()<10:
            print 'you win！'
            fenshu += 2*gamefen
            print fenshu
        else:
            print 'you lost'
    return fenshu
def number(fenshu,gamefen):#猜数字
    print '选择点数：3-18'
    choice = input()
    print '最终点数：%d' % tou()
    if choice==tou():
        fenshu += 10 * gamefen
    else:
        print 'you lost'
    return fenshu

print '***骰子游戏***'
while True:
    print '你当前剩余积分为%d，请输入你要投入的分数：'%fenshu
    gamefen = input()
    if fenshu - gamefen<0:
        print '对不起，您当前积分不足'
    else:
        fenshu -= gamefen
        break
while True:
    print '选择模式：1.猜大小 2.猜数字'
    choice = input()
    if choice == 1:
        fenshu = bm(fenshu,gamefen)
        break
    if choice == 2:
        fenshu = number(fenshu,gamefen)
        break
    else:print '请选择\'1\'或\'2\''


print '游戏结束，你当前积分为%d'%fenshu
f = file('fen','w')
f.write(str(fenshu))
f.close()


