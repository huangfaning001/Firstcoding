
#line = 9

#while line>0:
#    tmp = line
#    while tmp>0:
#        print("*",end="")
#        tmp -= 1
#    print()
#    line -= 1

first = 1

while first<=9:
    sec = 1
    while sec <= first:
        print(str(sec)+"*"+str(first)+"="+str(sec*first),end="\t")
        sec +=1
    print()
    first +=1
