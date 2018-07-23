#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
@author:Su
@file:autozan_linux.py
@time:2018/07/23
"""
"""
版本信息
selenium 3.13.0
Debian Linux9
chrome 67以及对应版本的chromedriver
python 3.5.3
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
    "chromedriver":"/usr/bin/chromedriver",
    "refreshtime":60,
    "qrpath":"/root/su/qr_code.png"
}
# qq:qq和扫码登录用的QQ一致(不修改好像也能用)
# chromedriver:chromedriver所在路径
# refreshtime:刷新页面的时间，以秒计，默认60秒
# qrpath：登录二维码的保存路径,可以使用相对路径
chrome_options = Options()
chrome_options.add_argument("--headless") # 无头模式
chrome_options.add_argument("--disable-gpu") # 禁用GPU
chrome_options.add_argument("--no-sandbox") # 某个报错
browser = webdriver.Chrome(executable_path=config["chromedriver"],chrome_options=chrome_options)


browser.get("https://user.qzone.qq.com/{}/infocenter".format(config["qq"]))

browser.switch_to.frame("login_frame")

wait = WebDriverWait(browser, 20)
browser.save_screenshot("qr_code.png")
# 等待登录
browser.switch_to.default_content()

print("登录二维码已经保存至{}，请在另一终端使用'sz {}'下载图片到本机后扫码登录".format(config["qrpath"],config["qrpath"]))
t=60
while t>0:
    print("\n给你一分钟时间登录,还有{}秒".format(t))
    time.sleep(5)
    t-=5
print("没登上就静等报错吧")

print("登上了吗？再等等")

while 1:
    browser.get('https://mobile.qzone.qq.com/infocenter')
    blocks=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"dataItem"))) # 说说所在的div
    print(time.asctime(time.localtime(time.time())))
    for block in blocks:
        likebtn=block.find_elements_by_tag_name("button")[0]
        if likebtn.text=="赞":
            # 判断是否已经赞过
            likebtn.click()
            time.sleep(1) # 这行可以删了，写在这里是为了让点赞的行为更像人一些
    time.sleep(config["refreshtime"])
