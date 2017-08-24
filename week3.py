#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
做一个可以用来记账的小程序
就在控制台下，可以输入收支数额和名目。程序会记录下每笔收支。之后可以查询余额和之前的收支明细。

举个例子：
> python account.py
选择操作：
记账
查余额
收支明细
'''
import os
import datetime
class Notebook(object):
    def __init__(self):
        print '''
***欢迎进入记账本***
操作编号：
1.记账
2.查余额
3.收支明细
0.退出
'''
        while True:  #break和continue用的绝妙
            choose = self.choose()
            if choose == '1':
                self.accounting()
            elif choose == '2':
                self.balance()
            elif choose == '3':
                self.details()
            elif choose == '0':
                break
            else:
                print '请输入正确的编号'
                continue

    def choose(self):
        print '请选择操作：'
        choose = raw_input()
        return choose

    def accounting(self):
        print '请选择1.支出 2.进账：'
        while True:
            select = raw_input()
            if select == '1':
                print '支出金额：'
                while True:
                    try:
                        currentSpend = input()
                        break
                    except:
                        print '请输入数字'
                        continue
                if os.path.isfile('balance.txt'):
                    with open('balance.txt','rb') as fp:
                        money = fp.read()
                        money = int(money)
                        fp.close()
                    with open('balance.txt','wb') as fp:
                        money -= currentSpend
                        fp.write(str(money))
                        fp.close()
                else:
                    with open('balance.txt', 'w+') as fp:
                        money = -currentSpend
                        fp.write(str(money))
                        fp.close()
                print '支出名目：'
                content = raw_input()
                now = datetime.datetime.now()  # 当前日期
                current_time = now.strftime('%Y-%m-%d')  # str格式
                with open('account.txt','a') as f:
                    f.write(current_time + '\t支出' + str(currentSpend) + '\t' + content + '\n')
                    f.close()
                break
            elif select == '2':
                print '收入金额：'
                while True:
                    try:
                        currentIncome = input()
                        break
                    except:
                        print '请输入数字'
                        continue
                if os.path.isfile('balance.txt'):
                    with open('balance.txt','rb') as fp:
                        money = fp.read()
                        money = int(money)
                        fp.close()
                    with open('balance.txt','wb') as fp:
                        money += currentIncome
                        fp.write(str(money))
                        fp.close()
                else:
                    with open('balance.txt', 'w+') as fp:
                        money = currentIncome
                        fp.write(str(money))
                        fp.close()
                print '收入名目：'
                content = raw_input()
                now = datetime.datetime.now()  # 当前日期
                current_time = now.strftime('%Y-%m-%d')  # str格式
                with open('account.txt','a') as f:
                    f.write(current_time + '\t收入' + str(currentIncome) + '\t' + content + '\n')
                    f.close()
                break
            else:
                print '请输入正确的编号'
                continue

    def balance(self):
        try:
            with open('balance.txt', 'r') as fp:
                print '余额：'+fp.read()
        except:
            print '还不存在账户数据'

    def details(self):
        try:
            with open('account.txt', 'r') as fp:
                print fp.read()
        except:
            print '还不存在账户数据'

if __name__ == '__main__':
    nb = Notebook()