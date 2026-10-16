"""
浅拷贝:创建一个新的外层对象,但是不会递归复制里面的子对象
深拷贝:深拷贝不仅创建新的外层对象,还会递归复制其中包含的对象
在不可变数据类型(数字,字符串,元组等)中,深浅拷贝的效果都是一样的,
但在可变数据类型(列表,字典,集合)中深浅拷贝效果不同
"""
# import copy
# a1 = [10,1,2]
# b1 = a1
# c1 = copy.copy(a1)
# d1 = copy.deepcopy(a1)
# print("内存地址:",id(a1),id(b1),id(c1),id(d1))
# print(a1,b1,c1,d1)
# print()
# a2 = 10
# b2 = a2
# c2 = copy.copy(a2)
# d2 = copy.deepcopy(a2)
# print("内存地址:",id(a2),id(b2),id(c2),id(d2))
# print(a2,b2,c2,d2)
# print()
# a3 = [10,[1,2],2]
# b3 = a3
# c3 = copy.copy(a3)
# d3 = copy.deepcopy(a3)
# print("内存地址:",id(a3),id(b3),id(c3),id(d3))
# print(a3,b3,c3,d3)
#########总结:浅拷贝复制外层对象,内部对象可能仍然共享.
#########深拷贝递归复制内部对象,通常可以避免嵌套对象之间的修改相互影响

##############################浅拷贝有哪些常见写法########################
# # ①:使用copy.copy
# import copy
# a = [1,2,3]
# b = copy.copy(a)
#
# # ②使用列表切片
# a = [1,2,3]
# b = a[:]
#
# # ③使用列表的copy()方法
# a = [1,2,3]
# b = a.copy()
#############################深浅拷贝在字典中的应用############################
# student = {"name":"小明","scores":{"语文":90,"数学":95}}
#使用浅拷贝
# import copy
# student = {"name":"小明","scores":{"语文":90,"数学":95}}
# new_student = copy.copy(student)
# new_student["name"]="小红"
# new_student["scores"]["数学"]=100
# print(student) #{"name":"小明","scores":{"语文":90,"数学":100}}
# print(new_student) #{"name":"小红","scores":{"语文":90,"数学":100}}

#使用深拷贝
# import copy
# student = {"name":"小明","scores":{"语文":90,"数学":95}}
# new_student = copy.deepcopy(student)
# new_student["name"]="小红"
# new_student["scores"]["数学"]=100
# print(student) #{"name":"小明","scores":{"语文":90,"数学":95}}
# print(new_student) #{"name":"小红","scores":{"语文":90,"数学":100}}

##########################深浅拷贝在类和对象中的运用###############################
# import copy
# #定义一个商品类
# class Shopping:
#     def __init__(self,name,price,tags):
#         self.name = name
#         self.price = price
#         self.tags = tags
# #创建一个商品类对象
# s1 = Shopping("苹果",5,["水果","新鲜"])
# #复制这个对象
# s2 = copy.copy(s1)
# print(s1.tags)
# print(s2.tags)
# s2.tags[1] = "不新鲜"
# print(s1.tags)
# print(s2.tags)
# print(s1.tags is s2.tags)

####################使用is判断两个变量是否指向同一个对象##############
# x = [1,2]
# a = [x,x]
# print(a[0] is a[1])
# import copy
# b= copy.deepcopy(a)
# print(b[0] is b[1])

##################拷贝不可变量###############
# 深拷贝不代表:所有东西都会生成一个全新对象,例如一些不可变对象
# int,str,tuple中的不可变内容,可能直接复用
import copy
a = (1,2,3)
b = copy.deepcopy(a)
print(a is b)
#但当不可变量里嵌套可变量时
a1 = (1,2,[3,4])
b1 = copy.deepcopy(a1)
print(a1 is b1)
print(a1[2] is b1[2])  #当不可变对象中嵌套可变对象时,深拷贝创建新对象,内部可变对象独立
