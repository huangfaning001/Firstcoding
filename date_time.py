#__author__:'Faning Huang'
#__time__:'2017/11/12 0012 下午 11:34'

# 1、python3日期和时间
# Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
#
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
#
# 时间间隔是以秒为单位的浮点小数。
#
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
#
# Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳

# import time
# print(time.time()) ##时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。

# 2、时间元组
# 多Python函数用一个元组装起来的9组数字处理时间
#
# 字段              属性                 值
# 4位年数          tm_year               2017
# 月               tm_mon                1到12
# 日               tm_mday               1到31
# 小时             tm_hour               0到23
# 分钟             tm_min                0到59
# 秒               tm_sec                0到61（60或61是润秒）
# 一周的第几日     tm_wday               0到6(0是周一)
# 一年的第几日     tm_yday               1到366,一年中的第几天
# 夏令时           tm_isdst              是否为夏令时，值为1时是夏令时，值为0时不是夏令时，默认为-1

# print(time.localtime(time.time()))##从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数

# 3、获取格式化的时间
# 可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()

# import time
# print(time.asctime(time.localtime(time.time())))

# 4、格式化日期
# 可以使用 time 模块的 strftime 方法来格式化日期
#
# python中时间日期格式化符号：
# •%y 两位数的年份表示（00-99）
# •%Y 四位数的年份表示（000-9999）
# •%m 月份（01-12）
# •%d 月内中的一天（0-31）
# •%H 24小时制小时数（0-23）
# •%I 12小时制小时数（01-12）
# •%M 分钟数（00=59）
# •%S 秒（00-59）
# •%a 本地简化星期名称
# •%A 本地完整星期名称
# •%b 本地简化的月份名称
# •%B 本地完整的月份名称
# •%c 本地相应的日期表示和时间表示
# •%j 年内的一天（001-366）
# •%p 本地A.M.或P.M.的等价符
# •%U 一年中的星期数（00-53）星期天为星期的开始
# •%w 星期（0-6），星期天为星期的开始
# •%W 一年中的星期数（00-53）星期一为星期的开始
# •%x 本地相应的日期表示
# •%X 本地相应的时间表示
# •%Z 当前时区的名称
# •%% %号本身

# import time
# print(time.strftime('%Y',time.localtime()))  #获取完整年份
# print(time.strftime('%y',time.localtime()))  #获取简写年份
# print(time.strftime('%m',time.localtime()))  #获取月
# print(time.strftime('%d',time.localtime()))  #获取日
# print(time.strftime('%Y-%m-%d',time.localtime()))  #获取年-月-日
#
#
# print(time.strftime('%H',time.localtime()))  #获取时，24小时制
# print(time.strftime('%l',time.localtime()))  #获取时，12小时制
# print(time.strftime('%M',time.localtime()))  #获取分
# print(time.strftime('%S',time.localtime()))  #获取秒
# print(time.strftime('%H:%M:%S',time.localtime()))  #获取时:分:秒
#
#
# print(time.strftime('%a',time.localtime()))  #本地简化星期
#
# print(time.strftime('%A',time.localtime()))  #本地完整星期
#
# print(time.strftime('%b',time.localtime()))  #本地简化月份
#
# print(time.strftime('%B',time.localtime()))  #本地完整月份
#
# print(time.strftime('%c',time.localtime()))  #本地日期和时间表示
#
#
# print(time.strftime('%j',time.localtime())) #一年中的第几天
# print(time.strftime('%p',time.localtime())) #P.M等价符
#
# print(time.strftime('%U',time.localtime())) #一年中的第几个星期，星期天为星期的开始
# print(time.strftime('%w',time.localtime()))  #星期几,星期天为星期的开始
# print(time.strftime('%W',time.localtime()))  #一年中的第几个星期，星期一为星期的开始
# print(time.strftime('%x',time.localtime()))  #本地日期表示
#
# print(time.strftime('%X',time.localtime()))  #本地时间表示
#
# print(time.strftime('%Z',time.localtime()))  #当前时区
#
# print(time.strftime('%%',time.localtime()))  #输出%本身
#
#
# print(time.strftime('%Y-%m-%d %H:%M:%S %w-%Z',time.localtime()))
# #完整日期，时间，星期，时区

# 5、获取月日历
# import calendar
# cal=calendar.month(2017,11)
# print(cal)


#calendar.calendar(2017)
#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。
# 每日宽度间隔为w字符。
# 每行长度为21* W+18+2* C。l是每星期行数。
# import calendar
# c = calendar.calendar(2017)
# print(c)



