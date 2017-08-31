#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
给你一个正整数n， 编程求所有这样的五位和六位十进制回文数，满足各位数字之和等于n(5<=n<=54)。 按从小到大的顺序输出满足条件的整数。
'''
import time
startTime = time.time()
# print startTime
print '需满足的各位数之和：'
sumInput = input()
num_1 = []

for num in range(10000,1000000):
    sum = 0
    lenth = len(str(num))
    i =0
    j = lenth-1
    while i <= j:
        if str(num)[i] == str(num)[j]:
            i += 1
            j -= 1
            if i > j:
                num_1.append(num)
        else:
            break
num_2 = []
for num in num_1:
    sum = 0
    for digital in str(num):
        sum += int(digital)
    if sum == sumInput:
        num_2.append(num)
stopTime = time.time()
time = stopTime - startTime
print num_1
print len(num_1)
print num_2
print len(num_2)
print time

'''
别人简洁版代码
def Palindrome(n):
    for i in range(10000, 1000000):
        number = list(str(i))
        #使用reversed把列表进行反向迭代， eval求值连接后的字符串
        if number == list(reversed(number)) and eval('+'.join(number)) == n:
            print(i)
Palindrome(52)
'''