#!/usr/bin/env python
# -*- coding: gbk -*-

#���ı�������̫�������

'''
���������֮ǰ�������ļ����Ļ����ϣ����Ӷ��ļ����ݵļ�������Ȼ���趨ĳ���ļ��У���ͬ����Ҫ������һ���ı�������Ȼ���г�����ļ��У����������ļ��У�������ļ����ݰ�����������ı����ļ���
'''
import os
import fnmatch
import re
def find_contents(path,keywords):
    fileList = []
    files = os.walk(path)  # ʹ��os.walk������������Ŀ¼�������ļ��������������б���ǰĿ¼��ַ����ǰĿ¼�µ��ļ�������û���򷵻�һ�����б�����ǰĿ¼�������ļ�
    for path, dirnames, filenames in files:
        for file in filenames:
            if file.endswith('.txt'):
                filepath = "\\".join([path,file])
                print filepath
                with open(filepath,'r') as fp:
                    # response = fp.read().decode('gbk')
                    response = fp.read()
                    print response
                    if re.search(response,keywords):
                        fileList.append(filepath)

if __name__ == '__main__':
    root = r'F:\test'
    keywords = r'te'
    lists = find_contents(root,keywords)
    if lists:
        for i in lists:
            print i
    else:
        print 'Not Found!'
