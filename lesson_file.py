#__author__:'Faning Huang'
#__time__:'2017/11/13 0013 下午 9:27'

# f = open('寄芸','r',encoding='utf-8')#打开文件
# data = f.read() #获取文件内容
# print(data)

# f = open('寄芸1','w',encoding='utf-8')
# f.write('\nhello world\n')
# f.write('faning')
# f.close()#关闭文件

# 对文件操作流程
#1，打开文件，得到文件句柄并赋值给一个变量
#2，通过句柄对文件进行操作
#3，关闭文件

f = open('寄芸','r',encoding = 'utf-8')
dd = f.read(10)
print (dd)