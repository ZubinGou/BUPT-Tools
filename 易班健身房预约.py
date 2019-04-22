#-*-coding=utf-8-*-
import os
import time
from selenium import webdriver
from datetime import date, datetime, timedelta

# 用于当日预约5天后的健身房，使用需要修改用户名和密码。验证码问题待解决...
def reserve(url):
    #打开浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    # wd = webdriver.Chrome(chrome_options=chrome_options) # 后台模式
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    wd.get(url) #网页跳转
    # wd.maximize_window() #放大窗口
    #查找html id获取位置
    wd.find_element_by_id(u'account-txt').send_keys(u'************') #填充用户名
    time.sleep(0.2)
    wd.find_element_by_id('password-txt').send_keys(u'***********') #填充密码
    time.sleep(0.2)
    wd.find_element_by_id(u'login-btn').click() #模拟点击
    time.sleep(8)  # 目前的办法是暂停一段时间手动输入验证码
    try: wd.find_element_by_id(u'login-btn').click()
    except: pass
    time.sleep(4)
    for i in range(10):
        wd.get(url)
        time.sleep(1*i)
        wd.find_element_by_id(u'submit').click()
        time.sleep(1)
    wd.quit()

def main():
    day_5 = datetime.now()+timedelta(days=5)
    time = day_5.strftime('%Y%m%d')
    # url中的time=1表示预约6-7点，2表示7-8点，3表示8-9点。
    url = 'https://gym.yiban.bupt.link/new.php?time=2&date='+time
    print(url)
    reserve(url, url2)
main()