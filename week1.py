#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 脚本登陆器
# 挑一个你看得顺眼的网站，通过代码模拟登录请求，并获取登录状态。进而再模拟进行用户操作，如发表状态、留言、评论等。
# 模拟登录是自动抓取某些网站的必要步骤。

#模拟登陆微博：use selenium
from selenium import webdriver
import time
import pickle
import requests
# url = r'https://weibo.com/'
driver = webdriver.PhantomJS()

#设置浏览器窗口的位置和大小
driver.set_window_position(20, 40)
driver.set_window_size(1100,700)

#打开一个页面（QQ空间登录页）
driver.get('http://qzone.qq.com')
#登录表单在页面的框架中，所以要切换到该框架
driver.switch_to.frame('login_frame')
#通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('191155395')
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('b*b-4ac=0')
driver.find_element_by_id('login_button').click()
time.sleep(3)
print driver.current_url

#通过cookies登陆网页   成功！！！
request = requests.Session()
headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
request.headers.update(headers)
cookies = driver.get_cookies()
print cookies
#存储cookies
# with open('cookies.ini','w') as f:
#     pickle.dump(cookies,f)
#取回cookies
# with open('cookies.ini','r') as f:
#     pickle.load(f)
for cookie in cookies:
    print cookie
    request.cookies.set(cookie['name'], cookie['value'])
response = request.get('http://user.qzone.qq.com/191155395')
print response.url
print response.text

#找不到发表状态的element
# time.sleep(5)
# print 'ok'
# print driver.current_url
# if driver.current_url == 'https://user.qzone.qq.com/191155395':
#     print 'ook'
#     driver.find_element_by_xpath(".//div[@id='$1_substitutor_content']").clear()
#     timeNow = time.localtime()
#     driver.find_element_by_xpath(".//div[@id='$1_substitutor_content']").send_keys(str(timeNow))
#     driver.find_element_by_class_name('btn-post gb_bt  evt_click').click()
# else:
#     print 'ouch'
#do something….
#退出窗口
# driver.quit()