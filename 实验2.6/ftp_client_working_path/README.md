# Python 基础学习（复习）

+ **使用[菜鸟教程 python100例](http://www.runoob.com/python/python-100-examples.html?tdsourcetag=s_pctim_aiomsg)进行练习,遇到不会的或者不熟练的问题会在这个页面上写出来（主要是一些库的使用）**
+ **原文使用Python2，由于Python即将停止维护的问题，这里的代码以Python3为主**

---

## time

**[Python练习实例10](http://www.runoob.com/python/python-exercise-example10.html)**

```python
#!/usr/bin/python
# -*- coding = utf-8 -*-
import time
	
	
def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	
	
if __name__ == "__main__":
    main()
```

只是用``time.time()``会生成时间戳，这样便于时间计算。
使用``time.localtime(time.time())``可以将时间戳转化为时间元组，其中元组中的元素如下：

|属性|字段|值|
|:---:|:---:|:---:|
|``tm_year``|四位年数|如:2008|
|``tm_mon``|月|1-12|
|``tm_mday``|日|1-31|
|``tm_hour``|小时|0-23|
|``tm_min``|分钟|0-59|
|``tm_sec``|秒|0-61(60或61是闰秒)|
|``tm_wday``|一周的第几日|0-6(0是周一)|
|``tm_yday``|一年的第几日|1-366(儒略历)|
|``tm_isdst``|夏令时|-1, 0, 1, -1是决定是否为夏令时的旗帜|

转换成元组之后就可以进行格式化输出

使用``time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))``就可以对当前的时间进行输出

其中引号中的日期格式化符号主要使用以下的几种:

+ ``%y`` 两位数的年份表示（00-99）
+ ``%Y`` 四位数的年份表示（000-9999）
+ ``%m`` 月份（01-12）
+ ``%d`` 月内中的一天（0-31）
+ ``%H`` 24小时制小时数（0-23）
+ ``%I`` 12小时制小时数（01-12）
+ ``%M`` 分钟数（00=59）
+ ``%S`` 秒（00-59）
+ ``%j`` 年内的一天（001-366）
+ ``%U`` 一年中的星期数（00-53）星期天为星期的开始
+ ``%w `` 星期（0-6），星期天为星期的开始
+ ``%W`` 一年中的星期数（00-53）星期一为星期的开始
+ ``%%`` %号本身

部分摘自[菜鸟教程](http://www.runoob.com/python/python-date-time.html)，仅供学习使用