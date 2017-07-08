# -*- coding: utf-8 -*-

# 查询当前正在热映的电影。方法是，找一个电影网站（豆瓣电影、时光网、格瓦拉等等），
# 把它的首页取过来，分析一下网页内容的结构，然后从中取出你要的信息。
# 因为一个网页上会包含很多内容，如何查找定位到你所需的内容，还是要费点功夫的。
# 你可能会用到正则表达式、urllib，或者BeautifulSoup之类的。
import re
import urllib2
import bs4
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://movie.douban.com/').read()
# print html
#提取豆瓣热映内容
soup = BeautifulSoup(html,'lxml')
# print soup
div_hot = soup.find('ul',class_="ui-slide-content")
# print div_hot
# for i in div_hot.find_all('li', class_='title'):
#     movie_title = i.a.get_text()
#     movie_title = movie_title.strip() #去除movie_title两边的空格
#     print movie_title
print '正在热映：'
for child in div_hot.children:
    if type(child)==(bs4.element.Tag):
        if child.has_attr('data-title'):
            print child['data-title']
# print div_hot
# contents = soup.select(' div.screening-bd > ul > li')
# print len(contents)
# print contents