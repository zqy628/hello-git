# -*- coding: utf-8 -*-

#从控制台输入或从文件中读入一段文本，统计出其中每个字符出现的次数，并按照出现次数排序输出。

str1 = 'History is his story.'
times = {}
for i in str1:
    if i != ' ':
        if i in times:
            times[i] += 1
        else:
            times[i] = 1

print sorted(times.iteritems(),key=lambda k:k[1],reverse=True)