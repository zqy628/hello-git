#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
如果一个正整数等于其各个数字的立方和，则称该数为阿姆斯特朗数（亦称为自恋数、自幂数）。

写一段代码，输出 1000 以内的所有阿姆斯特朗数。

附加题：输入一个正整数，输出距离它最近的阿姆斯特朗数。
'''
from math import pow
def judge_arms(num):
        sum = 0
        for j in str(num):
            sum += pow(int(j),len(str(num)))
        if sum == num:
            print num
            return True

def near_arms(n):
    if judge_arms(n):
        print n
    i,j = n-1,n+1
    while True:
        if judge_arms(i):
            # print i
            break
        elif judge_arms(j):
            # print j
            break
        else:
            i -= 1
            j += 1

for i in range(10,1001):
    judge_arms(i)

near_arms(100000)