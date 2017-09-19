#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
在一个宾馆里住着六个不同国籍的人，他们分别来自美国、德国、英国、法国、俄罗斯和意大利。他们的名字叫 A、B、C、D、E、F。名字的顺序与上面的国籍不一定相互对应。

A 和美国人是医生
E 和俄罗斯人是教师
C 和德国人是技师
B 和 F 曾经当过兵，而德国人从未参过军
法国人比 A 年龄大，意大利人比 C 年龄大
B 同美国人下周要去西安旅行，而 C 同法国人下周要去杭州度假
通过上述描述，判断 A、B、C、D、E、F 各是哪国人？
'''
from itertools import *
# count = 0
for i in permutations(['US','GER','ENG','FRA','RUS','ITA'],6):
    if i[0] in 'USRUSGER' or i[2] in 'USRUSGER' or i[4] in 'USRUSGER':
        # count += 1
        # print i
        continue
    elif i[1] == 'GER' or i[5] == 'GER':
        continue
    elif i[0] == 'FRA' or i[2] == 'ITA':
        continue
    elif i[1] == 'US' or i[2] == 'FRA':
        continue
    print i
# print count