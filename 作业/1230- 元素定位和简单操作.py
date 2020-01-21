'''
作者：seak
时间：
项目：
题目：
作用：
备注：
使用上课学到的 selenium 知识完成以下自动化操作：
1，百度搜索 “柠檬班”
2，点击进入柠檬班课堂
'''


import time
from selenium import webdriver

#第一步：初始化游览器

#1.指定文件路径
#browser = webdriver.Chrome(executable_path=r"C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\chromedriver_79.exe")
#2.全局文件路劲
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#第二步：进入被测网址
url = browser.get('http://www.baidu.com')

#第三步：调整样式
#1.放大窗口
#max_windown = browser.maximize_window()
#2.设置等待时间
#sleep = time.sleep(2)


#第四步：元素定位
# 1， ID, 查找到的元素是一个 WebElement 对象，
# 如果没有找到，报错：NoSuchElementException
input_element = browser.find_element_by_id('kw')
#.输入内容
write = input_element.send_keys("柠檬班")
time.sleep(2)

#第五步：点击搜索
click_find = browser.find_element_by_id("su").click()
time.sleep(2)
#通过link_text获取a标签的超链接
e = browser.find_element_by_xpath('//*[contains(text(),"lemon.ke.qq.com/")]')
e.click()
time.sleep(2)


#第六步：关闭游览器
close = browser.quit()

