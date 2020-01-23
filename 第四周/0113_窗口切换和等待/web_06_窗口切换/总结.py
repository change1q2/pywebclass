"""
xpath css
1, xapth:复杂元素定位，功能更强
2, css: 更简洁，效率更高，速度更快
text 只有 xpath 有，

xpath:
1, (//tagname(或者是*)[@属性名称=“属性值” and text()='文本值']/tagname)[1]
2, 轴定位难度：记住各种各样的关系（轴名称）  //tagname//轴名称::tagname[]

元素等待和窗口切换
三种元素等待：
1， time.sleep() 强制等待
2， 隐式等待
3， 显示等待

为什么要进行元素等待？？
1， 因为网络慢怕加载不出来
2， 元素只有执行某种交互的时候才会加载出来
3， 懒加载
一句话：某些元素或者某些操作只有加载完成才能定位

为什么要学习隐式等待和显示等待？？time.sleep() 不行吗？


1，一定要隐式等待。
2， 显示等待（）

3， 工作当中，可以自己去封装，

TODO:
web 自动化测试：90% 的错误，NoSuchElementException, TimeOut, 元素找不到。
1， 看你的元素定位方式有没有问题。xpath: 检查一下 xpath 表达式有没有问题
2， 没有等待。


1，强制等待一般不会用；
2，隐式等待。通用，创建完浏览器直接使用，全局只需要使用一次
3，显式等待。 写好代码，如果隐式等待不生效，再用显示等待。

面试：
隐式等待的不足：只能用来查找元素，元素是否被加载，
但是还有其他比较复杂的条件她是不能发现的（比如一个新窗口打开）

显示等待的用法：
1， 条件 locator 里面的参数类型：元组类型，千万不要把括号拉掉了。


窗口切换：
- window 切换， 等待的时候 window_handles 是在新窗口打开动作的前面。
- iframe 切换， 等待有 4 中参数： 1， 索引，2name, 3, webelement, 4 locator 元组
- alert 切换，  EC.alert_is_predent


"""
