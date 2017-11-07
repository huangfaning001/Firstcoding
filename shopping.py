#__author__:'Faning Huang'
#__time__:'2017/11/6 0006 下午 10:27'

# salary = int(input("Please input your salary: "))
#
# msg = '''
# ---------The shopping list------------
# 1, iphoneX 8888
# 2, macbook 9999
# 3, coffee 99
# 4, python book 88
# 5, bicyle 1999
# -----------------END------------------
# '''
# print(msg)
#
# want_buy_shopping = int(input("Please you want to buy shopping ordinal number: "))
#
# if want_buy_shopping == 1:
#      print("You should pay: "+str(want_buy_shopping),"Your banlance have: "+str(salary-want_buy_shopping))
# else:
#     print("Please input ordinal number")




product_list = [('iphoneX',8888),('macbook',9999),('coffee',99),('python book',88),('bicyle',1999)]

salary = input("Please input your salary: ")
shopping_car = []
if salary.isdigit():
    salary = int(salary)
    while True:
        #打印商品内容
        for i,v in enumerate(product_list,1):#enumerate会将数组或列表组成一个索引序列,使我们再获取索引和索引内容的时候更加方便
            print(i,">>>>",v)
            #引导用户选择商品
        chioce = input("Please select the purchase ID[quit:q]：")
        #验证输入是否合法
        if chioce.isdigit():
                chioce = int(chioce)
                if chioce>0 and chioce<=len(product_list):
                    #将用户选择商品通过choice取出来
                    p_item=product_list[chioce-1]
                    #如果钱够，用本金salary减去该商品价格，并将该商品加入购物车
                    if p_item[1] <= salary:
                        salary-=p_item[1]
                        shopping_car.append(p_item)
                    else:
                        print("Lack of balance!!!Remain %s yet"%salary)
                        #循环遍历购物车里的商品，购物车存放的是已买商品
                    print(p_item)
                else:
                    print('Encoding does not exist')
        elif chioce == 'q':
                print('------You have purchased the following items--------')
                for i in shopping_car:
                    print(i)
                print('You still have %s RMB'%salary)
                break
        else:
            print("Invalid input")
else:
    print("Invalid input")

# list_of_goods = [
#     ('iphoneX',8888),
#     ('macbook',9999),
#     ('ipad',3333),
#     ('python book',99),
#     ('coffee',88),
#     ('earphone',666)
# ]
#
# wages = input("Please input your wages: ")
# shopping_cart = []
# if wages.isdigit():
#     wages=int(wages)
#     while True:
#         for i,v in enumerate(list_of_goods,1):
#             print(i,'>>>>',v)
#             select = input('Please input product ID!![quit:q]: ')
#             if select.isdigit():
#                 select=int(select)
#                 if select>0 and select <=len(list_of_goods):
#                     p_item = list_of_goods[select-1]
#                     if p_item[1] <= wages:
#                         wages -=p_item[1]
#                         shopping_cart.append(p_item)
#                     else:
#                         print("Your balance is insufficient")
#                     print(p_item)
#                 else:
#                     print('Encoding does not exist')
#             elif select =='q':
#                 print('-----------You have purchased the following items--------------')
#                 for i in shopping_cart:
#                     print(i)
#                 print('You still have %s RMB'%wages)
#                 break
#             else:
#                 print('nvalid input')
# else:
#     print('nvalid input')

