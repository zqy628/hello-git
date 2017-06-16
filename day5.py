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
import re
poem = '静夜思 李白 床前明月光，疑似地上霜。举头望明月，低头思故乡。'
sentense = re.findall(ur'[\u4e00-\u9fa5]+',poem.decode('utf-8'))
title = sentense[0]+' '+sentense[1]
# print title
sentense1 = sentense[2]+'，'.decode('utf-8')
sentense2 = sentense[3]+'。'.decode('utf-8')
sentense3 = sentense[4]+'，'.decode('utf-8')
sentense4 = sentense[5]+'。'.decode('utf-8')
lenth = max(len(title),len(sentense1))
fenge = '┊'.decode('utf-8')
# print lenth
for i in range(lenth):
    print title[i]+fenge+sentense1[i]+fenge+sentense2[i]+fenge+sentense3[i]+fenge+sentense4[i]