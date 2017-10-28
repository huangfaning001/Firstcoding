#print("hello,world!",end = "")
#print("hello,world!",end = "")
#print("hello,world!",end = "")

#num1 =0

#while num1 <=7:
#    print(num1,end = "_")
#    num2 =0
#    while num2 <=8:
#        print(num2,end = "-")
#        num2 +=1
		
#    num1 += 1
#    print() #print(end="\n") 

height = int(input("Height: "))
width = int(input("Width: "))


num_height = 1
while num_height<=height:
    num_width = 1
    while num_width<=width:
        print("#",end=" ")
        num_width+=1
    print()
    num_height += 1