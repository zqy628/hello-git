#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
通过python去定时刷新某些网页，当有关注的信息更新时，发送提示。
基本思路：
分析你要抓取的页面，找出要关注的信息在哪里，可以通过怎样的方式来监测。是用BeautifulSoup还是正则表达式，还是直接字符串搜索就可以解决。以查询余票为例，就是找到记录剩余票数的字段，去判断数值。
设定固定时间间隔去请求页面，做好配置，确保能够得到有效返回，且不会因为太明显的机器行为而被屏蔽。很多网站需要你在header里提供一些必要参数才会理你。
当得到预期结果时，发送通知。我通常采取的方式时，在服务器上运行脚本，然后发送邮件通知。另一种可行的方法是在本地运行，得到结果后通过发出声音之类的方式提醒。
注意记录日志，以及异常情况的处理和提示，避免默默等了很久，其实都没有正常运行。

在Web应用中经常会遇到frame/iframe 表单嵌套页面的应用，WebDriver 只能在一个页面上对元素识别与定位，对于frame/iframe 表单内嵌页面上的元素无法直接定位。
这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe 表单的内嵌页面中。
'''

#写个思路：写一个脚本定时运行。
#脚本内容：打开指定页面，取出页面内容，然后找到制定信息。
#需要提醒时，selenium登陆邮箱发送邮件

#监视许嵩演唱会门票是否发售
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys  #这里是一个坑
import time
import urllib2
from bs4 import BeautifulSoup

headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }

response = urllib2.urlopen('https://piao.damai.cn/128220.html')
soup = BeautifulSoup(response.read(),'lxml')
item = soup.find('p',attrs={'class':'itm'})
# print len(item.get_text().strip())
if item.get_text().strip():#
    # print 'heihei'
    driver = webdriver.Chrome()
    # 打开一个页面（QQ空间登录页）
    driver.set_window_position(20, 40)
    driver.set_window_size(1100, 700)

    driver.get('http://mail.163.com/')
    time.sleep(3)  #等待这一步很重要
    # 登录表单在页面的框架中，所以要切换到该框架
    driver.switch_to.frame("x-URS-iframe")  #根据id也可寻找
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys('15608058020')
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys('zqy191155395')
    driver.find_element_by_id("dologin").click()
    time.sleep(2)
    element = driver.find_elements_by_class_name('oz0')
    element[1].click()
    time.sleep(2)
    driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('191155395@qq.com')
    driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys('ticket!!!')
    element1 = driver.find_element_by_class_name('APP-editor-iframe')
    driver.switch_to.frame(element1)  #根据id也可寻找
    driver.find_element_by_class_name('nui-scroll').send_keys('quikly!')

    driver.switch_to.parent_frame()  #记得返回上一层框架
    driver.find_elements_by_class_name('nui-btn-text')[2].click()
    # #直接键盘操作，不选取元素：TAB
    # chain = ActionChains(driver)
    # chain.send_keys('   15608058020').perform()
    # chain.send_keys(Keys.TAB).perform()   #用send_keys,不要用key_up
    # chain.send_keys("zqy191155395").perform()
    # chain.send_keys(Keys.ENTER).perform()
    # # chain.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    print driver.current_url

else:
    print 'ooooouch'