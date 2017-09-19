#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
给定一个 N * N 的矩阵（N >= 0），将其顺时针旋转 90°．输出处理之后的矩阵。

附加要求
在不创建新矩阵的情况下做变换，即所有的修改都在原矩阵上直接进行。
'''
'''
创建新矩阵
'''
# def ratate(mt):
#     l = len(mt)
#     # print l
#     matrix = []
#     for i in range(l):
#         matrix.append([])
#         for j in range(l):
#             matrix[i].append(0)
#     # print matrix
#     for m in range(l):
#         for n in range(l):
#             matrix[n][m] = mt[l-1-m][n]
#     return matrix
# m1 = [[]]
'''
不创建新矩阵
'''
def ratate(mt):
    l = len(mt)
    for i in range(l/2):
        for j in range(i,l-1-i):
            mt[i][j],mt[j][l-1-i],mt[l-1-i][l-1-j],mt[l-1-j][i] = mt[l-1-j][i],mt[i][j],mt[j][l-1-i],mt[l-1-i][l-1-j]
    return mt
m2 = [[1]]
m3 = [[i for i in range(3)] for j in range(3)]
m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# assert ratate(m1) == [[]]
#assert函数为判真函数
assert ratate(m2) == [[1]]
# assert ratate(m3) == [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
# assert ratate(m4) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
print ratate(m3)
print ratate(m4)