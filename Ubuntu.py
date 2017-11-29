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
