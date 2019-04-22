#-*-coding=utf-8-*-
import os
import requests
import json
from http import cookiejar
from bs4 import BeautifulSoup as bs
from twilio.rest import Client

# 本爬虫将北邮信息门户更新通知直接发送到你的手机上，可将之设置到系统的计划任务中，如每20分钟运行一次，即可自动提醒啦~
# 需设置你的学号、密码，注册twilio账号（用于发送短信）并设置，并且注册百度短网址获取token。

def getLt(str):
    lt=bs(str,'html.parser')
    dic={}
    for inp in lt.form.find_all('input'):
        if(inp.get('name'))!=None:
            dic[inp.get('name')]=inp.get('value')
    return dic

def craw(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    s=requests.Session()
    r=s.get('https://auth.bupt.edu.cn/authserver/login?service=http%3A%2F%2Fmy.bupt.edu.cn%2Findex.portal',headers=header)
    dic=getLt(r.text)
    postdata={
        'username':'********',#此处为你的学号
        'password':'***********',#你的密码
        'lt':dic['lt'],
        'execution':'e1s1',
        '_eventId':'submit',
        'rmShown':'1'
    }
    response=s.post('https://auth.bupt.edu.cn/authserver/login?service=http%3A%2F%2Fmy.bupt.edu.cn%2Findex.portal',data=postdata,headers=header)
    response2=s.get(url ,headers=header)
    soup=bs(response2.text,'lxml')
    info_all=soup.find('ul', class_='newslist list-unstyled')
    info_new=info_all.find('li')
    info_first=info_new.find('a')
    title=info_first.get('title')
    href='http://my.bupt.edu.cn/'+info_first.get('href')
    auther=info_new.find('span', class_='author').text
    time=info_new.find('span', class_='time').text
    return title, href, auther, time

# 使用Twilio的免费手机号发送短信
# 你需要在官网上申请一个账号，这里是官网：https://www.twilio.com/
def send_sms(my_number='+86**********', msg='你好，这是来自你自己的手机测试信息！'):
    # 从官网获得以下信息
    account_sid = '***************'
    auth_token = '**********'
    twilio_number = '**************'
    client = Client(account_sid, auth_token)
    try:
        client.messages.create(to=my_number, from_=twilio_number, body=msg)
        print('短信发送成功！')
    except ConnectionError as e:
        print('发送失败，请检查你的账号是否有效或网络是否良好！')
        return e

def short(urlx):
    host = 'https://dwz.cn'
    path = '/admin/v2/create'
    url = host + path
    method = 'POST'
    content_type = 'application/json'
    # TODO: 设置Token
    token = '你的token'
    # TODO：设置待创建的长网址
    bodys = {'url':urlx}
    # 配置headers
    headers = {'Content-Type':content_type, 'Token':'*********************'}
    # 发起请求
    response = requests.post(url=url, data=json.dumps(bodys), headers=headers)
    # 读取响应
    return response.json().get("ShortUrl")

def main():
    # 理学院
    url0='http://my.bupt.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjE3MzN8dmlld3xub3JtYWx8Z3JvdXBpZD0xODMzNDEwMDAmZ3JvdXBuYW1lPeeQhuWtpumZoiZhY3Rpb249YnVsbGV0aW5QYWdlTGlzdA__#anchorf1733'
    # 教务处
    url1='http://my.bupt.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjE3MzN8dmlld3xub3JtYWx8Z3JvdXBpZD0xODMyMDIwMDAmZ3JvdXBuYW1lPeaVmeWKoeWkhCZhY3Rpb249YnVsbGV0aW5QYWdlTGlzdA__#anchorf1733'
    # 计算机学院
    url2='http://my.bupt.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjE3MzN8dmlld3xub3JtYWx8Z3JvdXBpZD0xODMzMTMwMDAmZ3JvdXBuYW1lPeiuoeeul%2BacuuWtpumZoiZhY3Rpb249YnVsbGV0aW5QYWdlTGlzdA__#anchorf1733'
    # 马克思主义学院
    url3='http://my.bupt.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjE3MzN8dmlld3xub3JtYWx8Z3JvdXBpZD0xODMzMzIwMDAmZ3JvdXBuYW1lPemprOWFi%2BaAneS4u%2BS5ieWtpumZoiZhY3Rpb249YnVsbGV0aW5QYWdlTGlzdA__#anchorf1733'
    # 学生处
    url4='http://my.bupt.edu.cn/index.portal?.p=Znxjb20ud2lzY29tLnBvcnRhbC5zaXRlLnYyLmltcGwuRnJhZ21lbnRXaW5kb3d8ZjE3MzN8dmlld3xub3JtYWx8Z3JvdXBpZD0xODMyMTIwMDAmZ3JvdXBuYW1lPeWtpueUn%2BWkhCZhY3Rpb249YnVsbGV0aW5QYWdlTGlzdA__#anchorf1733'
    
    url_list=[url0, url1, url2, url3, url4]
    open('pre_title.txt', 'a')
    for u in url_list:
        title, href, auther, time=craw(u)
        with open('pre_title.txt', 'r+', encoding='utf-8') as file:
            pre_title=file.read().split('\n')
            print(pre_title)
            if title not in pre_title:
                url = short(href)
                print(url)
                # 需要设置一些短信不能发送的词汇，如http等
                send_sms(msg=title+'\n'+url.lstrip('https://')+'\n'+auther+'\n'+time)
                file.write(title+'\n')
            else:
                print('无更新')
main()