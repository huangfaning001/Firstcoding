<<<<<<< HEAD
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

f=open('寄芸1','a+',encoding='utf-8')
print(f.tell())
print(f.readline())
f.close()

# 终极问题
number=0
for line in f:
    number+=1
    if number==6:
       f.write('faning')

=======
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

f=open('寄芸1','a+',encoding='utf-8')
print(f.tell())
print(f.readline())
f.close()

# 终极问题
number=0
for line in f:
    number+=1
    if number==6:
       f.write('faning')

>>>>>>> 39c2212e8f3d36c2375e0176700d851aebefe0cb
