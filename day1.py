# -*- coding: utf-8 -*-
#从1~n中，随机取m个数。1<=m<=n
import random
print '设置抽取的最大数值：'
n = input()
print '设置抽取的数量：'
m = input()
number = []
for i in range(n):
    number.append(i+1)
print number
choose = random.sample(number,m)
print choose
#以下是坑，没考虑重复
# for j in range(m):
#     choose = random.choice(number)
#     del number[choose-1]
#     print choose

#简便方法
print random.sample(range(1,n+1),m)

