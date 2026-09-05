#if条件判断,如果分数超过680,我就去清华读书
# num =float( input("请输入您的分数:"))
# if 750 >= num > 680 :
#     print("去清华")
# print("########################")

# #完成B站登录功能的实现(正确账号和密码为188888888和666888)
# a = int(input("请输入您的账号:"))
# b = int(input("请输入您的密码:"))
# if a== 188888888 and b==666888:
#     print("账号和密码正确,登录成功")
# if a != 188888888 or b!=666888 :
#     print("账号和密码错误,登陆失败")


###################################if....else###############################################3
#结构优化,用if...else 结构
# a = int(input("请输入您的账号:"))
# b = int(input("请输入您的密码:"))
# if a==188888888 and b==666888:
#     print("账号和密码正确,登陆成功")
# else :
#     print("账号和密码错误,登陆失败")
    
#根据用户输入的年份判断这一年是闰年还是平年
#非整百年,且能被4整除的年份是闰年
#整百年份必须能被400整除的是闰年
# year = int(input("请输入您要查询的年份:"))
# if (year % 100 !=0 and year % 4 ==0) or (year % 100 == 0 and year % 400 ==0):
#     print(f"{year}年是闰年")
# else:
#     print(f"{year}年是平年")

#根据用户输入的数字,判断该数字是奇数还是偶数
# num = int (input("请输入您要判断的数字:"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

#根据用户输入的年龄,判断用户是否成年
# year = int(input("请输入您的年龄:"))
# if year >= 18:
#     print("您已经成年了")
# else:
#     print("您还没有成年")

#根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# num = float(input("请输入您要判断的数字:"))
# if num > 0 :
#     print(f"{num}是正数")
# else:
#     print(f"{num}是负数")



#根据用户输入的考试分数,判断该分数是否及格了
# num = float(input("请输入您的分数:"))
# if num >= 60:
#     print("及格")
# else:
#     print("不及格")


####################################if...elif ...else#####################################
#根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# num = float(input("请输入您要判断的数字:"))
# if num > 0:
#     print(f"{num}是正数")
# elif num < 0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}既不是正数也不是负数")

#根据输入用户名密码进行登录
#用户名,密码为admin/666888 或 root/547527 或 zhangsan/123456 则输出登录成功

# account = input("请输入用户名:")
# password = float(input("请输入密码:"))
# if account == "admin" and password ==666888:
#     print("登录成功")
# elif account == "root" and password ==547527:
#     print("登陆成功")
# elif account == "zhangsan" and password ==123456:
#     print("登陆成功")
# else:
#     print("登录失败")
#否则就提示用户名或密码错误


# 例题根据输入的三个边的边长(正整数),判断是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
a = int(input("请输入第一个边长:"))
b = int(input("请输入第二个边长:"))
c = int(input("请输入第三个边长:"))
if a + b > c  and b + c >a and c + a > b :
    if a == b == c :
        print("是等边三角形")
    elif a == b or b == c or c == a :
        print("是等腰三角形")
    else :
        print("是普通三角形")
else :
    print("不能构成三角形")
