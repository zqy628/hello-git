#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
现有一个 m × n (m,n 都小于 100)的网格，位于左上角的 A 要去寻找右下角的 B，A 只能向下或者向右行走，
现在问题来了，按照刚才的规则，A 到达 B 一共有多少种不重复的路径？
'''
#  转化成一个组合问题，C(m+n-2,m-1)
from math import factorial
def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''
    # your code here
    return factorial(m+n-2)/(factorial(n-1)*factorial(m-1))

print uniquePath(5,6)
assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900

# 从右下倒推回左上，每个点的路径数都是它右边和下边的路径数之和。
# 递归来做
def uniquePath1(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return uniquePath(m, n-1) + uniquePath1(m-1, n)

print uniquePath1(10,20 )

#迭代来做比较麻烦！
def uniquePath2(m, n):
    matrix = [[1 for i in range(n)]for j in range(m)]
    # print matrix
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[-1][-1]

print uniquePath2(5, 6)