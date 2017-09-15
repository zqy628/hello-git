#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
杨辉三角形，也称帕斯卡三角，其定义为：顶端是 1,视为(row0).第1行(row1)(1&1)两个1,
这两个1是由他们上头左右两数之和 (不在三角形内的数视为0).依此类推产生第2行(row2):0+1=1;1+1=2;1+0=1.
第3行(row3):0+1=1;1+2=3; 2+1=3;1+0=1. 循此法可以产生以下诸行，如下图所示。
'''
def yanghui(n):
    yh_nums = [[1],[1,1]]
    for i in range(2,n):
        # print i
        yh_num = [1] #inside
        for j in range(1,i):
            yh_num.append(yh_nums[i-1][j-1] + yh_nums[i-1][j])
        yh_num.append(1)
        yh_nums.append(yh_num)
    for yh_num in yh_nums:
        for num in yh_num:
            print str(num) + '\t',
        print '\n'
    # print yh_nums
yanghui(100)


