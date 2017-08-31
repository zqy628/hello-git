#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
要求：
统计一部英文小说里单词的出现次数（忽略大小写）
按出现次数显示最高的 100 个单词
【附加题】多统计几个不同作家的作品，挑选一些特征词汇的次数画在图表上，展示不同作家的风格区别。
'''
#Counter方法直接可以计算词频！
from collections import Counter
import re
with open(ur"Aesop’s Fables伊索寓言.txt".encode('gbk'),'r') as fp:
    text = fp.read()
    fp.close()
letters = re.findall(r'\w+',text)
print Counter(letters).most_common(10)