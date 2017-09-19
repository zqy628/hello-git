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
    matrix[0][0] = 1
    # print matrix
    num = 1 #从1开始
    flag = 0 #转向标志
    i = 0
    j = 0
    while num < n*n:
        if flag % 4 == 0:
            while j+1 in range(n):
                if matrix[i][j+1] == 0:
                    j += 1
                    num += 1
                    # print i,j,num,flag
                    matrix[i][j] = num
                else:
                    break
            flag += 1

        elif flag % 4 == 1:
            while i+1 in range(n):
                if matrix[i+1][j] == 0:
                    i += 1
                    num += 1
                    # print i,j,num,flag
                    matrix[i][j] = num
                else:
                    break
            flag += 1
        elif flag % 4 == 2:
            while j-1 in range(n):
                if matrix[i][j-1] == 0:
                    j -= 1
                    num += 1
                    # print i,j,num,flag
                    matrix[i][j] = num
                else:
                    break
            flag += 1
        elif flag % 4 == 3:
            while i-1 in range(n):
                if matrix[i-1][j] == 0:
                    i -= 1
                    num += 1
                    # print i,j,num,flag
                    matrix[i][j] = num
                else:
                    break
            flag += 1
    print matrix
    for i in matrix:
        for j in i:
            print str(j) + '\t',
        print
matrix(10)