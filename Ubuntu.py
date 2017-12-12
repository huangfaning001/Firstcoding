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


# chown ： 更改文件的所有者和所有组
# chown root:root  file
# chown root   file
# chown :root   file
#
# 特殊权限
#
# SUID：    让一般用户在执行某些程序的时候，能够暂时具有该程序拥有者的权限，SUID对目录是无效的
#
# SGID ：  文件：如果SGID设置在二进制文件上，则不论用户是谁，在执行该程序的时候，它的有效用户组（effective
# group）将会变成该程序的用户组所有者（group
# id）；    目录：如果SGID是设置在某目录上，则在该目录内所建立的文件或目录的用户组，将会是该目录的用户组。  SGID多用在特定的多人团队的项目开发上，在系统中用得较少
#
# STICKY ： 只针对目录有效，在具有SBit的目录下，用户若在该目录下具有w及x权限，则当用户在该目录下建立文件或目录时，只有文件拥有者与root才有权力删除。
#
# rwsrw - r - -  表明有suid标识，
# rwxrws - -- 表明有sgid标识，
# rwxrw - rwt
# 表明有stick标识，
# 当设置了特别权限位时，如果原来这个位上有x，那么这个特殊标示就显示为小写字母s, s, t ，否者就显示为大写S, S, T，此时他们不生效。
#
# 用户和用户组
#
# linux使用文件保存用户信息 ：
#
# 文件
# #      /etc/passwd 用户账户信息。
# #       /etc/shadow 安全用户账户信息。
# #       /etc/group 组账户信息。
# #       /etc/gshadow 安全组账户信息。
# #       /etc/default/useradd 账户创建的默认值。
# #       /etc/skel/ 包含默认文件的目录。
# #       /etc/login.defs Shadow 密码套件配置。
#
# useradd：  添加用户
# # -c 备注 加上备注。并会将此备注文字加在/etc/passwd中的第5项字段中
# #  -d 用户主文件夹。指定用户登录所进入的目录，并赋予用户对该目录的的完全控制权
# #  -e 有效期限。指定帐号的有效期限。格式为YYYY-MM-DD，将存储在/etc/shadow
# #  -f 缓冲天数。限定密码过期后多少天，将该用户帐号停用
# #  -g 主要组。设置用户所属的主要组  www.cit.cn
# #  -G 次要组。设置用户所属的次要组，可设置多组
# # -M 强制不创建用户主文件夹
# #  -m 强制建立用户主文件夹，并将/etc/skel/当中的文件复制到用户的根目录下
# #  -p 密码。输入该帐号的密码
# #  -s shell。用户登录所使用的shell

# #  -u uid。指定帐号的标志符user id，简称uid
#
# useradd user1 # 添加用户 user1
# useradd  -d /home/userTT user2
#
# userdel : 删除用户
# userdel  user1  #
# userdel -r user1
#
# #  -r, --remove   用户主目录中的文件将随用户主目录和用户邮箱一起删除。在其它文件系统中的文件必须手动搜索并删除。
# #    -f, --force    此选项强制删除用户账户，甚至用户仍然在登录状态。它也强制删除用户的主目录和邮箱，即使其它用户也使用同一个主目录或邮箱不属于指定的用户
#
# usermod : 修改用户信息
# #　-c<备注> 　修改用户帐号的备注文字。
# #　-d登入目录> 　修改用户登入时的目录。
# #　-e<有效期限> 　修改帐号的有效期限。
# #　-f<缓冲天数> 　修改在密码过期后多少天即关闭该帐号。
# #　-g<群组> 　修改用户所属的群组。
# #　-G<群组> 　修改用户所属的附加群组。
# #　-l<帐号名称> 　修改用户帐号名称。
# #　-L 　锁定用户密码，使密码无效。
# #　-s<shell> 　修改用户登入后所使用的shell。
# #　-u<uid> 　修改用户ID。
#
#
# #　-U 　解除密码锁定。
#
# usermod -G staff user2  # 将 newuser2 添加到组 staff 中
# usermod -l newuser1 newuser  # 修改 newuser 的用户名为 newuser1
# usermod -L newuser1  # 锁定账号 newuser1
# usermod -U newuser1  # 解除对 newuser1 的锁定
#
#
# groupadd : 添加组
# groupadd group1
# groupadd -g  1000 group1  # 指定gid
#
# groupdel ： 删除组
# groupdel group1 # 删除组

# su与 sudo
# su  : 切换用户，没有参数时，默认切换为root用户；
# su   # 切换为root
#
# ## 推荐
# su -   # 切换为root 并加载user1的环境配置
# su -  user1 # 切换为user1 并加载user1的环境配置
#
# sudo ：   让当前用户暂时以管理员的身份root来执行命令。
#
# Ubuntu 默认没有启用root用户， 普通用户执行一些特殊的操作时，使用sudo就可以让普通用户以root用户的身份执行命令
# sudo有一个配置文件： /etc/sudoers  ;  通过修改配置文件可以让指定用户使用sudo命令
#
# man sudoers # 查看man手册
# 看下面几行：
# # Host alias specification # 配置Host_Alias：就是主机的列表
# Host_Alias      HOST_FLAG = hostname1, hostname2, hostname3
# # User alias specification # 配置User_Alias：就是具有sudo权限的用户的列表
# User_Alias USER_FLAG = user1, user2, user3
#
# # Cmnd alias specification # 配置Cmnd_Alias：就是允许执行的命令的列表，命令前加上!表示不能执行此命令.命令一定要使用绝对路径，避免其他目录的同名命令被执行，造成安全隐患 ,因此使用的时候也是使用绝对路径!
# Cmnd_Alias      COMMAND_FLAG = command1, command2, command3 ，!command4
#
# # 配置Runas_Alias：就是用户以什么身份执行（例如root，或者oracle）的列表
# Runas_Alias RUNAS_FLAG = operator1, operator2, operator3
#
#
# # User privilege specification
# # 配置权限的格式如下：
# #  USER_FLAG HOST_FLAG=(RUNAS_FLAG) COMMAND_FLAG
#
# root    ALL=(ALL:ALL) ALL
# 如果不需要密码验证的话，则按照这样的格式来配置
# USER_FLAG HOST_FLAG=(RUNAS_FLAG) NOPASSWD: COMMAND_FLAG
#
#
# 格式为：用户名(用户别名) 主机名(主机别名)=[(运行用户或是Runas_Alias)可选] [tag可选]  可以执行的命令(或Cmmd_Alias)  这样描述语法很生硬，不易理解，举例子
# user1  host1 = /bin/kill　# user1 可以在host1上使用命令/bin/kill
# user1  host1 = NOPASSWD: /bin/kill　# user1 可以在host1上使用命令/bin/kill 同时可以不必输入密码(这里就是使用了NOPASSWD　# 这个tag，默认是PASSWD)
# user1  host1 = NOPASSWD: /bin/kill , PASSWORD: /bin/ls　# user1 可以在host1上使用命令/bin/kill无需输入密码，但是使用/bin/ls则需要输入密码
# user1  host1 = (opterator) /bin/kill　# user1 可以在host1上使用命令/bin/kill但是必须是以operator用户运行这个命令，等价于# su -u opertor /bin/kill
# user1  host1 = (:group_name) /bin/kill　# user1 可以在host1上使用命令/bin/kill,且必须以group_name这个用户群组里面的用户来运行。
# %group_name host1 = /bin/kill　# 所有group_name里面的用户都可以在host1上执行/bin/kill(Linux中一般代表整个用户群组用# %group_name)
# 再举个实际例子，我之前对sudo su这个命令不理解，为什么我可以直接就su到root用户了呢，连密码都不需要？查看了一下sudoers文件才知道原来里面有这么一行：
# xxx     ALL=NOPASSWD: /bin/su

# alias : 给命令起别名
# alias ll='ls -alF'
# alias la='ls -A'
# alias l='ls -CF'
# 如果需要别名永久生效，需要保存到 .bashrc 文件
#
# 我们用到的终端默认使用的shell
# 是bash
# 其他的shell
# 有dash  、csh 、tcsh、zsh等等
#
# Shell本身是一个用C语言编写的程序，它是用户使用Unix / Linux的桥梁，用户的大部分工作都是通过Shell完成的。Shell既是一种命令语言，又是一种程序设计语言。作为命令语言，它交互式地解释和执行用户输入的命令；作为程序设计语言，它定义了各种变量和参数，并提供了许多在高级语言中才具有的控制结构，包括循环和分支。
#
# 自定义账户的个性化环境的三个重要文件
#
# .bash_history.bash_logout.bashrc
#
# 刚登录Linux时，首先启动 / etc / profile
# 文件, ~ /.bash_profile、 ~ /.bash_login、 ~ /.profile。 如果
# ~ /.bash_profile文件存在的话，一般还会执行
# ~ /.bashrc文件。
#
# 关于各个文件的作用域，在网上找到了以下说明：
# （1） / etc / profile： 此文件为系统的每个用户设置环境信息, 当用户第一次登录时, 该文件被执行.并从 / etc / profile.d目录的配置文件中搜集shell的设置。
# （2） / etc / bashrc: 为每一个运行bash
# shell的用户执行此文件.当bash
# shell被打开时, 该文件被读取（即每次新开一个终端，都会执行bashrc）。
# （3） ~ /.bash_profile: 每个用户都可使用该文件输入专用于自己使用的shell信息, 当用户登录时, 该文件仅仅执行一次。默认情况下, 设置一些环境变量, 执行用户的.bashrc文件。
# （4） ~ /.bashrc: 该文件包含专用于你的bash
# shell的bash信息, 当登录时以及每次打开新的shell时, 该该文件被读取。
# （5） ~ /.bash_logout: 当每次退出系统(退出bash
# shell)时, 执行该文件.另外, / etc / profile中设定的变量(全局)
# 的可以作用于任何用户, 而
# ~ /.bashrc等中设定的变量(局部)
# 只能继承 / etc / profile中的变量, 他们是
# "父子"
# 关系。（6） ~ /.bash_profile: 也可能是.profile
# 是交互式、login
# 方式进入
# bash
# 运行的
# ~ /.bashrc
# 是交互式
# non - login
# 方式进入
# bash
# 运行的通常二者设置大致相同，所以通常前者会调用后者。
#
# PATH变量的设置
#
# env: 查看当前环境变量
#
# export: 设置或显示环境变量。
#
# source: 在当前bash环境下读取并执行FileName中的命令。该filename文件可以无
# "执行权限"
#
# env
# export name = "SN"
# source /etv/profile
#
# echo
# echo会将输入的字符串送往标准输出。输出的字符串间以空白字符隔开并在最后加上换行号。
#
# 　　　-n
# 不要在最后自动换行
# 　　　-e
# 若字符串中出现以下字符，则特别加以处理，而不会将它当成一般
# 　　　　 　 文字输出：
# 　　　　 　 \a
# 发出警告声；
# 　　　　 　 \b
# 删除前一个字符；
# 　　　　 　 \c
# 最后不加上换行符号；
# 　　　　 　 \f
# 换行但光标仍旧停留在原来的位置；
# 　　　　 　 \n
# 换行且光标移至行首；
# 　　　　 　 \r
# 光标移至行首，但不换行；
# 　　　　 　 \t
# 插入tab；
# 　　　　 　 \v
# 与\f相同；
#
#
#
#
#
# 管道符
#
# 管道符
# 就是 |  ：他的作用是
# 将前一个命令的结果
# 交给后一个命令使用
#
# 重定向
#
# > 重定向，如果的文件存在，则覆盖文件内容，文件不存在时创建文件
#
# >> 重定向，如果的文件存在，则向文件追加内容，文件不存在时创建文件
#
# 1 > 标准正确输出，同上
#
# 1 >> 标准正确输出，同上
#
# 2 > 标准错误输出，同上
#
# 2 >> 标准错误输出，同上
#
# & > 标准正确输出和标准错误输出，同上

#
# locate # 查找文件
# locate /etc/sh   # 搜索etc目录下所有以sh开头的文件。
# locate ~/a   # 搜索用户主目录下，所有以a开头的文件。
# locate -i ~/a   # 搜索用户主目录下，所有以a开头的文件，并且忽略大小写

find
使用方法： 
find   path   -option   [-print ]   [ -exec  -ok  command ]  {} \;

######  根据文件名查找 #######
find / -name filename 再根目录里面搜索文件名为filename的文件
find /home -name "*.txt"
find /home -iname "*.txt"  # 忽略大小写


######  根据文件类型查找 #######
find . -type 类型参数
f 普通文件
l 符号连接 
d 目录 
c 字符设备 
b 块设备 
s 套接字 
p Fifo


######  根据目录深度查找 #######
find . -maxdepth 3 -type f  # 最大深度为3
find . -mindepth 2 -type f  # 最小深度为2

#########   根据文件的权限或者大小名字类型进行查找 ###########

find . -type f -size (+|-)文件大小 # +表示大于 -表示小于 
b —— 块（512字节） 
c —— 字节 
w —— 字（2字节） 
k —— 千字节 
M —— 兆字节 
G —— 吉字节


#########   按照时间查找  ############

-atime（+|-）n  # 此选项代表查找出n天以前被读取过的文件。
-mtime（+|-）n  # 此选项代表查找出n天以前文件内容发生改变的文件。
-ctime（+|-）n  # 此选项代表查找出n天以前的文件的属性发生改变的文件。
-newer file  # 此选项代表查找出所有比file新的文件。
-newer file1 ! –newer file2  # 此选项代表查找比file1文件时间新但是没有file2时间新的文件。

# 注意：   
#  n为数字，如果前面没有+或者-号，代表的是查找出n天以前的，但是只是一天之内的范围内发生变化的文件。
#  如果n前面有+号，则代表查找距离n天之前的发生变化的文件。如果是减号，则代表查找距离n天之内的所有发生变化的文件。
#  -newer file1 ! –newer file2中的!是逻辑非运算符

#########   按照用户/权限查找  ############

-user 用户名：根据文件的属主名查找文件。
-group 组名：根据文件的属组名查找文件。
-uid n：根据文件属主的UID进行查找文件。
-gid n：根据文件属组的GID进行查找文件。
-nouser：查询文件属主在/etc/passwd文件中不存在的文件。
-nogroup：查询文件属组在/etc/group文件中不存在的文件
-perm 777： 查询权限为777的文件

来自: http://man.linuxde.net/find

########  查找时指定多个条件   ############

-o：逻辑或，两个条件只要满足一个即可。
-a：逻辑与，两个条件必须同时满足。

find  /etc -size +2M -a -size -10M


#########  对查找结果进行处理  #############
-exec  shell命令  {}  \;
-ok  shell命令  {}  \;
其中-exec就是代表要执行shell命令，后面加的是shell指令，再后面的“{}”表示的是要对前面查询到的结果进行查询，最后的“\；”表示命令结束。需要注意的是“{}”和“\”之间是要有空格的。而-ok选项与-exec的唯一区别就是它在执行shell命令的时候会事先进行询问，-print选项是将结果显示在标准输入上

find /home -name  “*.txt” -ok ls -l {} \;
find /home -name  “*.txt” -ok rm {} \;

df
-T : 显示文件系统类型
-h ： 以能显示的最大单位显示

df -Th


du
-s ： 如果后面是目录，只显示一层
-h : 以能显示的最大单位显示

du dirname # 显示dirname下所有目录及其子目录的大小

du -sh dirname  显示dirname的大小



mount / umount 3 挂载和卸载设备
mount # 查询挂在设备及属性

# 挂载光盘
mount -t iso9660 /dev/cerom /mnt
mount /dev/sr0 /mnt  


# 重新挂载设备
mount -o remount,rw /mnt  # 重新挂载设备并设置rw属性

# 挂载iso文件
mount  a.iso -o loop /mnt 


umount /mnt # 卸载设备
umount -l /mnt # 强制卸载

