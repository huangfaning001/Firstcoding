#__author__:'Faning Huang'
#__time__:'2017/11/1 0001 下午 8:35'

_user = "huangfaning"
_passwd ="123456"

for i in range(3):
    username = input("Username: ")
    password = input("Password: ")
    if username == _user and password == _passwd:
        print("Welcome %s login...."%_user)
        break #终止，中断
    else:
        print("Invalid username or password!")

    # for i in range(1,100,2): #  2  步长
    #     print("loop:",i)