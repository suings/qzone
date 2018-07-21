#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
@author:Su
@file:mobile.py
@time:2018/07/21
"""
"""
版本信息
selenium 3.12.0
win10企业版1803
chrome 68.0 64位，以及对应版本的chromedriver
pycharm 2018.1社区版
python 3.62
使用前请补全config配置，位于第26行
"""
"""
可能遇到的问题:
    一分钟内刷新出的说说条数大于5条，则只会点赞最新5条(不打算解决
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

config={
    "qq":"3066819216",
    "pwd":"你的qq密码",
    "chromedriver":"C:\\Users\\Su\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver",
    "headless":False,
    "refreshtime":60
}
# qq:qq号码
# pwd:qq密码
# chromedriver:chromedriver所在路径，不用加.exe,注意是两个反斜杠
# headless: True 或者 False;是否以无头模式启动，默认是
# refreshtime:刷新页面的时间，以秒计，默认60秒
chrome_options = Options()
if config["headless"]:
    # 无头模式
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path=config["chromedriver"],chrome_options=chrome_options)

browser.get('https://mobile.qzone.qq.com/infocenter')
wait = WebDriverWait(browser, 20)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="u"]'))).send_keys(config["qq"])
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="p"]'))).send_keys(config["pwd"])

time.sleep(2) # 登陆之前停留一会，可能会出现滑动验证码，其实在设备和ip不变的情况下，一般不会出现滑动验证码
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="go"]'))).click() # 登录按钮
while 1:
    blocks=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"dataItem"))) # 说说所在的div
    print(time.asctime(time.localtime(time.time())))
    for block in blocks:
        likebtn=block.find_elements_by_tag_name("button")[0]
        if likebtn.text=="赞":
            likebtn.click()
            time.sleep(1) # 这行可以删了，写在这里是为了让点赞的行为更像人一些
    time.sleep(config["refreshtime"])
