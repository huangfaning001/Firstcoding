#__author__:'Faning Huang'
#__time__:'2017/11/24 0024 下午 11:38'

# Python字典(dictionary)
#
# 字典dict，是Python唯一的标准mapping类型，也是内置在Python解释器中的。
#
# mapping
# object把一个可哈希的值（hashable
# value）映射到一个任意的object上。
#
# 什么是可哈希的
#
# 一个object是可哈希的（hashable）， 是指这个object在其生存期内有一个不变的哈希值（hash
# value），即__hash__()
# 方法返回的值。
#
# 所有不可变的（immutable）内置object都是hashable的，比如string，tuple。所有可变的（mutable）内置容器都不是hashable的，比如list，dict（即没有__hash__()
# 方法）。而所有自定义的类（use - defined
#
#
# class ）对象都是可哈希的（hashable），并且只能和自己相等，其hashvalue为其id(object)的值，这里的id()为内置函数，CPython实现的时候取的对象在内存中的地址。
#
#
# 字典Dictionary的key必须是可哈希的，所以tuple，string可以做key，而list不能做key，关于这个我以后会专门解释，或参见文末参考第3篇。
#
# dict本身是一个类
#
#
# class dict(mapping)
#
#
# 1，字典的创建
#
# d = dict({1: 'a', 2: 'b', 3: 'c'})  # 通过dict类来构建
#
# d
#
# {1: 'a', 2: 'b', 3: 'c'}
#
# d2 = {1: 'a', 2: 'b', 3: 'c'}           ＃直接构建，注意语法，大括号，冒号，逗号
#
# d2
#
# {1: 'a', 2: 'b', 3: 'c'}
#
# 2，dictionary支持的操作
#
# 作为Python唯一的标准mapping
# type，dictionary支持了增，删，查，整体更新等操作。
#
# 一部分操作是由dict的成员函数实现的，一部分操作是由Python的内置函数（built - in）function实现的，也有使用Python的del语句
#
# 2.1
# 引用元素
#
# 直接用d[
#     key]，就可以得到key所对应得那个object，但是如果key不存在呢，如果使用的就是标准的dict，那么会抛出KeyError异常。但是如果我们是自己从dict派生了一个自己的dictionary，那么只要我们定义__missing__函数，当key不存在时，这个函数会以key做为参数被调用，我们试验一下。
#
# 写一个module  ，mdict.py
# class myDict(dict):
#     2
#
# def __missing__(self, key):
#     print
#     "__missing__ called , key = ", key
#     return "^_^"
#
# 然后打开Python命令行解释器，import mdict
#
# 复制代码
# from mdict import myDict
# d = myDict({1: 'a', 2: 'b', 3: 'c'})
# d
# {1: 'a', 2: 'b', 3: 'c'}
# d[1]
# 'a'
# d[4]
# __missing__
# called, key = 4
# ^ _ ^
#
# 复制代码
#
# 可以看到__missing__()
# 被调用了。
#
# 如果只想得到某个key对应的value，不想对其进行改变，则用对象方法get(), 这类似C + +中“引用”和“值”的概念。
#
# a = d.get(1)
# a
# 'a'
#
# 2.2
# 类方法实现的操作
#
# d.clear()  # 清空
#
# d.copy()  # 拷贝生成另一个，浅拷贝（shallow copy）
#
# d.keys()，d.values()，d.items()
#
# 这三个都会生成dictionary相应的keys，values，items的copy，返回结果都是list，d.items()
# 生成的是(key, value)
# 二元tuple的list
#
# 复制代码
# d.items()
# [(1, 'a'), (2, 'b'), (3, 'c')]
# d.keys()
# [1, 2, 3]
#  d.values()
# ['a', 'b', 'c']
#
# 复制代码
#
# d.viewkeys()，d.viewvalues()，d.viewitems()
#
# 这三个都会生成dictionary相应的view
# object，view
# object是dictionary中（key, value）的动态反映，当dictionary中的内容变化时，view
# object也会变。
#
#
# 复制代码
# iewkeys = d.viewkeys()
# viewkeys
# dict_keys([1, 2, 3])
# list(viewkeys)
# [1, 2, 3]
# del d[1]
# list(viewkeys)
# [2, 3]
#
# 复制代码
#
# 2.3
# 内置函数实现的操作
#
# len(d)  # dictionary的长度
#
# del d[key]
# 或
# del d  # del语句
#
# key in d
# 或
# key not in d  # 返回True or False
#
# 3, 字典的bool判断
#
# Python的对象都可以直接用来判断其bool值, 对内置的字典来说, 当其为空时为False, 不为空时True
#
# d = {}
# bool(d)
# False
