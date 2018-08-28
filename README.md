# qzone
qq空间相关
有问题提[issue](https://github.com/suings/qzone/issues/new)
## 自动点赞说说
### windows版[autozan_windows.py](autozan_windows.py)

#### 测试环境:
    python3.6  
    selenium3.12.0  
    chrome68以及对应版本的chromedriver  
相关配置在config={}中
#### 思路
-  获取[手机版的空间](https://mobile.qzone.qq.com/infocenter)
-  直接使用密码登录，密码等位于代码中的config={}中  
-  使用`while True:`循环
-  在循环中先找到说说所在的div，然后判断这个说说是否已经点过赞，没有点过就点赞
### linux版[autozan_linux.py](autozan_linux.py)  
#### 测试环境:
    selenium 3.13.0  
    Debian Linux9  
    chrome 67以及对应版本的chromedriver  
    python 3.5.3  
相关配置也在config={}中  
#### 使用
装好各种库后，然后执行这个文件:[autozan_linux.py](autozan_linux.py)：`python3 autozan_linux.py`  
等待终端出现倒计时,在一分钟内将同目录下的qr_code.jpg文件转移到你的windows(或者一个可以查看图片的系统)下，可以使用sz命令:`sz qr_code.jpg`(建议预先安装lrzsz: `apt-get install lrzsz`),然后扫码登录。  
在一分钟内扫码登录成功就可自动点赞(每分钟刷新，比秒赞差一点)
#### 思路
-  直接获取空间链接，会自动跳转到登录页面
-  通过selenium获取页面截图(包含登录二维码)
-  下载截图然后扫码登录
-  登陆后就...自己写吧
#### Debian下相关环境配置(安装chrome及chromedriver)  
phantomjs已经过时，所以采用我改用chrome(其实是在原来系统上装phantomjs总有问题，就放弃了)  

Chrome安装参照了[Debian+Selenium+ChromeDriver](https://blog.csdn.net/GO_D_OG/article/details/79073727)，这篇文章看到'安装Xvfb'以前就行了，余下的可以看我写的  
我安装的版本是Google Chrome 67.xx  
对应的chromedriver可以用2.40版本[2.40版本](  http://chromedriver.storage.googleapis.com/index.html?path=2.40/)  
##### chromedrivere安装过程:  
使用wget下载对应版本chromedriver:  
`wget http://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip`  
然后使用unzip解压:`unzip chromedriver_linux64.zip`
提示没有unzip就先安装unzip:`apt-get install unzip`
unzip后会出现一个chromedriver文件  
然后mv移动chromedriver到/usr/bin目录:  
    `mv chromedriver /usr/bin`  
简单demo(demo.py):  
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("http://s.yuca.fun/tools/baidu.html")
print(browser.page_source)
```
demo是用来测试selenium以及chromedriver是否安装配置成功的  
demo中最重要的是chrome_options的4行。  
然后chrome的使用和phantomjs基本没区别

## PC版空间广告屏蔽规则(Adblocks Plus适用)
```
user.qzone.qq.com##.f-single.f-s-s > .f-single-top + *
user.qzone.qq.com##.f-single-biz
user.qzone.qq.com##.collet_box.fn_paipai
user.qzone.qq.com###idQbossHotbar
```