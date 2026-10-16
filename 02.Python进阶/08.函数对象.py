"""
函数本身也是一个对象
这意味着函数不仅可以被调用,还可以像其他对象一样被赋值给其他函数,传递给其他函数
"""

####################一 将函数赋值给另一个变量
# def hello(): #定义一个函数
#     print("你好")
# a = hello
# a()
# print(a)
# print(hello)
# print(a is hello)

#注意,下面两种写法不一样
# a = hello #将函数对象赋值给a
# b = hello() #调用函数,并把函数的返回值赋值给a
# print(a)
# print(b)
 ####################二 将函数作为参数传递
# def add(a,b):
#     return a+b
# def calculate(func,a,b):
#     result = func(a,b)
#     print(result)
# calculate(add,1,2)

####################三 将函数作为返回值
# def outer():
#     def inner():
#         print("这里是内部函数")
#     return inner
# result = outer()
# result()

#######################四 函数对象的区别
# def get_number():  #定义一个函数
#     return 100     #返回100
# a = get_number     #将get_number这个函数对象赋值给a
# b = get_number()   #调用函数,并将返回值100赋值给b
# print(a)           #输出函数对象的相关信息
# print(b)           #输出100

#########################五 函数对象的属性
#__name__:获取函数的名称
#__doc__: 获取函数的文档字符串
# def add(a,b):
#     """
#     计算两个数字的和
#     :param a:
#     :param b:
#     :return:
#     """
#     return a+b
#
# print(add.__name__)
# print(add.__doc__)

#########################六 匿名函数lambda
# #一般情况下
# def add(a,b):
#     return a+b
# #使用lambda            结构:lambda 参数:表达式
# add1 = lambda a,b:a+b
# print(add(10,20))
# print(add1(10,20))
# #lambda适合简单的表达式,def适合更复杂的逻辑

##########################七 高阶函数
#可以被称为高阶函数的条件:
#1.接收其他函数作为参数   2.返回一个函数对象作为结果
def square(x):
    return x * x
def process(func,number):  #高阶函数
    return func(number)
print(process(square,3))