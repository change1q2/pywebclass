'''
作者：seak
时间：
项目：
题目：
作用：
备注：
访问课堂派，看到的任何一个元素都可以定位(全用xpath的相对定位方式)：
作业格式要求：
txt/excel文件：
每一个元素定位：1）元素说明(哪个页面哪个元素)  2）定位表达式
ps: 可用其它网站代替。不要求一定是课堂派。
'''
import time
from selenium import webdriver
#初始化游览器
browser = webdriver.Chrome()

#获取游览器地址
get_url = browser.get('http://inner.meeno.net:20684/dist/')
time.sleep(2)

