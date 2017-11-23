#__author__:'Faning Huang'
#__time__:'2017/11/20 0020 下午 7:31'

# import sys,time
# for i in range(30):
#     sys.stdout.write(">")
#     sys.stdout.flush()
#     time.sleep(1)

# import sys,time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.2)

# f=open('寄芸1','w',encoding= 'utf-8')
# f.truncate(5)
# f.write('hello world')
# f.truncate(11)
# f.close()


# r+ w+ a+
# f=open('寄芸','r+',encoding='utf-8')
# f.readlines()
# f.write('faning')
# f.close()

# f=open('寄芸','w+',encoding='utf-8')
# print(f.readline( ))
# f.write('faning88888888888')
# print(f.tell())
# f.seek(0)
# print(f.readline( ))
# f.close()

# f=open('寄芸1','a+',encoding='utf-8')
# print(f.tell())
# print(f.readline())
# f.close()

# 终极问题
# number=0
# for line in f:
#     number+=1
#     if number==6:
#        f.write('faning')

# f_read=open('寄芸','r',encoding='utf-8')
# f_write=open('寄芸1','w',encoding='utf-8')
# number=0
# for line in f_read:
#     number+=1
#     if number==5:
#         line='hello faning'
#     f_write.write(line)
# f_read.close()
# f_write.close()


# with语句
# 为了避免打开文件后忘记关闭，可以通过管理上下文，即：
# with open('log','r') as f:
#     pass
# 如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源、
# 在python2.7后，whih又支持同时对多个文件 的上下文 进行管理，即：
# whih open('log1') as obj1, open('log2') as obj2
#     pass


with open('log1','r') as f_read,open('log2','w') as f_write:
    for line in f_read:
        f_write.write(line)




