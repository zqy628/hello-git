#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
基本要求：

需要输入邮箱地址、密码两项
邮箱地址需要满足形如 xxx@xxx.xx 的正常邮件格式（中间有一个 @，后半段中间至少有一个 .），并且不包含空格
密码需要8位以上，必须包含有大写字母、小写字母和数字三种字符（三种都要有）
附加要求：

通过正则表达式来验证规则
增加重名验证
'''
import re
import cPickle
print '欢迎注册邮箱'
# address = raw_input('邮箱地址：')
try:
    with open('email1.pkl','rb') as f:
        emails = cPickle.load(f)
        print 'had data'
except:
    emails = []
while True:
    address = raw_input('邮箱地址：').decode('utf-8')
    if address in emails:
        print '此地址已注册'
        continue
    elif ' ' in address:
        print '邮箱地址需要满足形如 xxx@xxx.xx 的正常邮件格式，并且不包含空格'
        continue
    elif not re.search('\S+@{1}[a-z0-9]+.[a-z]+',address):
        print '邮箱地址需要满足形如 xxx@xxx.xx 的正常邮件格式，并且不包含空格'
        continue
    else:break
while True:
    password = raw_input('密码：')
    if len(password) > 8 and re.search('[A-Z]+',password) and re.search('[a-z]+',password) and re.search('\d+',password):
        break
    else:
        print '密码需要8位以上，必须包含有大写字母、小写字母和数字三种字符（三种都要有）'
        continue
print 'Congratulation注册成功！'
emails.append(address)
print emails
with open('email1.pkl','wb') as f:
    cPickle.dump(emails,f)