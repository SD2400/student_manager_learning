#set集合
# 特点:无序的,不要可重复的,可修改的
# 定义:集合名 = {元素1.元素2...}      空集合: 集合名 = set{}
# s1 = {1,3,4,5,7,9,0,1,5}
# print(s1)
# print(type(s1))
#
# s2 = set()   #定义空集合
# print(type(s2))
# s3 = {}   #此代码定义的是字典
# print(type(s3))

# 集合的常用操作
# add(..)   添加一个元素到set集合中
# s4 = {1,2,3,4,5,6,7,8,0}
# s4.add(10)
# print(s4)
#
# # remove(..),删除set 集合中的一个指定元素
# s4.remove(10)
# print(s4)
#
# # pop(),随机删除一个元素并返回
# e= s4.pop()
# print(e)
# print(s4)
# #
# #clear(),清空元素
# s4.clear()
# print(s4)


# s1.difference(s2),两集合之差(输出第一个集合里包含而第二个集合不包含的元素)
s5 = {1,3,5,7,9,2}
s6 = {2,4,6,8,10,1}
print(s5.difference(s6))
print(s6.difference(s5))


# s1.union(s2),输出两个集合的并集
print(s5.union(s6))


# s1.intersection(s2),交集
print(s5.intersection(s6))


