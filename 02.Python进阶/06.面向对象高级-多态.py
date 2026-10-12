# 多态:指同一个方法,具有不同的形态,行为,表现
# class Car:
#     def __init__(self,name,color,price):
#         self.name = name
#         self.color = color
#         self.price = price
#     def charge(self):
#         print("正在补充燃料")
#
# class ElectricCar(Car):
#     def charge(self):
#         print("正在充电")
#
# class FuleCar(Car):
#     def charge(self):
#         print("正在加油")
#
# #参数类型为父类,支持传入任意参数的子类
# def handle_charge(car:Car):      #car:Car  --> car 指参数,: 代表类型注解,Car表示只接受Car类的参数
#     car.charge()
#
# if __name__ == "__main__":
#     handle_charge(ElectricCar("宝马","红色","1000"))
#     handle_charge(FuleCar("奔驰","黑色","123"))


###################################多态(鸭子类型)#####################################################3
#鸭子类型(Duck Typing):是指如果它走路像鸭子,叫起来也像鸭子,那么它就是鸭子
#在鸭子类型中,关注的是对象的行为(它有什么方法),而不是对象的类型(它是什么类)
class Duck:
    def __init__(self,name,year):
        self.name = name
        self.year= year
    def swimming(self):
        print(f"Duck :{self.year}岁的{self.name}正在游泳")

class Dog:
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def swimming(self):
        print(f"Dog :{self.year}岁的{self.name}正在游泳")

class Pig:
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def swimming(self):
        print(f"Pig :{self.year}岁的{self.name}正在游泳")

def swimming(duck):
    duck.swimming()
if __name__ == "__main__":
    swimming(Duck("唐老鸭","1"))
    swimming(Dog("小白","3"))
    swimming(Pig("佩奇","2"))

#鸭子类型的优势是不需要依赖继承关系,只要对象有相应的方法就能使用
