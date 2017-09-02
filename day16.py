#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
所有囚犯排成一个圈，以某个人为起点从 1 开始报数，依次递增。所有报到奇数的犯人立刻离开，剩下的人继续往下报数。最后剩下的一个犯人获得假释。
那么，站在哪个位置，才能保证一站到底？
'''
print '一共多少囚犯？'
number = input()
prisoners = range(1,number+1)
num = 1 #从1开始报数
while len(prisoners) > 1:
    prisoners_copy = prisoners[:]
    for prisoner in prisoners:
        if num % 2 == 1:
            prisoners_copy.remove(prisoner)
        num += 1
    prisoners = prisoners_copy
    # print prisoners
print prisoners