# -*- coding: utf-8 -*-

# 把一段字符串用“右起竖排”的古文格式输出，并且拿竖线符号作为每一列的分割符。
# 比如这段文字：
# "静夜思 李白 床前明月光，疑似地上霜。举头望明月，低头思故乡。"
# 输出结果：
# 低┊举┊疑┊床┊静
# 头┊头┊似┊前┊夜
# 思┊望┊地┊明┊思
# 故┊明┊上┊月┊
# 乡┊月┊霜┊光┊李
# 。┊，┊。┊，┊白
'''
        没有解决题目和诗句不等长的问题
        1.title比句子短：题目作者中间加空格
        2.反之：题目作者分两行？（还是不能解决全部。。。
        更新：已解决不等长问题
            非四言诗如何解决？（将诗句存入列表---已解决
            词呢？词句子不等长。。。艰难。。。
        再次更新：已解决！！！异常抛出处理解决哈哈哈哈！
        最终版本！
        还是要有个更新。。。：不用区分题目还是诗句长的。。。大量减少代码
        最终终版本！！
'''
import re
# poem = '天净沙·秋思 马致远 枯藤老树昏鸦，小桥流水人家，古道西风瘦马。夕阳西下，断肠人在天涯。'
poem = file('poem').read()
sentense = re.findall(ur'[\u4e00-\u9fa5·]+[？！，。：；、]?',poem.decode('utf-8'))
# print sentense
# print len(sentense)
fenge = '┊'.decode('utf-8')
maxlen = 0

for s in range(2,len(sentense)):
    if len(sentense[s]) > maxlen:
        maxlen = len(sentense[s])
lenth = max(len(sentense[0]),maxlen)#比较题目诗句长度
# print lenth
# if lenth == len(sentense[0]):#题目长
#     title = sentense[0]
#     author = sentense[1] + ' ' * (lenth - maxlen)
#     for i in range(maxlen):
#         if author[i] != ' ':#都有字
#             print title[i] + fenge + author[i] + fenge,
#             for j in range(2,len(sentense)):
#                 print sentense[j][i] + fenge,
#             print
#         else:
#             print title[i] + fenge + '   ' + author[i]
#     for j in range(maxlen,lenth):
#         print title[j] + fenge
# elif lenth == maxlen:#诗句长
title = sentense[0] + ' ' * (lenth - len(sentense[0]))
author = sentense[1] + ' ' * (lenth - len(sentense[1]))
# title = sentense[0]
# author = sentense[1]
for i in range(lenth):
    if title[i] != ' ' and author[i] != ' ':#标题作者都有字
        for j in range(2,len(sentense))[::-1]:
            try:
                print sentense[j][i] + fenge,
            except:
                print '    ',
        print author[i] + fenge + title[i] + fenge,
        print
    elif title[i] != ' ' and author[i] == ' ':#标题有字作者没字
        for j in range(2,len(sentense))[::-1]:
            try:
                print sentense[j][i] + fenge,
            except:
                print '    ',
        print author[i] + '   ' + title[i] + fenge,
        print
    elif title[i] == ' ' and author[i] != ' ':#作者有字标题没字
        for j in range(2,len(sentense))[::-1]:
            try:
                print sentense[j][i] + fenge,
            except:
                print '    ',
        print author[i] + fenge + title[i] + fenge,
        print
    else:
        for j in range(2,len(sentense))[::-1]:
            try:
                print sentense[j][i] + fenge,
            except:
                print '    ',
        # print author[i] + fenge + title[i] + fenge,
        print


