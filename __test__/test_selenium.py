import time

from selenium import webdriver

wd = webdriver.Chrome('D:\cafe24\chromedriver.exe')
wd.get('http://www.google.co.kr')

time.sleep(2)
html = wd.page_source
print(html)
wd.quit()