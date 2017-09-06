#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
https://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166445&idx=1&sn=90890a143ecce91d761d90dd8dc479ed&chksm=be4b59d5893cd0c32d604ba1e23af9e1f20ed0cde09f2daad5d72ca3f6969f4bbde954f52c17&scene=21#wechat_redirect
田忌赛马
现在将马分为 优、上、中、下、劣 五等，五局三胜制，抽象为列表[2,4,6,8,10] 与 [1,3,5,7,9] ，其他条件不变，计算出田忌有多少种赢得比赛的可能。
齐王顺序不变
'''
from itertools import *
def saima():
    qiwang = [10,8,6,4,2]
    tianji = [1,3,5,7,9]
    tianji_ = list(permutations(tianji))
    saima = []
    for tj in tianji_:
        saima.append(zip(qiwang,tj))
    win_ = 0
    for sm in saima:
        win = 0
        for sm_ in sm:
            if sm_[0] < sm_[1]:
                win += 1
        if win >= 3:
            win_ += 1
            print sm
    print win_
saima()