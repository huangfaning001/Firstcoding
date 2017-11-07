#__author__:'Faning Huang'
#__time__:'2017/11/5 0005 下午 10:36'

#元组
# a = (2,4,5,6,7,8,9)
# print(a[1])
# a[1]=5
# print(a)

#字典
#字典是一种key-value形式的数据类型
#字典两大特点： 无序，键唯一

# dict1={'name':'faning','age':'25','sex':'male'}
# dict2=dict((('name','faing'),))
# print(dict1)
# print(dict2)
# print(dict1['name'])
#
# dict3=dict([['year','17'],])
# print(dict3)

info ={
    'student001':'张晓明',
    'student002':'李天霸',
    'student003':'王箩' #key尽量不要写中文，虽然不会报错，但是有可能导致编码问题，value取不出来
}
# print(info)
# print(info['student002'])
# info['student001']='Alice'#若是字典中key已存在，则更改value
# print(info)
# info['student004']='Ben'#若是key不存在，则新增
# print(info)
# del info['student001']#根据key来删除
# print(info)
# info.pop('student002')#根据key来删除（标准的删除姿势）
# print(info)
# print(info.get('student003'))#根据key查找（推荐）
# print('student004' in info)#判断key是否在字典中，在返回True，不在返回False
# print(info.items())#将字典转换为列表
# print(info.fromkeys([7,8,9],'abc'))#创建一个新的字典如：{8:'abc',9:'abc',7:'abc'}

# b = {
#     'student003':'Bar',
#     1:5,
#     6:9
# }
# info.update(b)
# print(info)
# print(b)
#现在有inof，b两个字典，info.update(b)是将b作为参数传到info中去
#如果info中有和b相同的key，则替换value，如果没有，就将b中数据增加到info中去。
#两个字典合并，中间有交叉的就替换，没有交叉的就增加

#字典的循环
# for i in info:#推荐使用的循环方式（效率高）
#      print(i)#循环打印key
#      print(i,info[i])#循环打印key，value
# for k,v in info.items():#不推荐的循环方式，info.items()先将字典转换为列表，再循环打印，如果数据量大，效率低下
#     print(k,v)

#嵌套字典
world = {
    '美国' : {'城市' : ['旧金山','西雅图'] ,
            '总统': ['克林顿','奥巴马']
           },
    '中国' : {'城市' : ['西安','成都'],
            '主席' : ['毛##','习##']
           }
}

# print(world)
# world['中国']['主席'][0] = '习大大'
# print(world)
# print(world.keys())#打印字典的key
# print(world.values())
world.setdefault('##',{'##':['##','##']})#先到字典里边查询有没有，如果有，就返回值，没有就加进去
print(world)