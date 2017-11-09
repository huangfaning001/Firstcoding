#__author__:'Faning Huang'
#__time__:'2017/11/1 0001 下午 8:35'

# _user = "huangfaning"
# _passwd ="123456"
#
# passed_authentication = False # 假，不成立  (flag=标志位)

# for i in range(3):
#     username = input("Username: ")
#     password = input("Password: ")
#     if username == _user and password == _passwd:
#         print("Welcome %s login...."%_user)
#         passed_authentication = True #真，成立
#         break #终止，中断
#     else:
#         print("Invalid username or password!")
#
# if not passed_authentication :#只有在True的情况下，条件成立
#     print("要不要脸啊，臭流氓，%s"%_user)

    # for i in range(1,100,2): #  2  步长
    #     print("loop:",i)

#
# for i in range(3):
#     username = input("Username: ")
#     password = input("Password: ")
#     if username == _user and password == _passwd:
#         print("Welcome %s login...."%_user)
#         break #终止，中断  (break for 过后，就不会执行最后的else语句 )
#     else:
#         print("Invalid username or password!")
#
# else: #(只要上面的for循环正常执行完毕，中间没被打断，就会执行else语句)
#     print("要不要脸啊，臭流氓，%s"%_user)

#
# 实现简单的用户登录控制
i = 0
userName = 'Python'
userPassword = '123456'
while i<3:
    name = input("请输入用户名:")
    password = input("请输入密码:")
    if(name==userName and password==userPassword):
        print("登陆成功!")
        break
    elif(name==userName):
        print("密码有误,请重新输入!")
    elif(password == userPassword):
        print("用户名输入有误,请重新输入!")
    else:
        print("用户名和密码错误!")
        i+=1;
        print("温馨提示:您还有%d次登录机会"%(3-i))
print("今天登陆次数已达上限,今晚想想;明天再来哈!")
