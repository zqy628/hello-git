#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
设定一个长度为 N 的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值。

附加题：
输入的数字串可以重新打乱排列，比如输入 123 ，打乱排列之后会有 132，213，231，312，321 等情况，其他条件不变，求最大值。
'''
import itertools
def question1(N):
    maxN = 0
    for i in range(1,len(str(N))):
        multi = int(str(N)[:i]) * int(str(N)[i:])
        if multi > maxN:
            # multi_num = [int(str(N)[:i]),int(str(N)[i:]]
            maxN = multi
    return maxN
def question2(N):
    numbers = itertools.permutations(str(N))
    maxN = 0
    for number in numbers:
        N = ''.join(number)
        for i in range(1, len(str(N))):
            multi = int(str(N)[:i]) * int(str(N)[i:])
            if multi > maxN:
                # multi_num = [int(str(N)[:i]),int(str(N)[i:]]
                maxN = multi
    return maxN


print question1(123456)
print question2(123456)