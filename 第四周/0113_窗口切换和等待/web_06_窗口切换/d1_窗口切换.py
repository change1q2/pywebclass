import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

input_elem = driver.find_element_by_id('kw')
input_elem.send_keys('柠檬班')

# 百度提交
driver.find_element_by_id('su').click()


# 点击腾讯课堂
ketang = driver.find_element_by_xpath('//*[contains(text(), "lemon.ke.qq.com/")]')




handles = driver.window_handles
print("点击之前的所有的句柄", handles)

before_handle = driver.current_window_handle

print("切换之前", driver.current_window_handle)

ketang.click()


WebDriverWait(driver, 20).until(EC.new_window_is_opened(   handles    ))

print("等待之后", driver.current_window_handle)

print("等待之后的所有的窗口句柄", driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])
print("切换之后的窗口句柄", driver.current_window_handle)




