#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
罗马数字采用七个罗马字母作数字、即 I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。

给定一个小于 3999 的罗马数，将其转换为整数，例如：Ⅲ=3、Ⅳ=4、Ⅵ=6、XIX=19、XX=20、XLV=45、MCMLXXX=1980。
附加题：
给定一个小于 3999 整数，将其转换为罗马数。
'''
# 罗马数字转整数
def romanToInt(s):

    d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res, p = 0, 'I'
    # 逆序逐一遍历
    # 使用逆序的好处在于，每次只需对一位罗马数字进行加或减的操作
    # 使用顺序的话，可能为两位
    for c in s[::-1]:
        if d[c] < d[p]:
            res = res - d[c]
        else:
            res = res + d[c]
        p = c

    return res

# 整数转罗马数字
def intToRoman(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

    # 迭代依次处理每位数字
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num %= values[i]
        i += 1
    return res

print intToRoman(3789)