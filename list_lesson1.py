#__author__:'Faning Huang'
#__time__:'2017/11/4 0004 下午 8:20'

#count 方法统计某个元素在列表中出现的次数

#extend 方法可以在列表 的末尾一次性追加另一个序列中的多个值

#index 方法用于从列表中找出某个值第一个匹配项的索引位置
# a = ['wc','jx','xh','lg','sp','lg',['wc','jx']]
# first_lg_index = a.index('lg')
# print("first_lg_index",first_lg_index)
# little_list= a[first_lg_index+1:]
# second_lg_index = little_list.index('lg')
# print("second_lg_index",second_lg_index)
#
# second_lg_index_in_big_list = first_lg_index + second_lg_index + 1
#
# print("second_lg_index_in_big_list",second_lg_index_in_big_list)
#
# print("second lg: ",a[second_lg_index_in_big_list])

#reverse 方法将列表中的元素反向存放
# a = ['wc','jx','xh','lg','sp']
# a.reverse()
# print(a)

#sort 方法用于在原位置对列表进行排序
# x = [3,1,4,9,7,2,0,8]
# x.sort(reverse=True)#从大到小        #x.sort()#从小到大
# print(x)

# a = ['wc','jx','Xh','Lg','sp']
# a.sort()
# print(a)

a = ['wc','jx','xh','lg','sp']
print(a.count("hdlg"))






