#__author__:'Faning Huang'
#__time__:'2017/11/14 0014 上午 10:00'
#

# enumerate函数说明：
# 函数原型：enumerate(sequence, [start=0])
#
# 功能：将可循环序列sequence以start开始分别列出序列数据和数据下标
#
# 即对一个可遍历的数据对象(如列表、元组或字符串)，enumerate会将该数据对象组合为一个索引序列，同时列出数据和数据下标。
# 举例说明：
# 存在一个sequence，对其使用enumerate将会得到如下结果：
#
# start        sequence[0]
#
# start+1　 sequence[1]
#
# start+2    sequence[2]......
#
# enumerate函数用于遍历序列中的元素以及它们的下标,多用于在for循环中得到计数,enumerate参数为可遍历的变量，如 字符串，列表等
#
# 一般情况下对一个列表或数组既要遍历索引又要遍历元素时，会这样写：
#
# 12 for i in range (0,len(list)):
#   print i ,list[i]
#
# 但是这种方法有些累赘，使用内置enumerrate函数会有更加直接，优美的做法，先看看enumerate的定义：
#
# 1234567 def enumerate(collection):
#   'Generates an indexed series: (0,coll[0]), (1,coll[1]) ...'
#    i = 0
#    it = iter(collection)
#    while 1:
#    yield (i, it.next())
#    i += 1
#
#
# enumerate会将数组或列表组成一个索引序列。使我们再获取索引和索引内容的时候更加方便如下：
#
# 12 for index，text in enumerate(list):
#   print index ,text
#
#
# 代码实例1：
# 12345 i = 0
# seq = ['one', 'two', 'three']
# for element in seq:
#     print i, seq[i]
#     i += 1
#
# 0 one
#
# 1 two
#
# 2 three
#
# 代码实例2：
# 123 seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print i, seq[i]
#
# 0 one
#
# 1 two
#
# 2 three
#
#
# 代码实例3：
# 12 for i,j in enumerate('abc'):
#     print i,j
#
# 0 a
#
# 1 b
#
# 2 c
