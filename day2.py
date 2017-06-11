# -*- coding: utf-8 -*-

# 今天的坑：从一组数据中去除掉重复的元素，并将其排序输出。比如：
# 4, 7, 3, 4, 1, 9, 8, 3, 7
# 输出结果：
# 1, 3, 4, 7, 8, 9

print '输入一组数据：'  #set方法贼简单啊啊啊啊啊啊啊！set(list)
list = raw_input()
num = []
for k in range(len(list)):
    num.append(int(list[k]))
len1 = len(num)
num1 = num[:]

for i in range(len1 - 1):
    for j in range(i + 1, len1):
        # print num[i], num[j]
        if num[j] == num[i]:
            num1[j] = 0
# for n in range(len(num1)):
#     if num1[n] == 0:

dellist = []
for i in num1:
    if i == 0:
        dellist.append(i)
for i in dellist:
    print i
    num1.remove(i)

# num1.remove('0')
print sorted(num1)
