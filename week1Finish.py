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
driver = webdriver.Chrome()

#设置浏览器窗口的位置和大小
driver.set_window_position(20, 40)
driver.set_window_size(1440,900)

#打开一个页面
driver.get('https://weibo.com/')
time.sleep(10)
#登录表单在页面的框架中，所以要切换到该框架
# driver.switch_to.frame('login_frame')
#通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_link_text('登录').click()
# time.sleep(2)
# driver.switch_to.window('')
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('15608058020')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('zqy191155395')
time.sleep(0.5)
driver.find_element_by_class_name('W_btn_a').click()
time.sleep(3)
driver.find_element_by_css_selector('.input textarea ').clear()
moment = time.localtime()
driver.find_element_by_css_selector('.input textarea').send_keys(str(moment))
driver.find_element_by_link_text('发布').click()
print driver.current_url