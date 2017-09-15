#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
哥德巴赫在 1742 年给欧拉的信中提出了以下猜想：任一大于 2 的整数都可写成三个质数之和。
（因现今数学界已经不使用“1 也是质数”这个约定，原初猜想的现代陈述为：任一大于 5 的整数都可写成三个质数之和。）
欧拉在回信中也提出另一等价版本，即任一大于 2 的偶数都可写成两个质数之和。今日常见的猜想陈述为欧拉的版本。
'''
# 实现一段代码，输入一个大于 2 的偶数 k，输出两个质数 m、n，满足 m + n == k。
import math
def goldbach(n):
    for i in range(2,n/2+1):
        j = n - i
        if isPrime(i) and isPrime(j):
            print '{0} = {1} + {2}'.format(n,i,j)

def isPrime(num):
    maxC = int(math.sqrt(num))
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3,maxC+1,2):
            if num % i == 0:
                return False
        return True

goldbach(1950)