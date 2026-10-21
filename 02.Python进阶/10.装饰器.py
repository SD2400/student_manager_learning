"""
装饰器就是给已有函数增加额外功能的函数,它本质上就是一个闭包
特点:
  1.不修改已有函数的源代码
  2.不修改已有函数的调用方式
  3.给已有函数增加额外的功能
学习装饰器的目的:对已有函数进行额外的功能扩展
"""
#例
#定义装饰器
# def decorator(func):  #如果闭包函数的参数有且只有一个并且是函数类型,那么这个闭包函数称为装饰器
#     def inner_func():
#         #在内部函数里面对已有函数进行装饰
#         print("登录成功")
#         func()
#     return inner_func
# #装饰器语法糖写法
# @decorator  #等价于comment = decorator(comment)
# def comment():
#     print("发表评论")
#
# comment()

#装饰器的执行时机:当当前模块加载完成后,装饰器会立即执行,对已有函数进行装饰

#############################装饰器的使用####################
"""
装饰器的使用场景:1.函数执行时间的统计 2.输出日志信息"""
# import time
# def decorator(func):
#     def inner():
#         begin = time.time()  #获取的时间为距离1979-1-1 0:0:1
#         func()
#         end = time.time()
#         print(end - begin)
#     return inner
# @decorator
# def comment():
#     for i in range(1000000):
#         print(i)
# comment()

#############################通用装饰器的使用######################
"""
通用的装饰器:可以装饰任意类型的函数
#使用装饰器装饰已有函数时,内部函数的类型要和要装饰的已有函数的类型保持一致
"""
#---------------装饰带有参数无返回值的函数
# def decorator(func):
#     def inner(a,b):
#         print("正在努力计算....")
#         func(a,b)
#     return inner
# @decorator
# def add_num(num1,num2):
#     result = num1 +num2
#     print("结果为:",result)
# add_num(10,20)

#---------------装饰带有参数有返回值的函数
# def decorator(func):
#     def inner(a,b):
#         print("正在努力计算....")
#         num = func(a,b)
#         return num
#     return inner
# @decorator
# def add_num(num1,num2):
#     result = num1 +num2
#     return result
# result = add_num(10,20)
# print("结果为:",result)

#---------------装饰带有不定长参数,有返回值的函数
#该装饰器还可以成为通用的装饰器
# def decorator(func):
#     def inner(*args,**kwargs):
#         print("正在努力执行加法计算")
#         #*args:把元组里面的每一个元素,按照位置参数的方式进行传参
#         #**kwargs:把字典里面的每一个键值对,按照关键字的方式进行传参
#         #这里对元组和字典进行拆包,仅限于结合不定长参数的函数使用
#         num= func(*args,**kwargs)
#         return num
#     return inner
#
# @decorator
# def add_num(*args,**kwargs):
#     result = 0
#     #args:元组类型
#     #kwargs:字典类型
#     for value in args:
#         result += value
#     for value in kwargs.values():
#         result +=value
#     return result
# a=add_num(1,1)
# print(a)


###########################多个装饰器的使用
#多个装饰器的过程:由内到外的一个装饰过程,先执行内部的装饰器,再执行外部的装饰器
#原理剖析:content = make_div(make_p(content))
# def make_p(func):
#     print("make_p装饰器好了")
#     def inner():
#         result= "<p>"+func()+"<p/>"
#         return result
#     return inner
# def make_div(func):
#     print("make_div装饰器好了")
#     def inner():
#         result = "<div>"+func()+"<div/>"
#         return result
#     return inner
# @make_div
# @make_p
# def content():
#     return "人生苦短,我用Python!"
# result = content()
# print(result)

###########################带有参数的装饰器
"""
使用带有参数的装饰器,其实是在装饰器外面又包裹了一个函数,使用该函数的接收参数
,返回是装饰器,因为@符号需要配合装饰器实例使用"""
def return_decorator(flag):
    def decorator(func):
        def inner(*args):
            if flag == "+":
                print("正在努力执行加法计算")
            elif flag == "-":
                print("正在努力执行减法计算")
            func(*args)
        return inner
    return decorator
@return_decorator("+")
def add_func(a,b):
    result = a+b
    print(result)
@return_decorator("-")
def sub_func(a,b):
    result = a-b
    print(result)
add_func(1,2)
sub_func(1,2)