# -*- coding:utf-8 -*-
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com/')
print('打開瀏覽器')
print(driver.title)
driver.find_element_by_id('kw').send_keys('測試')
print('關閉')
driver.quit()
print('測試完成')