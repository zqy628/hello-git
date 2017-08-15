#!/usr/bin/env python
# -*- coding: utf-8 -*-

#中文编码问题太烦了妈的

'''
今天就是在之前“查找文件”的基础上，增加对文件内容的检索。仍然是设定某个文件夹，不同的是要再增加一个文本参数，然后列出这个文件夹（含所有子文件夹）里，所有文件内容包括这个搜索文本的文件。
'''
import os
import fnmatch
import re
def find_contents(path,keywords):
    fileList = []
    files = os.walk(path)  # 使用os.walk（遍历包括子目录下所有文件），生成三组列表：当前目录地址当下前目录下的文件夹名（没有则返回一个空列表），当前目录的所有文件
    for path, dirnames, filenames in files:
        for file in filenames:
            if file.endswith('.txt'):
                filepath = "\\".join([path,file])
                print filepath
                with open(filepath,'r') as fp:
                    # response = fp.read().decode('gbk')
                    response = fp.read()
                    print response
                    if len(re.findall(keywords,response))>0:  #正则查找
                        fileList.append(filepath)
    return fileList

if __name__ == '__main__':
    root = r'F:\test'
    keywords = '2'
    lists = find_contents(root,keywords)
    if lists:
        for i in lists:
            print i + '存在'
    else:
        print 'Not Found!'
