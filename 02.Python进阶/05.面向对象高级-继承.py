#继承:描述的是两个类之间的关西,子类继承父类,可以获取父类的属性和方法(非私有)

# class Car:
#     def __init__(self,name,color,price,owner):
#         self.name = name
#         self.color = color
#         self.price = price
#         self.__owner = owner
#
#     def start(self):
#         print(f"一辆{self.color}的{self.name}开始行驶")
#
#     def running(self):
#         print(f"一辆{self.color}的{self.name}正在高速上行驶...")
#
#     def stop(self):
#         print(f"一辆{self.color}的{self.name}停了下来")
#
#     def __change(self):
#         print(f"车主{self.__owner}的{self.color}{self.name}变成了变形金刚")
#
# c1 = Car("奥迪","黑色","999999","张三")
# c1.start()
# c1.running()
# c1.stop()
# c1._Car__change()
# print(c1.price)
# print(c1.name)
# print(c1.color)
# print(c1._Car__owner)
#
# class ElectricCar(Car):
#     pass
# c2 = ElectricCar("奔驰","白色","100000000","李四")
# c2.start()
# c2.running()
# c2.stop()
# c2._Car__change()
# print(c2.price)
# print(c2._Car__owner)
###################################继承-重写##########################################
#重写:是指子类继承父类后,如果父类中的方法不满足需求,可以在子类中重新定义父类的方法(方法名相同),
#    从而满足其需求
"""
在子类中调用父类的方法:
1.
super.方法名()
2.
z父类名.方法名(self)
"""
#
# class Car:
#     def __init__(self,name,color,price,owner):
#         self.name = name
#         self.color = color
#         self.price = price
#         self.__owner = owner
#
#     def start(self):
#         print(f"一辆{self.color}的{self.name}开始行驶")
#
#     def running(self):
#         print(f"一辆{self.color}的{self.name}正在高速上行驶...")
#
#     def stop(self):
#         print(f"一辆{self.color}的{self.name}停了下来")
#
#     def charge(self):
#         print(f"{self.color}的{self.name}正在补充燃料...")
# c1 = Car("奥迪","红色","99999","张三")
# c1.charge()
#
# class ElectricCar(Car):
#     def charge(self):
#         print(f"{self.color}的{self.name}正在充电...")
# c2 = ElectricCar("特斯拉","白色","400000","李四")
# c2.charge()
#############################多继承###########################################################
#多继承:指的是一个子类同时继承多个父类的情况(会将多个父类的属性和方法同时继承下来)
"""
语法:
class 子类名(父类名1,父类名2,...):
    代码
    ...
"""

#注意:
#    当一个类继承了多个父类时,默认优先使用第一个父类名中的同名属性或方法,可以使用
#    类名.__mro__ 属性 或 类名.mro() 方法查看调用顺序
class Car:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    def run(self):
        print(f"一辆{self.color}的{self.name}正在高速上行驶...")

class Huawei:
    def __init__(self,version=1.0):
        self.version = version
    def run(self):
        print(f"华为nb")
class WenJie(Car,Huawei):
    def __init__(self,version,name,color,price):
        Car.__init__(self,name,color,price)
        Huawei.__init__(self,version)
    def run(self):
        Car.run(self)
        Huawei.run(self)
c1 = WenJie(1.2,"天下","白色","21345")
print(WenJie.__mro__)
print(c1.__dict__)
