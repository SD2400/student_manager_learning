"""
定义:在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,
    ,我们把这个使用外部函数变量的内部函数称为闭包
条件:1.在函数嵌套的前提下
    2.内部函数使用了外部函数的变量(还包括外部函数的参数)
    3.外部函数返回了内部函数
作用:可以保存外部函数的变量
"""
# 示例:
# def func_out(): #定义一个外部函数
#     num1 = 10
#     def func_inner(num2):#定义一个内部函数
#         num = num1 + num2 #使用外部函数的变量
#         print(num)
#     return func_inner #返回内部函数,此函数即为闭包
# new_func = func_out()
# new_func(1)

#闭包的使用
"""
1.案例
需求:根据配置信息使用闭包实现不同人的对话信息,例如对话:
张三:到北京了吗? 李四:已经到了,放心吧
2.实现步骤说明
 定义外部函数接受不同的配置信息参数,参数是人名
 定义内部函数接收对话信息参数
 在内部函数里面把配置信息和对话信息进行拼接输出
"""
# def func1(name):
#
#     def func2(message):
#         print(f"{name} :{message}")
#     print(id(func2))
#     return func2
# #创建一个jem的闭包
# jem = func1("jem")
# #创建一个danny的闭包
# danny = func1("danny")
# jem("在干啥")
# danny("没干啥")
# jem("没干啥是干啥")
# danny("没干啥不是干啥而是没干啥")

#修改闭包内使用的外部变量函数,需使用关键字nonlocal
def func_out():
    num1 = 10
    def func_inner(num2):
        nonlocal num1
        num1 = 20
        print(num1 + num2)
    print("修改闭包前的外部变量:",num1)
    func_inner(10)
    print("修改闭包后的外部变量:",num1)
    return func_inner
new_func = func_out()
new_func(1)