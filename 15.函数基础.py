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
# def grades(list):
#     """
#     根据传入的班级学生高考成绩列表,计算集中的最高分,最低分,平均分
#     :param list: 高考成绩列表
#     :return: 最高分,最低分,平均分
#     """
#     max_grade = max(list)
#     min_grade = min(list)
#     avg_grade = round(sum(list)/len(list),2)
#     return max_grade,min_grade,avg_grade
# grades_list = [654,678,624,531,499]
# print(grades(grades_list))

################################################ 函数的变量作用域:指的是函数的作用范围
# 全局变量(在整个文件中都能使用) 和 局部变量(只能在函数内部使用)
# num = 1    #全局
# def uuu():
#     num =1000  #局部
#     print("num=",num)  #局部
#     print("______________")
# uuu()  #局部
# print("num=",num)   #全局

#global关键字:用于明确告诉Python解释器,在函数中使用全局变量,使得可以在函数内部修改全局变量的值
# num = 1
# def uuu():
#     global num
#     num = 1000
#     print("num",num)
# uuu()
# print("num=",num)

##################################################### 函数-传参方式
# # 定义函数
# def reg_stu(name,age,gender,city):
#     print(F"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return{"name":name,"age":age,"gender":gender,"city":city}

# 传参方式一:位置参数(调用时参数顺序与定义时的参数顺序完全一致)
# reg = reg_stu("张三",20,"男","北京")
# print(reg)
#
#
# # 传参方式二:关键字参数(调用时的参数顺序与定义时的参数顺序不一定完全一致)
# reg = reg_stu(name="张三",city="北京",age=20,gender="男")
# print(reg)
#
#
# # 传参方式三:位置参数  +  关键字传参(位置参数一定保证在关键字参数之前)
# reg = reg_stu("张三",20,city="南京",gender="女")
# print(reg)

#############################默认参数##############################
# 定义函数
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return{"name":name,"age":age,"gender":gender,"city":city}
#
# # 使用默认参数
# stu = reg_stu(name="张三",age=20)
# print(stu)
#
# stu1 = reg_stu(name="张三",age=20,city="上海")
# print(stu1)
#
# stu2 = reg_stu(name="张三",gender="男",age="20",city="广州")
# print(stu2)

#############################函数-不定长参数##############################
# 位置传递:*args  -->元组
# 传递的所有匹配的位置参数都会被args变量收集,这些参数会合并封装为一个元组,args是元组类型
# args只是约定俗成的变量名,并不是关键字,这里可以使用任何合法的变量名
# 需求:根据传入的数据,计算这批数据的最大值,最小值和平均值
# def Data(*args):
#     max_data = max(args)
#     min_data = min(args)
#     avg_data = sum(args)/len(args)
#     return max_data,min_data,avg_data
# data = Data(2,54,765,4345,6543,234)
# print(data)


# 关键字传递:**kwargs -->字典
# def Data(*args,**kwargs):
#     max_data =max(args)
#     min_data =min(args)
#     avg_data =sum(args)/len(args)
#
#
#     if kwargs.get("round") is not None:
#         avg_data=round(avg_data,kwargs.get("round"))
#
#     if kwargs.get("print"):
#         print(f"最大值为:{max_data},最小值为:{min_data},平均值为:{avg_data}")
#     return max_data, min_data, avg_data
#
# abc = Data(3,4,6,7,8,round = 2,print = True)
# print(abc)

# 函数的参数类型
# 普通参数:数字,布尔,字符串,列表,字典,元组,集合等
# 特殊参数:函数
# def add(x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def calc(x,y,oper):
#     return x, y ,oper(x,y)
#
# a = calc(10,20,add)
# print(a)
#
# b = calc(10,20,subtract)
# print(b)


# 匿名函数:指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数(单行表达式)
# 打印一个分割线
# out_line = lambda :print("--------")
# out_line()
#
# out_lina = lambda :"--------"
# print(out_lina())
#
# # 计算两数之和
# add = lambda x,y:x+y
# print(add(1,2))


# 需求:完成下列表的排序操作,按照每一个元素的字符个数,从小到大排序:
# 错误示范:
# data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
# data_list.sort()   #列表本身的排序是按照首字母的顺须进行排序的
# print(data_list)

data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
data_list.sort(key = lambda item:len(item))
print(data_list)
data_list.sort(key = lambda item:len(item),reverse = True)
print(data_list)