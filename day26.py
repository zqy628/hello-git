#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
输入一个正整数 N，输出以 N 为边长的螺旋矩阵。（比如上图就是 N 为 4 的结果）
'''
def matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    num = 1 #从1开始
    flag = 0 #转向标志
    i,j = 0
    if flag % 4 == 0:
        for m in range(n)
# print matrix
matrix(4)