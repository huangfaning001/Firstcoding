num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:")

max_num = 0

if num1>num2:
    max_num = num1
    if max_num > num3:
        print("max number is ",max_num)
    else:
        print("max number is ",num3)

else:
    max_num = num2
    if max_num > num3:
        print("max number is ",max_num)
    else:
        print("max number is",num3)

#if num1>num2: 
#    max_num= num1
#    if max_num > num3:
#        print("Max NUM is",max_num)
#    else:
#        print("Max NUM is",num3)
#else:
#    max_num = num2
#    if max_num > num3:
#        print("Max NUM is",max_num)
#    else:
#        print("Max NUM is",num3)