# def 函数名(参数列表):
    # 函数体
    # 返回值
# 函数名(参数)函数定义时的参数列表和返回值是可有可无的(又需求确定)
#


# 函数定义
# def out_line():
#     print("---------------------")      #函数在定义时不会运行,只有在调用后才运行
# # 函数调用
# out_line()                        #函数必须先定义,后调用
#
# def name():
#     input("请输入您的姓名:")
# name()
#
# out_line()
# name()
# out_line()
#
#
#
# ##############################函数的参数及返回值
# 1.计算圆的面积
# def circle_area(r):
#     """
#     计根据圆的半径,算圆的面积
#     :param r: 圆的半径
#     :return: 返回圆的面积
#     """
#     area = 3.14 * r * r
#     return area
# c_area = circle_area(10)
# print(c_area)
#
# # 2.计算长方形的面积
# def rectangle_area(a,b):
#     """
#     根据长方形的长度和宽度,计算长方形的面积
#     :param a: 长方形的长
#     :param b: 长方形的宽
#     :return: 长方形的面积
#     """
#     area = a*b
#     return area
# re_area = rectangle_area(10,20)
# print(re_area)
#
# # 3.计算圆的面积以及周长
# def circle(r): #如果返回有多个,多个返回值之间用逗号分隔    ---->多个返回值会封装到元组之中
#     """
#     根据圆的半径,计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积,周长
#     """
#     return 3.14*r**2,round(2*3.14*r,1)   #round(a,b)  a是要四舍五入的对象,b是要保留的小数点
# print(circle(10))
# print(type(circle(10)))
#
# area,length = circle(10)   #解包
# print(area)
# print(length)

# 函数的嵌套调用,函数的调用遵循栈结构,最后被调用的函数最先返回
# def function_a():
#     print("a...before")
#     function_b()
#     print("a...after")
#
# def function_b():
#     print("b...before")
#     function_c()
#     print("b...after")
#
# def function_c():
#     print("c...")
#
# function_a()
#
# """
# 运行代码后首先会执行function_a()--->print("a...before")--->function_b()--->print("b...before")--->function_c
# ---> print("c...") ---> print("b...after") --->print("a...after")
# """
#
# print("OVER")

# 案例1:
# 定义一个函数,根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)
# def s_area(d,h):
#     """
#     根据底和高计算三角形的面积
#     :param d:三角形的底
#     :param h: 三角形的高
#     :return: 三角形的面积
#     """
#     area = d * h / 2
#     return area
# print(s_area(2,3))

# 案例2:计算传入的字符串计算元音字母的个数(aeiouAEIOU)
# def vowel(s):
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num += 1
#     return num
# print(vowel("avnjskjaokdsmAFJKWO"))
#

# 案例3:定义一个函数:计算传入的班级学生高考成绩列表中成绩的最高分,最低分,平均值(保留1位小数)并返回
def grades(s):
    max_grade = max(s)
    min_grade = min(s)
    avg_grade = round(sum(s)/len(s,),1)
    return max_grade,min_grade,avg_grade
list_grade = [546,578,675,356,765,234,765,335]
print(grades(list_grade))