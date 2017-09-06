#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
十分钟之后，韩信带着 10000 金币和纠结，来到了神秘的古老商店，他仅有如下装备选择：

影忍之足             690
巨人之握             1500
破甲弓                 2100
泣血之刃             1740
无尽战刃             2140
贤者的庇护         2080

在不考虑装备重复的情况之下，即可以多次购买一件装备，要填满六格物品栏，有多少种购买方式？写一个程序，输出所有可行的购买组合。
附加题：
1、如果没有6格物品栏限制，有多少种购买方式？
2、在 1 的前提下，影忍之足最多购买一次，现在有多少种购买方式？
'''

'''
import itertools
# 装满 6 格，金额小于 10000
equipment = [690,1500,2100,1740,2140,2080]
def func():
    iter = itertools.combinations_with_replacement(equipment,6)
    count = 0
    for i in iter:
        if sum(i) <= 10000:
            print(i)
            count += 1
    return count
print(func())

'''
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import combinations, product
import itertools

items = [
    {'name':'影者之足','price':'690'},
    {'name':'巨人之握','price':'1500'},
    {'name':'破甲弓','price':'2100'},
    {'name':'泣血之刃','price':'1740'},
    {'name':'无尽战刃','price':'2140'},
    {'name':'贤者的庇护','price':'2080'},
]


'''

在不考虑装备重复的情况之下，即可以多次购买一件装备，要填满六格物品栏，

有多少种购买方式？写一个程序，输出所有可行的购买组合。

'''

def one(items, bound):
    count = 0
    for p in combinations_with_replacement(items, 6):
        sum_price = []
        for f in p:
            sum_price.append(int(f['price']))
        if sum(sum_price) < bound:
            count += 1
            print(p, '总计金额：%s' % sum(sum_price))

    print('总共有%s种购买方式' % count)



'''

如果没有6格物品栏限制，有多少种购买方式？

'''

def two(item, bound):
    price_list = []
    for price in item:
        price_list.append(int(price['price']))
    max_length = bound // min(price_list)
    count = 0
    for n in range(1, max_length+1):
        for c in itertools.combinations_with_replacement(price_list,n):
            if sum(c) <= bound:
                count += 1
                print('+'.join(map(str, c)))
    print('共有%s种购买方式' %count )


'''

在 1 的前提下，影忍之足最多购买一次，现在有多少种购买方式？

'''

def three(item, bound):
    price_list = []
    for price in item:
        price_list.append(int(price['price']))
    max_length = bound // min(price_list)
    count = 0
    for n in range(1, max_length+1):
        for c in itertools.combinations_with_replacement(price_list,n):
            if sum(c) <= bound:
                string = '+'.join(map(str, c))
                if string.count('690') <= 1:
                    count += 1
    print('共有%s种购买方式' %count )

three(items,10000)