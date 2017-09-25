#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
python练习册 第0000题
PIL的一些用法：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
'''
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from random import *

# im = Image.open('test.jpg')
# w,h = im.size
# # im.thumbnail((w/2,h/2)) #缩小图片尺寸
# im2 = im.filter(ImageFilter.BLUR) #高斯模糊图片
# im2.save('test2.jpg','jpeg') #保存图片

def rndChar():
    return chr(randint(65,90))

def rndColor():
    return (randint(64,255),randint(64,255),randint(64,255))

def rndColor2():
    return (randint(32,127),randint(32,127),randint(32,127))

w,h = 240,60
image = Image.new('RGB',(w,h),(255,255,255))
# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in xrange(w):
    for y in xrange(h):
        draw.point((x,y),rndColor())
# 输入文字
for t in range(4):
    draw.text((60*t + 10, 10),rndChar(),rndColor2(),font)
image = image.filter(ImageFilter.BLUR)
image.save('test3.jpg','jpeg')