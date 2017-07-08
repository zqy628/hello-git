#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。
'''
import os
def findTxts(path):
    fileList = []
    files = os.walk(path) #使用os.walk（遍历包括子目录下所有文件），生成三组列表：当前目录地址当下前目录下的文件夹名（没有则返回一个空列表），当前目录的所有文件
    for path,dirnames,filenames in files:
        for file in filenames:
            if file.endswith('.txt'):
                # print path,filenames
                fileList.append(file)
    return fileList

if __name__ == '__main__':
    path = r'F:\test'
    lists = findTxts(path)
    for filename in lists:
        print filename
