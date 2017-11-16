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

