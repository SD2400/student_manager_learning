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
# s5 = {1,3,5,7,9,2}
# s6 = {2,4,6,8,10,1}
# print(s5.difference(s6))
# print(s6.difference(s5))
#
#
# # s1.union(s2),输出两个集合的并集
# print(s5.union(s6))
#
#
# # s1.intersection(s2),交集
# print(s5.intersection(s6))

# 案例
# 根据提供的班级学生的选课情况,完成如下需求:
# 1.找出同时选修了法语和艺术的学生
# 2.找出同时选修了所有四门课程的学生
# 3.找出选修了足球,但没有选秀篮球的学生
# 4.统计每一个学生选秀的课程数量

# 选修足球的学生名单
football_set = {"王林","曾牛","徐立国","天运子","韩立","历飞雨","乌丑","紫灵","遁天"}
# 选修篮球的学生名单
basketball_set = {"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","历飞雨","云露"}
# 选修法语的学生名单
french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","历飞雨","韩立","曾牛"}
# 选修艺术生的学生名单
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}


# 1.同时选修法语和艺术的学生
# 方法一:   intersection --->求交集
print("同时选修法语和艺术的学生:",french_set.intersection(art_set))
# 方法二:   &  --->交集
print("同时选修法语和艺术的学生:",french_set & art_set )


# 2.同时选修所有四门课程的学生
# 方法一:
football_basketball = football_set.intersection(basketball_set)
french_art = french_set.intersection(art_set)
print("同时选修所有四门课程的学生:",football_basketball.intersection(french_art))
# 或者:
print("同时选修所有四门课程的学生:",football_set.intersection(basketball_set).intersection(french_set).intersection(art_set))
# 方法二:(最简洁)
print("同时选修所有四门课程的学生:",football_set & basketball_set & art_set & french_set)

# 3.选修了足球但没有选修篮球的学生
# 方法一:difference -->差集
print("选修了足球但没有选修篮球的学生:",football_set.difference(basketball_set))
# 方法二:  -    -->差集
print("选修了足球但没有选修篮球的学生:",football_set - basketball_set)
# 方法三:  集合推导式:变量名称 = {i表达式 for  i  in 集合 }       ,    变量名称 = {i表达式 for i in 集合 if 条件}
football_notbasketball = {i for i in football_set if i not in basketball_set}
print(football_notbasketball)
# 4.统计每一个学生选修的课程数量
all_set = football_set | basketball_set | art_set | french_set
print(all_set)  #首先求出所有学生的名单
all_list = [*football_set,*basketball_set,*art_set,*french_set]   #list列表中元素可重复,*起解包的作用
print(all_list)
for i in all_set:
    print(f"{i}选修的课程数量为:{all_list.count(i)}")  #列表名.count() -->统计列表中元素的数量