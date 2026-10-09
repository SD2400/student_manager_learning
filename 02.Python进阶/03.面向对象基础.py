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
# class Car:
#     #__init__方法是对象初始化的方法,会在对象创建时自动调用,可在该方法中为对象创建对应的属性
#     #self是第一个参数,表示当前所创建出来的实例对象
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand = c_brand
#         self.price = c_price
#         self.name = c_name
# C1 = Car("奔驰","x5",500000)
# print(C1.name)
# print(C1.__dict__)
# C2 = Car("宝马","x6",900000)
# print(C2.__dict__)

# class People:
#     def __init__(self,p_name,p_age,p_gender,p_bir):
#         self.name = p_name
#         self.age =p_age
#         self.gender = p_gender
#         self.bir = p_bir
#         print("People 类属性初始化完毕")
# Num1 = People("赵",20,"男","3.13")
# print(Num1.__dict__)
# Num2 = People("温",20,"女","0718")
# print(Num2.__dict__)

###################################实例方法######################################
"""
class 类名:
    def __init__(self,形参列表):
        self.属性名 = 参数
        self.属性名 参数
    def 方法名(self,形参列表):
        ...
    def 方法名(self,形参列表):
        ...
"""
# class Car:
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#     def running(self):
#         print(f"{self.brand}的{self.name}正在高速上行驶")      #self 表示当前实例对象
#     def total_price(self,discount,rate=0.1):
#         """
#         计算购买汽车的最终价格
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 最终价格
#         """
#         return self.price * discount + self.price * rate
#
# C1 = Car("奔驰","e300",5000)
# print(C1.__dict__)
# C1.running()
# print(C1.total_price(0.9))
# print(C1.total_price(0.9,0.1))


##############################实例属性与类属性######################
#实例属性:实例属性属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据)
# 类属性:类属性是属于类本身的属性,所有实例共享的(所有对象共享的数据或配置)

class Car:
    #类属性,通过 类名.属性 的方式查询
    rate = 0.1
    num_tire = 4
    def __init__(self,c_color,c_price,c_name):
        #实例属性,通过 实例对象.属性 的方式查询
        self.color = c_color
        self.price = c_price
        self.name = c_name
        self.rate = 0.2
    def running(self):
        print(f"一辆{self.color}的{self.name}正在高速上行驶...")
    def total_price(self,discount,rate):
        return discount * self.price + rate * self.price
C1 = Car("红色",45000,"奔驰")
#通过实例查找属性时,会先查询实例属性,实例属性不存在,再查询类属性
print("C1的价格:",C1.price)
print("C1的税率:",C1.rate)
print("Car这个类的税率:",Car.rate)
print("C1的轮胎数量:",C1.num_tire)
print("Car的轮胎数量:",Car.num_tire)
