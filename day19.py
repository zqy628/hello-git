#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
乒乓序列从1开始计数，并且始终向上或向下计数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
'''
#定义一个函数 pingpong ，传入一个正整数参数 n ，返回第 n 个乒乓数

def pingpong(n,k =7):
    flag = 1
    i = 1 #计算第几个乒乓数
    num = 1 #从1开始数数
    pingpong_ = []
    while i <= n:
        pingpong_.append(num)
        if (i % k == 0) or ('k' in str(i)):
            flag *= -1
        num += flag
        i += 1
    print pingpong_

pingpong(10)
