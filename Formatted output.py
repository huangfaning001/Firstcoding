#__author__:'Faning Huang'
#__time__:'2017/10/31 0031 下午 8:39'


#占位符 %
#  %s   s = string 字符串
#  %d   d = digit 整数
#  %f   f = float 浮点数，约等于小数

name = input("Input your name: ")
age = int(input("Input your age: "))
job = input("Input your job: ")
salary = input("Input your salary: ")

if salary.isdigit():   #长的像不像数字,比如200d, '200'
    salary = int(salary)

# else:
#    #print()
#    exit("Must input digit")  #退出程序


msg = '''
--------INFO OF %s--------
name: %s
age: %d
job: %s
salary: %d
You will be retired in %s years !
---------------END----------------
'''% (name,name,age,job,salary,65-age)
print(msg)