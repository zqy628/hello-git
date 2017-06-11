# -*- coding: utf-8 -*-

# 有一个字符串
# text = "aAsmr3idd4bgs7Dlsf9eAF"
#
# 请将text字符串中的数字取出，并输出成一个新的字符串。
import re
text = "aAsmr345idd4bgs7Dlsf9eAF546.46"
str1 = re.findall(r'[\d|.]+',text)
str2 = ''
print str1
for i in str1:
    str2 += i
print str2