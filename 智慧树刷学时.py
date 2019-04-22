#-*-coding=utf-8-*-
import os
import re
import time
from selenium import webdriver
from datetime import date, datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.wait import WebDriverWait

# 模拟人工操作，没有任何风险。更改账号、密码，先把弹题做完！！！然后运行即可。
# 本脚本默认刷军事理论课程

def rush(url):
    #打开浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Chrome(chrome_options=chrome_options) # 后台模式
    wd.get(url) #网页跳转
    wd.maximize_window() # 放大窗口
    # time.sleep(10)
    try:
        wd.find_element_by_id('lUsername').send_keys(u'**********') # 填充用户名
        wd.find_element_by_id('lPassword').send_keys(u'**********') # 填充密码
        wd.find_element_by_class_name(u'wall-sub-btn').click()
    except:
        pass
    time.sleep(2)
    try: 
        wd.find_element_by_link_text('关闭').click() # 关闭可能出现的启动弹题
    except:
        pass
    time.sleep(1)
    wd.find_element_by_link_text('确定').click()
    time.sleep(1)
    wd.find_element_by_link_text('我已知晓').click()
    time.sleep(1)
    for i in range(100): # 设置一共播放多少节
        element = wd.find_element_by_id('mediaplayer')
        element.click()
        time.sleep(0.5)
        element.click()
        # time.sleep(0.2)
        wd.find_element_by_class_name('speedBox').click()
        # time.sleep(0.1)
        wd.find_element_by_class_name('speedTab15').click() # 切换1.5倍速度
        # time.sleep(0.1)
        wd.find_element_by_class_name('volumeBox').click()
        # time.sleep(0.1)
        wd.find_element_by_class_name('volumeIcon').click() # 静音
        # time.sleep(0.1)
        
        pro = wd.find_element_by_class_name('progressbar').get_attribute('style') # 获取进度
        pro = int(re.findall(r'[1-9]\d*',pro)[0])
        while pro!=100:
            print('本节进度：%d'%pro)
            pro1 = pro
            try:
                element = WebDriverWait(wd,20).until(EC.presence_of_element_located((By.CLASS_NAME, "popboxes_close"))) # 检测弹题
                element.click() # 关闭弹题
            except:
                pass
            time.sleep(2)
            pro = wd.find_element_by_class_name('progressbar').get_attribute('style') # 再次获取进度
            pro = int(re.findall(r'[1-9]\d*',pro)[0])
            if pro == pro1:
                wd.find_element_by_id('mediaplayer').click() # 播放结束而未完成进度，则再次播放
                wd.find_element_by_class_name('definiBox').click()
                wd.find_element_by_class_name('line1gq').click() # 换高清源

        time.sleep(1)
        wd.find_element_by_link_text('下一节').click() # 进度100后播放下一节
        print('本节完毕，播放下一节')
        time.sleep(3)

def main():
    url = 'http://study.zhihuishu.com/learning/videoList;jsessionid=F8729D3E0BDC524E45F8A69FAB731BE9?recruitAndCourseId=4b585c594c52415846425a5f51#'
    rush(url)

main()