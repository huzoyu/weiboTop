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


'''
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