#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 mongoDB 非关系型数据库中。
'''
#激活码：8位数字大写字母随机组合
import string
import random
import pymongo
#保存在mongoDB中
MS = {
    # 'server': '10.80.94.84',
    'server': 'localhost',
    'port':37215,
    'db': 'dailywork',
    'collection': 'codes',
    'user': 'zqy',
    'password': '191155395'
}
letters = string.ascii_uppercase + string.digits
def code():
    #无查重，需要时可以添加列表查重，while循环
    for i in xrange(200):
        code =  ''.join([random.choice(letters) for i in xrange(8)]) #浓缩代码
        # 验证连接数据库
        client = pymongo.MongoClient(MS['server'], MS['port'])
        MS_database = client[MS['db']]
        MS_database.authenticate(MS['user'], MS['password'], source='admin')
        if not MS_database['codes'].find_one({"code": code}):  # 新建站点表,增加查重
            MS_database['codes'].insert_one(
                {"code": code})
code()