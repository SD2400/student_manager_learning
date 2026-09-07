# #需求:根据输入的用户名密码执行登录操作,具体要求如下:
# 1.正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666
# 2.输入用户名和密码进行登录,直到登录成功,程序结束运行;如果登录失败,则继续输入用户名和密码进行登录
# 3.输入的用户名和密码不能为空!
# 4.登录成功:输出"登录成功,进入B站首页~"
# 5.登录失败:输出"用户名或密码错误,请重新输入!"

# 错误示范:
# 原因:input放在了循环外,当输入的用户名或密码不正确时,错误的用户名或密码会一直从新进行循环,导致一直输出错误的结果
# user_name = input("请输入用户名:")
# password = input("请输入密码:")
# while True:
#     if user_name == "admin" and password =="666888":
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "zhangsan" and password == "123456":
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "taoge" and password == "888666":
#         print("登录成功,进入B站首页")
#         break
#     elif user_name == "" or password == "":
#         print("输入的用户名和密码不能为空")
#         continue
#     else:
#         print("用户名或密码错误,请重新输入!")



# 正确示范
# while True:
#     user_name =input("请输入您的用户名:")
#     password = input("请输入您的密码:")
#     if user_name =="admin" and password == "666888" :
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "zhangsan" and password == "123456":
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "taoge" and password == "888666":
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "" or password == "":
#         print("输入的用户名和密码不能为空")
#         continue
#     else :
#         print("用户名或密码错误,请重新输入!")


# 例题
# 用户名密码登录,正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666,
# 5次登录机会,输入错误五次,不允许再操作了
# i = 1
# while i<=5:
#     user_name = input("请输入您的用户名:")
#     password = input("请输入您的密码:")
#     if user_name == "admin" and password == "666888" :
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name == "zhanngsan" and password =="123456":
#         print("登录成功,进入B站首页~")
#         break
#     elif user_name =="taoge" and password =="888666":
#         print("登录成功,进入B站首页~")
#         break
#     else:
#         print(f"登录失败,您还有{5-i}次机会!")
#         i += 1

# 例题
# 猜数字游戏
# 1.系统随机生成一个随机数       import random
#                            random_number = random.randint(a,b)     -->表示随机生成一个[a,b]范围内的数字
# 2.用户根据提示猜数字,并将所猜数字输入系统
# 3.如果猜错,系统给出提示是猜大了,还是猜小了,然后继续输入猜的数字
# 4.如果猜对,系统自动退出,游戏结束
# import random
# random_number = random.randint(1,100)
# while True:
#     num = int(input("请输入您要猜的数字:"))
#     if num == random_number:
#         print("恭喜你猜对了!")
#         break
#     else :
#         if num <random_number:
#             print("你猜小了")
#         else :
#             print("你猜大了")