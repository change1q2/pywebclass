'''
作者：seak
时间：
项目：
题目：
作用：
备注：
根据上课内容，使用显示等待，在百度页面搜索柠檬班，定位柠檬班腾讯课堂当中的 “小简老师”
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#初始化游览器
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#进行隐式等待:得不到某个元素就等待一段时间，直到拿到某个元素位置，超过对应等待时间会报异常。
#driver.implicitly_wait(30)
#输入游览器地址
driver_url = driver.get("https://www.baidu.com")

#找到搜索框
find_su = driver.find_element_by_id("kw").send_keys("柠檬班")
#找到百度一下，点击
find_kw = driver.find_element_by_id("su").click()

#找到柠檬班腾讯课堂，点击
find_lemone = driver.find_element_by_link_text("柠檬班_腾讯课堂")

#获取句柄的操作
handles = driver.window_handles
print("点击之前的所有句柄", handles)

before_handles = driver.current_window_handle
print("切换之前的句柄", before_handles)

find_lemone.click()

#显示等待
e = WebDriverWait(driver,30,0.2).until(EC.element_to_be_clickable((By.XPATH,)))

#找到小简老师点击

#关闭游览器
time.sleep(2)
driver.quit()