# coding:utf-8
# 引入selenium中的webdriver
import re
from urllib.request import urlretrieve
from selenium import webdriver
import time
# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器

driver = webdriver.PhantomJS(executable_path="D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")


# 下载HTML
def getHtml(url):
    # 使用浏览器请求页面
    driver.get(url)
    # 加载3秒，等待所有数据加载完毕
    time.sleep(15)
    # 通过id来定位元素，
    # .text获取元素的文本数据
    html = driver.page_source.encode('utf-8', 'ignore')  # 这个函数获取页面的html
    driver.get_screenshot_as_file(url+".png")  # 获取页面截图
    print("Success To Create the screenshot & gather html")
    # 关闭浏览器

    return html



# 从html中解析出图片URL
def getImgList(html):
       reg = r'src="(http://imgsrc.baidu.com/.*?\.jpg)"'
       imgre = re.compile(reg)
       htmld = html.decode('utf-8')
       imglist = imgre.findall(htmld)
       return imglist

# 下载处理
def imgDownload(imglist,i):
   x=0
   for imgurl in imglist:
       print(imgurl)
       urlretrieve(imgurl,'E:/spider/beautiful/%s%s.jpg' % (x,i))
       x+=1


url = 'http://tieba.baidu.com/p/2173159072#!/l/p'
if __name__ == '__main__':
    for i in range(1,7):
       setUrl = url+str(i)
       print(setUrl)
       html = getHtml(setUrl)

       imgList = getImgList(html)
       print(imgList)
       imgDownload(imgList,str(i))
driver.close()



'''

# -*- coding: utf-8 -*-
import urllib.request
import urllib.urlretrieve
import urllib
import re
import time

from selenium import webdriver
from bs4 import BeautifulSoup


page = urllib.request.urlopen("http://www.maigoo.com/news/463071.html")
html = page.read().decode("utf-8")
print(html)


soup = BeautifulSoup(html)
print(soup.prettify())

soup = BeautifulSoup(page,"html.parser")
hot_div = soup.find(attrs={"class":"S_wrap "})
#hot_a = hot_div.findAll(attrs={"target":"_blank"})
for hot in hot_div:
    print(hot.string)


#参考代码
# -*- coding: utf-8 -*-
import urllib.request
import urllib
from bs4 import BeautifulSoup

res = urllib.request.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res,"html.parser")
book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print(book.string)
    '''