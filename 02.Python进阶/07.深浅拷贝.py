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
# 例题:
import copy
a = [[1,2],[3,4]]
b = copy.copy(a)  #浅拷贝  ,
c = copy.deepcopy(a) #深拷贝
b[0].append(5)
c[1].append(6)
print(a) #[[1,2,5],[3,4]]
print(b) #[[1,2,5],[3,4]]
print(c) #[[1,2],[3,4,6]]