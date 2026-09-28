#面向对象编程:对象可以理解为现实中的人或物在程序中的数字化身(万物皆对象)
# 类:描述的是一组具有相同属性和方法的模板
# 定义类名时每个单词首字母需要大写,每个单词之间不用分隔
# 类的定义:
# class Car:  #定义类         ------>不推荐
#     pass
# C1 = Car()  #创建对象
# C1.color = "red"
# C1.price = 500000  #动态的为对象添加属性
# print(C1)
# print(C1.price)
# print(C1.__dict__)  #会将对象的所有属性以字典的形式输出出来

# 创建对象
class Car:
    #__init__方法是对象初始化的方法,会在对象创建时自动调用,可在该方法中为对象创建对应的属性
    #self是第一个参数,表示当前所创建出来的实例对象
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.price = c_price
        self.name = c_name
C1 = Car("奔驰","x5",500000)
print(C1.name)
print(C1.__dict__)
C2 = Car("宝马","x6",900000)
print(C2.__dict__)
