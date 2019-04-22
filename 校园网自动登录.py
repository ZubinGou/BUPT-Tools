"""
Veritas vos liberabit
Unoriginal
@author: Tyrion Lannister
"""
'''
这是电脑自动登录校园网bupt-portal脚本，欲登录运营商网络请自行修改

打开方式：
0，更改账号(2018211000)和密码(******),连接bupt-portal，在未登录情况下，运行即可自动登录。

开机自动登录：
1，移动脚本到开机自启动文件夹内，一般为C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
2，wifi连接bupt-portal勾选自动连接
3，重启试下吧！
（也可以设置到计划任务里面开机运行）
'''
import urllib.request
import re
#              账号↓          密码↓
pd = 'DDDDD=2018211000&upass=******&savePWD=0&0MKKey='.encode('utf-8')
fp = urllib.request.urlopen("http://10.3.8.211",pd)

mbt=fp.read().decode('gb2312')
checkinfo=re.compile(r'(?<=<title>)\S+?(?=</title>)')
check=re.findall(checkinfo,mbt)
if check[0]=='登录成功窗':
    print('''                      .::::.
                     .::::::::.
                    :::::::::::
                 ..:::::::::::'
              '::::::::::::'
                .::::::::::         Viva la Vida!!
           '::::::::::::::..
                ..::::::::::::.
              ``::::::::::::::::
               ::::``:::::::::'        .:::.
              ::::'   ':::::'       .::::::::.
            .::::'      ::::     .:::::::'::::.
           .:::'       :::::  .:::::::::' ':::::.
          .::'        :::::.:::::::::'      ':::::.
         .::'         ::::::::::::::'         ``::::.
     ...:::           ::::::::::::'              ``::.
    ```` ':.          ':::::::::'                  ::::..
                       '.:::::'                    ':'````..''')
    
else:
    print('''
 　　　　　　　　┏┓　　　┏┓
 　　　　　　　┏┛┻━━━┛┻┓┻━━━┛
 　　　　　　　┃　　　　　　　┃ 　
 　　　　　　　┃　　　━　　　 ┃
 　　　　　　　┃　＞　　　＜　┃
 　　　　　　　┃　　　　　　　┃
 　　　　　　　┃...　⌒　... ┃           Valar Morghulis.
 　　　　　　　┃　　　　　　　┃
 　　　　　　　┗━┓　　　   ┏━┛
 　　　　　　　　　┃　　　┃　　　　　　　　　
 　　　　　　　　　┃　　　┃   
 　　　　　　　　　┃　　　┃　　　　　　　　　　　
 　　　　　　　　　┃　　　┃  　　　　　　
 　　　　　　　　　┃　　　┃
 　　　　　　　　　┃　　　┃　　　　　　　　　　　
 　　　　　　　　　┃　　　┗━━━┓
 　　　　　　　　　┃　　　　　　　┣┓
 　　　　　　　　　┃　　　　　　　┏┛
 　　　　　　　　　┗┓┓┏━┳┓┏┛
 　　　　　　　　　　┃┫┫　┃┫┫
 　　　　　　　　　　┗┻┛　┗┻┛''')
    
