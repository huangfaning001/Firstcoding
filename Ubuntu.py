#__author__:'Faning Huang'
#__time__:'2017/11/28 0028 下午 10:10'


# 一、 Ubuntu简介
#
# Ubuntu（乌班图）是一个基于Debian的以桌面应用为主的Linux操作系统，据说其名称来自非洲南部祖鲁语或科萨语的“ubuntu”一词，意思是“人性”、“我的存在是因为大家的存在”，是非洲传统的一种价值观。
#
# Ubuntu的目标在于为一般用户提供一个最新同时又相当稳定，主要以自由软件建构而成的操作系统。Ubuntu目前具有庞大的社区力量支持，用户可以方便地从社区获得帮助。
#
#
# 二. 安装
#
# ubuntu官方网站： http://www.ubuntu.com/    对应中文地址为 http://www.ubuntu.org.cn/index_kylin
#
# 桌面版下载地址： http://www.ubuntu.com/download/desktop
#
# # 目前最新版本是：  Ubuntu 16.04.1 LTS ，建议下载：  Ubuntu 16.04.1 Desktop (64-bit)
#
# 虚拟机软件： vmware /VirtualBox ，mac下还可以使用： parallels  ， 其中VirtualBox是开源免费的。
#
#
# 三、 安装过程中的知识点：
#
# 虚拟机的网络类型的简单理解：
#
# 　　虚拟机是在我们的操作系统里使用软件模拟出来的，相当于虚拟机是寄宿在我们的真实的物理机的操作系统里的，虚拟机和物理机之间的关系是 寄宿与被寄宿的关系， 真实的物理机被称为宿主机。
#
# 　　1.  bridged（桥接模式） ：  我们的电脑在上网的时候都需要有一个网络地址（IP地址），通过这个地址可以确定我们的电脑在网络上的位置，桥接模式就是将我们虚拟机中的网卡的网络地址 放在我们真实的物理机的网卡上。 这样的话，我们的虚拟机就好像跟我们的宿主机所在的局域网中的一台机器一样。 桥接模式适合有路由器的情况，和真实的物理环境一样。
# 　
# 　　2. NAT（网络地址转换模式） ： 在宿主机上制作一个虚拟网卡，通过这个网卡，给虚拟机分配IP。宿主机在这里的角色相当于局域网中的路由器。NAT模式适合于没有路由器的情况，虚拟机通过宿主机去上网。　　
#
# 　　3.Host-Only（模式）： 和NAT模式很像，唯一的区别是，没有地址转换服务，所以该模式下虚拟机只能访问到主机。无法访问外网。
#
#
# LInux目录结构：
#
# / ： 所有目录都在
# /boot : boot 配置文件、内核和其它启动 时所需的文件
# /etc ： 存放系统配置有关的文件
# /home ： 存放普通用户目录
# /mnt ： 硬盘上手动 挂载的文件系统
# /media ： 自动挂载（加载）的硬盘分区以及类似CD、数码相机等可移动介质。
# /cdrom ： 挂载光盘？
# /opt ： 存放一些可选程序,如某个程序测试版本,安装到该目录的程序的所有数据,库文件都存在同个目录下
# /root ： 系统管理员的目录，对于系统来说，系统管理员好比上帝，他可以对系统做任何操作，比如删除你的文件，一般情况下不要使用root用户。
# /bin ： 存放常用的程序文件（命令文件）。
# /sbin ： 系统管理命令，这里存放的是系统管理员使用的管理程序
# /tmp ： 临时目录，存放临时文件，系统会定期清理该目录下的文件。
# /usr ： 在这个目录下，你可以找到那些不适合放在/bin或/etc目录下的额外的工具。比如游戏、打印工具等。/usr目录包含了许多子目录： /usr/bin目录用于存放程序;/usr/share用于存放一些共享的数据，比如音乐文件或者图标等等;/usr/lib目录用于存放那些不能直接 运行的，但却是许多程序运行所必需的一些函数库文件。/usr/local ： 这个目录一般是用来存放用户自编译安装软件的存放目录；一般是通过源码包安装的软件，如果没有特别指定安装目录的话，一般是安装在这个目录中。
#  　　　　/usr/bin/ 非必要可执行文件 (在单用户模式中不需要)；面向所有用户。
#  　　　　/usr/include/ 标准包含文件。
#  　　　　/usr/lib/ /usr/bin/和/usr/sbin/中二进制文件的库。
#  　　　　/usr/sbin/ 非必要的系统二进制文件，例如：大量网络服务的守护进程。
#  　　　　/usr/share/ 体系结构无关（共享）数据。
#  　　　　/usr/src/ 源代码,例如:内核源代码及其头文件。
#  　　　　/usr/X11R6/ X Window系统 版本 11, Release 6.
# 　　　　/usr/local/ 本地数据的第三层次， 具体到本台主机。通常而言有进一步的子目录， 例如：bin/、lib/、share/.
#
# /var ： 该目录存放那些经常被修改的文件，包括各种日志、数据文件；
# /var/cache/ 应用程序缓存数据。这些数据是在本地生成的一个耗时的I/O或计算结果。应用程序必须能够再生或恢复数据。缓存的文件可以被删除而不导致数据丢失。
# /var/lib/ 状态信息。 由程序在运行时维护的持久性数据。 例如：数据库、包装的系统元数据等。
# /var/lock/ 锁文件，一类跟踪当前使用中资源的文件。
# /var/log/ 日志文件，包含大量日志文件。
# /var/mail/ 用户的电子邮箱。
# /var/run/ 自最后一次启动以来运行中的系统的信息，例如：当前登录的用户和运行中的守护进程。现已经被/run代替[13]。
# /var/spool/ 等待处理的任务的脱机文件，例如：打印队列和未读的邮件。
# /var/spool/mail/ 用户的邮箱(不鼓励的存储位置)
#  /var/tmp/ 在系统重启过程中可以保留的临时文件。
# /lib : 目录是根文件系统上的程序所需的共享库，存放了根文件系统程序运行所需的共享文件。这些文件包含了可被许多程序共享的代码，以避免每个程序都包含有相同的子程序的副本，故可以使得可执行文件变得更小，节省空间。
# /lib32 : 同上
# /lib64 ： 同上
# /lost+found ： 该目录在大多数情况下都是空的。但当突然停电、或者非正常关机后，有些文件就临时存放在；
# /dev : 存放设备文件
# /run ： 代替/var/run目录，
# /proc : 虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
# /sys ： 和proc一样，虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
#
#
#
# SWAP分区的作用：
#
# 当系统的物理内存不够用的时候，就需要将物理内存中的一部分空间释放出来，以供当前运行的程序使用。那些被释放的空间可能来自一些很长时间没有什么操作的程序，这些被释放的空间被临时保存到Swap空间中，等到那些程序要运行时，再从Swap中恢复保存的数据到内存中。这样，系统总是在物理内存不够时，才进行Swap交换。
#
# sudo cat /proc/sys/vm/swappiness
#
# 该值默认值是60.
#
# swappiness=0的时候表示最大限度使用物理内存，然后才是 swap空间，
#
# swappiness＝100的时候表示积极的使用swap分区，并且把内存上的数据及时的搬运到swap空间里面。
#
# 　　--临时性修改：
# 　　　　[root@rhce ~]# sysctl vm.swappiness=10
# 　　　　vm.swappiness = 10
#
# 　　　[root@rhce ~]# cat /proc/sys/vm/swappiness
# 　　　　10
# 　　　　这里我们的修改已经生效，但是如果我们重启了系统，又会变成60.
#  　　--永久修改：
# 　　　　在/etc/sysctl.conf 文件里添加如下参数：
# 　　　　vm.swappiness=10


# 语言环境
#
# 查看是否安装了中文支持
# locale -a
# 如果有 zh_CN.utf8 则表示系统已经安装了中文locale，如果没有则需要安装相应的软件包。安装方式如下：
# sudo apt-get install language-pack-zh-hans language-pack-zh-hans-base
#
#
#
# 软件管理 apt ( Advanced Packaging Tool ) , 他可以自动下载、配置、安装软件包；简化了Linux系统上的。Debian及衍生版中都包含了apt ， RedHat系列的linux的则使用yum来进行管理，其中Fedora22中Centos7中开始使用dnf 来替代yum。
#
# apt-cache search package 搜索包
# apt-cache show package 获取包的相关信息，如说明、大小、版本等
# sudo apt-get install package 安装包
# sudo apt-get install package –reinstall 重新安装包
# sudo apt-get -f install 强制安装
# sudo apt-get remove package 删除包
# sudo apt-get remove package –purge 删除包，包括删除配置文件等
# sudo apt-get autoremove 自动删除不需要的包
# sudo apt-get update 更新源
# sudo apt-get upgrade 更新已安装的包
# sudo apt-get dist-upgrade 升级系统
# sudo apt-get dselect-upgrade 使用 dselect 升级
# apt-cache depends package 了解使用依赖
# apt-cache rdepends package 了解某个具体的依赖
# sudo apt-get build-dep package 安装相关的编译环境
# apt-get source package 下载该包的源代码
# sudo apt-get clean && sudo apt-get autoclean 清理下载文件的存档
# sudo apt-get check 检查是否有损坏的依赖
#
#
# apt的配置文件
#
# /etc/apt/sources.list 设置软件包的获取来源
# /etc/apt/apt.conf apt配置文件
# /etc/apt/apt.conf.d apt的零碎配置文件
# /etc/apt/preferences 版本参数
# /var/cache/apt/archives/partial 存放正在下载的软件包
# /var/cache/apt/archives 存放已经下载的软件包
# /var/lib/apt/lists 存放已经下载的软件包详细信息
# /var/lib/apt/lists/partial 存放正在下载的软件包详细信息


# date ： 用来显示或设定系统的日期和与时间
#
# date //显示当前日期
# # 日期格式化
# #       %Y     year
# #       %m     month (01..12)
# #       %d     day of month (e.g., 01)
# #       %H     hour (00..23)
# #       %I     hour (01..12)
# #       %M     minute (00..59)
# #       %S     second (00..60)
# date +"%Y%m%d %H%M%S"
# 223856
# date +"%Y-%m-%d %H:%M:%S"
#     2016-08-24 22:39:07
#
# date -s //设置当前时间，只有root权限才能设置，其他只能查看。
# date -s 20061010 //设置成20061010，这样会把具体时间设置成空00:00:00
# date -s 12:23:23 //设置具体时间，不会对日期做更改
# date -s “12:12:23 2006-10-10″ //这样可以设置全部时间
#
# # 注意： 重新设置时间后需要将时间捅不到硬件时钟。方式如下：
# hwclock -w
#
#
# cal : 显示一个日历
# cal  #  现实当前月份的日历
# cal -y  # 显示当年的日历
# cal 2016 #  # 显示指定年份的日历
#
# 设置时区
# tzselect
#
#
# 修改密码：
# # 修改密码的命令
# passwd # 默认修改当前用户的密码
# passwd username # 修改指定用户的密码，需要管理员权限
#
#
# 忘记密码
# 开始时长按shift键，进入grub菜单-->  按字母e 进入编辑模式 --> 编辑内容--> 启动 进入但用户模式 ，重新设置用户密码，-->  按照F10重启 -- >  使用新密码进入系统
#
#
#
# 注销/重启/关机
# logout  # 注销
# reboot  # 重启系统： 需要管理员全新啊
# shutdown # 关机： 需要管理员权限
# shutdown -r now # 现在立即重启
# shutdown -r +5  # 三分钟后重启
# shutdown -r 12:12    #在12:12时将重启计算机
#
# shutdown -h now # 现在立即关机
# shutdown -h +5  “The System will shutdown after 3 minutes”   # 提示使用者将在三分钟后关机
# shutdown -h +5   #  5分钟后关机
# shutdown -h 12:00  # 12点钟关机
# shutdown -c   # 取消关机操作

# cd  ： 切换目录
# cd  # 回到当前用户的家目录
# # ～  可用于表示用户家目录
# cd  /etc # 切换到/etc目录
#
# cd - # 切换到上一次的目录
#
#
# pwd ： 查看当前的工作路径
#
#
# 创建目录：
# # mkdir 目录名
# mkdir my_dir
#
# # - p 参数 : 递归创建目录，用于同时创建多级目录
# mkdir   a/b/c/d
#
#
# 获取帮助
#  -h  --help  info  man
# man man  # 查看man命令的手册
# man  cd
# man  pwd
# man 5 passwd
# man -k passwd # 模糊查找
# man -f  passwd  # 精确查找
#
# 创建文件
#
# touch ： 改变文件或目录的时间，文件不存在时会创建一个空文件。
# touch file1 # file1 不存在时被创建
# touch -c file1 # 不创建文件
# touch -r ref_file file1  更新file1.txt的时间戳和ref+file相同
# touch -t 201210120505.25 file1
#
# #  -t  time 使用指定的时间值 time 作为指定文件相应时间戳记的新值．此处的 # # time规定为如下形式的十进制数:
# #  [[CC]YY]MMDDhhmm[.SS]
# #   这里，CC为年数中的前两位，即”世纪数”；YY为年数的后两位，即某世纪中的年数．如果不给出CC的值，则touch   将把年数CCYY限定在1969--2068之内．MM为月数，DD为天将把年数CCYY限定在1969--2068之内．MM为月数，DD为天数，hh 为小时数(几点)，mm为分钟数，SS为秒数．此处秒的设定范围是0--61，这样可以处理闰秒．这些数字组成的时间是环境变量TZ指定的时区中的一个时 间．由于系统的限制，早于1970年1月1日的时间是错误的。
#
# 注意： 如果文件以 ”.“ 开头，则表示文件是隐藏文件。
#
#
# 删除：
# rm   ： 删除命令
# rm -f  file1 # 强制删除文件
# rm -r  a/b/file1  # 删除指定目录及其下的所有文件和目录
# rm -rf  a/b/file1  #  强制删除指定目录及其下的所有文件和目录
# # rm 命令太危险，不建议使用
#
#
# mv  ： 移动或重命令文件或目录
# mv
# SOURCE
# DEST  #
#
# mv
# test.log
# test.txt  # 文件改名
# mv
# test1.txt
# dir1 /  # 移动文件
#
# mv
# test1.txt
# test2.tx
# test3.tx
# dir1 /  # 移动多个文件
#
#
# cp ： 复制
# cp SOURCE DEST # 复制文件
# cp -i  SOURCE DEST  #   如果遇到需要覆盖的情况，则提示
# cp -r  dir1  dir2  # 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名
# cp -p  file1 file2  #  此时cp除复制源文件的内容外，还将把其修改时间和访问权限也复制到新文件中。
# cp -rp dir1  dir2
#
#
# stat : 查看文件相信信息
# stat filename
# #  Access time(atime):是指取用文件的时间，所谓取用，常见的操作有：使用编辑器查看文件内容，使用cat命令显示文件内容，使用cp命令把该文件（即来源文件）复制成其他文件，或者在这个文件上运用grep sed more less tail head 等命令，凡是读取而不修改文件的操作，均衡改变文件的Access time.
# #  Modify time(mtime)：是指修改文件内容的时间，只要文件内容有改动（如使用转向输出或转向附加的方式）或存盘的操作，就会改变文件的Modify time,平常我们使用ls –l查看文件时，显示的时间就是Modify time
# #  Change time(ctime):是指文件属性或文件位置改动的时间，如使用chmod，chown,mv指令集使用ln做文件的硬是连接，就会改变文件的Change time.

# cat : 链接文件后输出文件内容到屏幕上，其实就是查看文件内容
#
# tac : 反转行的输出
#
# cat file1  #显示 file1的文件内容
# cat file1 file2   # 显示file1和file2的文件内容
# cat -n file1  #  由1开始对所有输出的行数编号
# cat -s file  # 当遇到连续2行以上的空白行，只保留一行空白行
#
# wc   :统计指定文件中的字节数、字数、行数，并将统计结果显示输出
# -c 统计字节数。
# -l 统计行数。
# -m 统计字符数。这个标志不能与 -c 标志一起使用。
# -w 统计字数。一个字被定义为由空白、跳格或换行字符分隔的字符串
#
# sort ： 排序
# sort [-fbMnrtuk] [file or stdin]
# 选项与参数：
# -f  ：忽略大小写的差异，例如 A 与 a 视为编码相同；
# -b  ：忽略最前面的空格符部分；
# -n  ：使用『纯数字』进行排序(默认是以文字型态来排序的)；
# -r  ：反向排序；
# -u  ：就是 uniq ，相同的数据中，仅出现一行代表；
# -t  ：分隔符，默认是用 [tab] 键来分隔；
# -k  ：以那个区间 (field) 来进行排序的意思

# uniq ： 忽略或报告重复行
# uniq [-icu]
# 选项与参数：
# -i   ：忽略大小写字符的不同；
# -c  ：进行计数
# -u  ：只显示唯一的行
#
# cut命令可以从一个文本文件或者文本流中提取文本列。
# 选项与参数：
# -d  ：后面接分隔字符。与 -f 一起使用；
# -f  ：依据 -d 的分隔字符将一段信息分割成为数段，用 -f 取出第几段的意思；
# -c  ：以字符 (characters) 的单位取出固定字符区间；
#
# tee ： 读取标准输入的数据，并将其内容输出成文件。
# cat sec.log | tee file1  # 读取sec.log ，并生成file1文件
# cat sec.log | tee - a file1  # 读取sec.log ，并追加，
# cat sec.log | tee file1 file2
#
# history ： 查看执行过的命令。
# history  # 显示最近1000条历史命令
# history 5   # 显示最后5条命令
# !number# number为history之后命令前的序号：执行该条命令
# !cat # 执行最后一条以cat开头的命令
#
# more ：   查看文件内容
#
# less  ： 查看文件内容
#
# head ： 输出文件的开始的部分， 可以指定行数 , 默认显示10行
# head -n 5 file
#
# tail  ：   查看文件尾部的内容。默认显示最后10行
# tail file1
# tail -n 5 file1
# tail -f file1  # 动态监控文件
#
# which # 查找其他命令的位置
# which ls


# ls ： 列出目标目录中所有的子目录和文件
#
# 格式：ls [选项] [目录名]
#
# -a 用于显示所有文件和子目录(保罗点文件)。
#
# -l 除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来。
#
# -r 将目录的内容清单以英文字母顺序的逆序显示。
#
# -t 按文件修改时间进行排序，而不是按文件名进行排序。
#
# -A 同-a，但不列出“.”(表示当前目录)和“..”(表示当前目录的父目录)。
#
# -F 在列出的文件名和目录名后添加标志。例如，在可执行文件后添加“*”，在目录名后添加“/”以区分不同的类型。
#
# -R 如果目标目录及其子目录中有文件，就列出所有的文件。
#
# . 和..
#
# . 表示当前目录
#
# .. 表示父目录
#
#
# ls  # 列出当前目录下的文件和目录
# ls  . # 列出当前目录下的文件和目录
# ls ..   # 列出当前目录的父目录下的文件和目录
# ls  /etc    # 列出/etc目录下的文件和目录
#
# ls -l  # 以长格式显示文件信息
# 总用量 76
# -rwxrwxrwx 1 will will    78 5月  13 18:11 ss_start.sh
#
#
# 文件类型
#
# -  普通文件
#
# d  目录文件
#
# b 块设备文件
#
# c  字符设备文件
#
# l  链接文件
#
# p 管道文件
#
# s  socket文件
#
#
# ls -l  /dev  # 可以查看字符设备文件和块设备文件
# ls -l  /run  #  可以找到socket文件
# ls -l  /run/systemd/inhibit/ # 可以查看到管道文件
#
# 文件权限
# rwxrwxr-- ： 三组rwx 分别表示 所有者、所有组、其他人 的权限。
#
# r ： 表示可读, 可以用数字 4 来表示
# w ： 标识可写 ，可以用数字 2 来表示
# x ： 表示可执行 ， 可以用数字 1 来表示
# - ：表示没有相应权限  可以用数字 0 来表示
#
# chmod o+w  file1
# chmod g-w file1
# chmod go-w file1
# chmod u=rwx file1
#
# chmod 755  file1  # -rwxr-xr-x (755) 只有所有者才有读，写，执行的权限，组群和其他人只有读和执行的权限
# chmod 644  #  -rw-r--r-- (644) 只有所有者才有读和写的权限，组群和其他人只有读的权限
#
#
# #  其中：
# #  u 代表所有者（user）
# #  g 代表所有者所在的组群（group）
# #  o 代表其他人，但不是u和g （other）
# #  a 代表全部的人，也就是包括u，g和o
#
# 目录上的权限：
#
# r ：  表示是否可以读取目录下的文件名
#
# w ：  表示是否可以在目录下创建修改文件
#
# x  ： 表示目录是否可以被搜索
#
# 有x权限后，就可以使用  ./a.py 的方式执行文件

