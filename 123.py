#__author__:'Faning Huang'
#__time__:'2017/11/16 0016 下午 9:10'

def register():
    f = open('login_info',"r+",encoding='utf-8')
    try:
        name = input("name: ")
        for line in f.readlines():
            if name in line:
                print("已存在")
                del name
                f.close()
                register()
                break
        else:
            password1 = input("password:")
            password2 = input("password again:")
            if password1 == password2:
                f.writelines("\n")
                f.write(name)
                f.write(":")
                f.write(password1)
                f.close()
            else:
                print("passwd1 != passwd2")
                register()
    except UnboundLocalError as e:
        pass

if _name_=="_main_":
    login_user = input("name>>")
    f1=open("black","r+",encoding="utf-8")
    for line in f.readlines():
        if login_user in line:
            user,passwd = line.strip('\n').split(':')
            for i in range(3):
                login_password = input("password>>")
                if login_user == user and login_password == passwd:
                    print("welcome %s login_user")
                    f.close()
                    break
                else:
                    f1 = open("black",encoding="utf-8")
                    f1.writelines('\n')
                    f1.writelines(login_user)
                    f1.close()
                    print("you are in black now")
                break
            else:
                print("没有注册，是否注册？1：注册  其他任意字符退出" )
                try:
                    choice = int(input("choose>>"))
                    if choice !=1:
                        pass
                    else:
                        retister()
                except ValueError as e:
                    pass



