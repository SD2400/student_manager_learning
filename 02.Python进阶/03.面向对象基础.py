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

# class Car:
#     #类属性,通过 类名.属性 的方式查询
#     rate = 0.1
#     num_tire = 4
#     def __init__(self,c_color,c_price,c_name):
#         #实例属性,通过 实例对象.属性 的方式查询
#         self.color = c_color
#         self.price = c_price
#         self.name = c_name
#         self.rate = 0.2
#     def running(self):
#         print(f"一辆{self.color}的{self.name}正在高速上行驶...")
#     def total_price(self,discount,rate):
#         return discount * self.price + rate * self.price
# C1 = Car("红色",45000,"奔驰")
# #通过实例查找属性时,会先查询实例属性,实例属性不存在,再查询类属性
# print("C1的价格:",C1.price)
# print("C1的税率:",C1.rate)
# print("Car这个类的税率:",Car.rate)
# print("C1的轮胎数量:",C1.num_tire)
# print("Car的轮胎数量:",Car.num_tire)

######################### 魔法方法 ##############################
# 魔法方法:指的是Python中以双下划线开头和结尾的特殊方法,用于定义类的特殊行为
# 魔法方法不需要我们手动调用,它会在合适的时机自动调用

#一些常见的魔法方法
"""
__init__ : 初始化方法
__str__  : 字符串表示的方法
__eq__   : 比较两个对象是否相等(equal)
__lt__   : 支持比较两个对象的大小,小于(less than)
__le__   : 同上,小于等于(less than equal)
__gt__   : 同上,大于(greater than)
__ge__   : 同上,大于等于(greater than equal)
"""
# class Car:
#     def __init__(self,color,name,price):
#         self.color = color
#         self.name = name
#         self.price = price
# C1 = Car("红色","byd",500000)
# C2 = Car("红色","byd",500000)
# print(C1) #默认输出出来的是对象的内存地址(16进制)
# print(C2)
# print(C1==C2) #默认基于对象的内存地址进行比较

#
# class Car:
#     def __init__(self,color,name,price):
#         self.color = color
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"颜色为:{self.color},品牌为:{self.name},价格为:{self.price}"
#     def __eq__(self,other):
#         return self.color == other.color and self.name ==  other.name and self.price == other.price
#     def __lt__(self,other):
#         return self.price < other.price
# C1 = Car("红色","byd",500000)
# C2 = Car("红色","byd",500000)
# print(C1)
# print(C2)
# print(C1==C2)
# print(C1<C2)

"""
案例1:
采用面向对象的编程思想,完成教务系统管理的开发,教务管理系统可以管理在校学生的成绩信息,
通过控制台菜单与用户交互,具体的功能如下:
1.添加学生成绩:根据输入的学生姓名,语文成绩,数学成绩,英语成绩,记录在系统中
  1.1 输入学生姓名,语文成绩,数学成绩,英语成绩
  1.2 检查学生姓名是否已存在,如果学生不存在,再添加(存在则不添加)
  1.3 验证成绩范围(0-100)
  1.4 创建学生对象并添加到系统
2.修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
  2.1 输入要修改的学生姓名
  2.2 根据姓名查找该学生,显示该学生当前成绩信息
  2.3 输入新的语文,数学,英语成绩
  2.4 更新学生成绩数据
3.删除学生成绩:根据输入的学生姓名,删除对应的学生成绩
4.查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出
  4.1 输出格式为:"姓名: 张三 | 语文:85 | 数学:90 | 英语:88 | 总分:263"
5.展示全部学生成绩:展示出系统中所有学生的成绩

"""

# #创建学生类
# class Student:
#     def __init__(self,name,chinese,math,english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#         self.total = self.chinese + self.math + self.english
#     #将学生类对象的输出结果变为字符串
#     def __str__(self):
#         return f"姓名: {self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} |总分:{self.total} "
#
#     #修改学生成绩
#     def update(self,chinese=None,math=None,english=None):
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english
# # 创建教务系统类
# class EduManagement:
#     #定义两个类属性
#     system_version = "1.0"
#     system_name = "教务管理系统"
#     def __init__(self):
#         self.student_list = []   #创建学生列表
#     #添加学生
#     def add_student(self):
#         name = input("请输入学生的姓名:")
#         for i in self.student_list:
#             if i.name == name:
#                 print("该学生已存在,请重新输入!")
#                 return
#         chinese = int(input("请输入该学生的语文成绩:"))
#         math = int(input("请输入该学生的数学成绩:"))
#         english = int(input("请输入该学生的英语成绩:"))
#         if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <=100:
#             stu = Student(name,chinese,math,english)
#             self.student_list.append(stu)
#             print("学生添加成功!")
#             return
#         else:
#             print("学生的成绩不满足要求:0 - 100")
#     #修改学生
#     def update_student(self):
#         name = input("请输入要修改的学生姓名:")
#         for i in self.student_list:
#             if i.name == name:
#                 print(f"当前成绩为:{i}")
#                 chinese = int(input("请输入修改后的语文成绩:"))
#                 math = int(input("请输入修改后的数学成绩:"))
#                 english = int(input("请输入修改后的英语成绩:"))
#                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                     i.update(name,chinese,math,english)
#                     print(f"修改后的成绩为:{i}")
#                     return
#                 else:
#                     print("学生的成绩不满足要求:0 - 100")
#                     return
#         print("未找到该学生,请重新输入!")
#     #删除学生
#     def delete_student(self):
#         name = input("请输入要删除的学生姓名:")
#         for i in self.student_list:
#             if i.name == name:
#                 self.student_list.remove(i)
#                 print("该学生已删除!")
#                 return
#         print("未找到该学生,请重新输入!")
#     #查询指定学生
#     def find_student(self):
#         name = input("请输入要查询的学生姓名:")
#         for i in self.student_list:
#             if i.name == name:
#                 print(i)
#                 return
#         print("未找到该学生,请重新输入!")
#
#     #展示全部学生
#     def show_student(self):
#         for i in self.student_list:
#             print(i)
#
#     def run(self):
#         print(f"欢迎使用教务管理系统{EduManagement.system_version}")
#         while True:
#             print("""
#             #######################################################################
#             #1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.展示全部学生  6.退出系统  #
#             #######################################################################
#                   """)
#             a = int(input("请选择要输入的数字(1-6):"))
#             match a:
#                 case 1:
#                     self.add_student()
#                 case 2:
#                     self.update_student()
#                 case 3:
#                     self.delete_student()
#                 case 4:
#                     self.find_student()
#                 case 5:
#                     self.show_student()
#                 case 6:
#                     print("bye~")
#                     break
#                 case _:
#                     print("输入错误!")
#
#
# if __name__ == "__main__":
#     em = EduManagement()
#     em.run()
"""
案例2:
采用面向对象的编程思想,开发一个购物车管理系统,实现商品信息的添加,修改,删除,查询功能.
系统使用自定义对象存储商品数据,通过控制台菜单与用户交互.具体功能如下:
1.添加购物车:用户根据提示录入商品名称,以及商品的价格,数量,保存该商品信息到购物车.
2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格,数量,
  输入完成后修改该商品的信息
3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品
4.查询购物车:将购物车中的商品信息展示出来,格式为:
  "商品名称: xxx, 商品价格: xxx, 商品数量: xxx".
5.退出购物车
"""
#定义商品类
class Commodity:
    def __init__(self,name,price,num):#初始化商品名称,价格,数量
        self.name = name
        self.price = price
        self.num = num
    def __str__(self): #将商品对象转化为字符串
        return f"商品名称: {self.name},商品价格: {self.price},商品数量: {self.num}"
    def update(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num
#定义管理系统类
class ManSystem:
    #创建一个空列表
    def __init__(self):
        self.com_list = []
    #添加购物车
    def add_com(self):
        name = input("请输入要添加的商品名称:")
        for i in self.com_list:
            if i.name == name:
                print("该商品已录入,请重新输入!")
                return
        price = float(input("请输入该商品的价格:"))
        num = int(input("请输入该商品的数量:"))
        if price >0 and num>0:
            com = Commodity(name,price,num)
            self.com_list.append(com)
            print("该商品已添加完成!")
            return
        else:
            print("该商品的价格/数量应大于0,请重新输入")
    #修改购物车
    def update_com(self):
        name = input("请输入要修改的商品名称:")
        for i in self.com_list:
            if i.name == name:
                print("该商品当前的信息为:",i)
                price = float(input(f"请输入修改后{i.name}的价格:"))
                num = int(input(f"请输入修改后{i.name}的数量:"))
                if price > 0 and num > 0:
                    i.update(price, num)
                    print("商品信息修改完成!")
                    print("修改后的商品信息为:", i)
                    return
                else:
                    print("该商品的价格/数量应大于0,请重新输入")
                    return
        print("未找到该商品,请重新输入!")
    #删除购物车
    def del_com(self):
        name = input("请输入要删除的商品名称:")
        for i in self.com_list:
            if i.name == name:
                self.com_list.remove(i)
                print("该商品信息已删除!")
                return
        print("未找到该商品")
    #查询购物车
    def show_com(self):
        for i in self.com_list:
            print(i)
    #退出购物车
    def exit_com(self):
        print("bye~")
    def run(self):
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加购物车 2.修改购物车 3.删除购物车 4.查询购物车 5.退出购物车 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            a = input("请输入您要使用的功能(1-5):")
            match a:
                case "1":
                    self.add_com()
                case "2":
                    self.update_com()
                case "3":
                    self.del_com()
                case "4":
                    self.show_com()
                case "5":
                    self.exit_com()
                    break
if __name__ == "__main__":
    m = ManSystem()
    m.run()