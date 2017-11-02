#__author__:'Faning Huang'
#__time__:'2017/11/2 0002 下午 9:31'

_user = "huangfaning"
_passwd ="123456"

counter = 0

while counter<3:  #当while 后面的条件成立（True），才会执行它下面的代码
    username = input("Username: ")
    password = input("Password: ")
    if username == _user and password == _passwd:
        print("Welcome %s login...."%_user)
        break #终止，中断
    else:
        print("Invalid username or password!")

        counter+=1
    if counter == 3:
        keep_going_choice = input("还想玩吗？？？ y/n")
        if keep_going_choice == "y":
            counter = 0
else:
    print("要不要脸啊，臭流氓，%s" % _user)