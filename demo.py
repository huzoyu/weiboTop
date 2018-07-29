# coding:utf-8
# 引入selenium中的webdriver
import re
from bs4 import BeautifulSoup
from time import process_time
from selenium import webdriver
import time

#取只有href属性的标签
def has_href_but_no_others(tag):
    return tag.has_attr('href') \
           and not tag.has_attr('class') \
           and not tag.has_attr('action-type') \
           and not tag.has_attr('id') \
           #and not tag.has_attr('action-type')

#加载驱动
option = webdriver.ChromeOptions()
option.add_argument('headless')
brower = webdriver.Chrome(chrome_options=option)
#设置url常量
url = 'http://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
#开始计时
start = process_time()
# 使用浏览器请求页面
brower.get(url)
# 加载3秒，等待所有数据加载完毕
time.sleep(15)
#获取html
html = brower.page_source
#bs解析
soup = BeautifulSoup(html, "html.parser")
# 通过id来定位元素
# .text获取元素的文本数据

#这种方式爬出来的是粗糙数据
#hotList = soup.find_all("p", class_="star_name",limit = 10)

#这种方法爬出来的有含class属性的空白a标签
#hotList = soup.find("body").find_all("a",attrs={"href":re.compile("/weibo/"),"target":re.compile("_blank")})

#
hotList = soup.find_all(has_href_but_no_others,href=re.compile("/weibo/"))

#打印结果
print(brower.title)
#逐条打印，去除每条前后的空白
i = 1
for hot in hotList:
#打印爬到标签的全部信息，方便调试
#    print(hot)
#只打印字符串
    print("%d : %s"%(i,hot.get_text("|",strip=True)))
    i=i+1

# 关闭浏览器
brower.quit()
#结束计时
end = process_time()
print(end-start)

