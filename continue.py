#__author__:'Faning Huang'
#__time__:'2017/11/3 0003 下午 9:20'

#continue 结束本次循环，继续下一次循环
#break 跳出整个当前的循环

exit_flag = False

for i in range(10):
    if i <5:
        continue
    print(i)
    for j in range(10):
        print("layer2",j)
        if j ==6:
            exit_flag=True
            break
    if exit_flag:
        break