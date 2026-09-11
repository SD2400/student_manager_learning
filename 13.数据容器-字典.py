# 字典-dict
# 字典的存储形式:字典存储的是键值对(key:value)类型的数据,可以根据键(key)找到对应的值(value)
# dict1 = {"王林" : 687, "李慕婉" : 690, "徐立国":674}
# print(dict1)
# print(type(dict1))
# print(dict1["王林"])
#
# # 字典的特点:
# #存储的是键值对,key不可以重复(如果重复,那么后面的值将会覆盖前面的值),值可以修改
# dict2 = {0:12,2:23,2:54}     #key重复时后面的值将会覆盖前面的值
# print(dict2)
# dict2[0] = 90           #字典的值可以修改
# print(dict2)
#
# # 字典的注意事项
# # 字典的值可以是任意类型,但key必须是不可变类型,如:int,float,tuple,str等
# dict3 = {1:[1,2]}
# print(dict3)
# dict4 = {[1,2]:1}  #这个字典中key的类型是list,所以报错
# print(dict4)

# 字典是没有索引下表的,不能根据索引来获取字典值,只能根据key来获取
# dict5 = {"hello": "world"}
# print(dict5["hello"])


# 字典的常用操作---增删改查
# dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
# # 增--添加,字典名[key] = value (当字典中没有key时,会将此键值对添加进字典中)
# dict1["涛哥"] = 700
# print(dict1)
#
# # 改--修改,字典名[key] = value(当字典中存在key时,会将此原来key的值修改为value)
# dict1["涛哥"] = 720
# print(dict1)
#
# # 删--删除,    返回值=字典名.pop(key)       del 字典名[key]
# a=dict1.pop("涛哥")
# print(a)
# print(dict1)
# del dict1["王林"]
# print(dict1)
#
# # 查-查找
# # 字典名[key]------返回对应的值value
# print(dict1["韩立"])
#
# # 字典名.get(key)---返回对应的值value
# print(dict1.get("韩立"))
#
# # 字典名.keys()-----返回所有的key
# print(dict1.keys())
#
# # 字典名.values()----返回所有的value
# print(dict1.values())
#
# # 字典名.items()-----返回所有的键值对
# print(dict1.items())
#

# 遍历
# for a,b in dict1.items():  #直接遍历键值对
#     print(a,b)
#
#
# for a,b in dict1.items():
#     print(f"{a}:{b}")
#
# for key in dict1.keys():        #通过遍历key输出value
#     print(f"{key}",dict1[key])
#
# for key in dict1.keys():
#     print(f"{key}",dict1.get(key)) #通过遍历key输出value

# 案例
# 开发一个购物车管理系统,实现商品信息的添加,修改,删除,查询功能.系统使用字典结构存储商品数据,
# 通过控制台菜单与用户交互.具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称,以及该商品的价格,数量,保存该商品信息到购物车.
# 2.修改购物车:要求用户输入要修改的购物车商品名称,然后在提示该商品的价格,数量,输入完成后修改该商品信息
# 3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品.
# 4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商品数量:xxx".
# 5.退出购物车
print("欢迎使用购物系统!")
shopping = {}    #结构:shop = {"shopping_name":{"shopping_price":xxx,"shopping_num":xxx},xxx}
print("""
########################
#     添加购物车请输入1   #
#     修改购物车请输入2   #
#     删除购物车请输入3   #
#     查询购物车请输入4   #
#     退出购物车请输入5   #
########################
      """)
a = int(input("请输入您要使用的功能(1-5):"))
if a == 1:     #添加购物车
    goods_name=input("请输入商品名称:")
    goods_price=float(input("请输入商品价格:"))
    goods_num=int(input("请输入商品数量:"))
    if goods_name in shopping:
        print("该商品已存在,请重新输入")
    else:
        shopping[goods_name]={"price":goods_price,"num":goods_num }
        print("商品已加入购物车!")

elif a == 2:   #修改购物车
    goods_name = input("请输入要修改的商品名称:")
    goods_price = float(input("请输入商品最终的价格:"))
    goods_num = int(input("请输入商品最终的数量:"))
    if goods_name not in shopping:
        print("该商品不存在,请重新输入")
    else:
        shopping[goods_name] = {"price": goods_price, "num": goods_num}
        print("商品已修改")
elif a == 3:   #删除购物车
    goods_name = input("请输入要删除的商品名称:")
    if goods_name not in shopping:
        print("商品不存在,请重新输入")
    else:
        del shopping[goods_name]
        print("商品删除完毕")
elif a == 4:   #查询购物车

elif a == 5:   #退出购物车


else:
    print("输入不符合规范,请重新输入!")


