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

f = open('寄芸1','r',encoding = 'utf-8')
# print(f.read(5))
# print(f.read(5))
num = 0
for i in f.readlines():
    num+=1
    if num == 6:
        i = ''.join((i.strip(),'123456'))#取代万恶的+
    print(i.strip())
f.close()
# print(f.readline())
# print(f.readline())

# print(f.readlines()) #['依稀共话西厢人\n', '怎堪无力渡芳魂\n', '案上锦书残\n', '零落轻拾当日谶\n', '无人与我立黄昏\n', '无人问我粥可温']












# 文件操作的步骤：
#
# 打开文件 -> 操作文件 -> 关闭文件
#
# 切记：最后要关闭文件（否则可能会有意想不到的结果）
#
# 打开文件
# 文件句柄 = open('文件路径', '模式')
#
# 指定文件编码
#
#
#
#
# 文件句柄= open('文件路径','模式',encoding='utf-8')
#
# 为了防止忘记关闭文件，可以使用上下文管理器来打开文件
#
#
#
#
# with open('文件路径','模式') as 文件句柄:
#
# 打开文件的模式有：
#
#
#
#
# r，只读模式（默认）。
#
# w，只写模式。【不可读；不存在则创建；存在则删除内容；】
#
# a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
#
# r+，可读写文件。【可读；可写；可追加】
#
# w+，写读
#
# "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
#
# rU
#
# r+U
#
# "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
#
# rb
#
# wb
#
# ab
#
# 关闭文件
# 文件句柄.close()
#
# 操作文件：
#
# detach
#
# #占位
#
# fileno（返回文件描述符,用于底层操作系统的 I/O 操作）
#
# fid = 文件句柄.fileno()
#
# print(fid)
#
# flush（刷新缓冲区，将缓冲区中的数据立刻写入文件）
#
#
#
#
# 文件句柄.flush()
#
# isatty（判断文件是否连接到一个终端设备，返回布尔值）
#
#
#
#
# 文件句柄.isatty()
#
# read（从文件中读取指定的字符数，默认读取全部）
#
#
#
#
# str = 文件句柄.read()      #读取整个文件
#
# str1 = 文件句柄.read(10)   #读取文件前10个字符
#
# readable（判断文件是否可读，返回布尔值）
#
#
#
#
# 文件句柄.readable()
#
# readline（每次最多读取一行数据，每行的最后包含换行符'\n'）
#
#
#
#
# print(文件句柄.readline())   #读取第一行数据
#
# print(文件句柄.readline(3))  #读取第二行前3个字符
#
# print(文件句柄.readline())   #读取第二行剩余字符
#
# print(文件句柄.readline())   #读取第三行
#
# seek（移动文件读取的指针，如果文件中包含中文，移动指针必须是3的倍数，不然会报错，因为一个中文字符等于3个字节）
#
#
#
#
# 文件句柄.seek(6)
#
# seekable（判断文件指针是否可用，返回布尔值）
#
#
#
#
# 文件句柄.seekable()
#
# tell（获取指针位置）
#
#
#
#
# 文件句柄.tell()
#
# truncate（截断，把指针后面的内容删除，并写入文件，要在可写模式下操作）
#
#
#
#
# f = open('text.txt','r+',encoding='utf-8')
#
# f.seek(9)   #把指针移动到第9个字节后面（即第3个中文后面）
#
# f.truncate()  #把第3个中文后面的字符删除，并写入文件
#
# f.close()
#
# writable（判断文件是否可写，返回布尔值）
#
#
#
#
# 文件句柄.writable()
#
# write（把字符串写入文件，并返回字符数）
#
#
#
#
# 文件句柄.write('字符串')

