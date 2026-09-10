#元组
# 形式:元组名 = (元素1,元素2,元素3...)
# 元组中的元素是可重复的,有序的,不可修改的
# 定义空元组:①元组名 = ()   ②元组名 = tuple()
# s = (1,23,45,534,2,43,1,455)
# print(s)
# print(type(s))
#
# # 空元组
# a = ()
# b = tuple()
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# 元组的基本方法
# count()  --->统计元素的个数
# b = (1,2,3,4,5,6,7,8,9,1)
# print(b)
# print(b.count(1))
# print(b.count(0))
# print(b.count(9))
#
# # 切片
# print(b[0:3:1])
#
#
# # index()  --->获取元素的索引(元素重复时获取第一个元素的位置)
# print(b.index(1))
# print(b.index(9))
#
#
# # 注意事项:在定义只有一个元素的元组时,应在元素后加 ","  -->  c = (1,)
# c = (1,)
# print(c)
# print(type(c))
# print(isinstance(c,tuple))


####################################元组的组包与解包########################################
# 组包:将多个值合并到一个容器(元组,列表)中
# 解包:将容器中的元素分别赋值给多个变量
# 组包操作
# t1 = (1,2,3,4,5,6,7)
# t2 = 1,2,3,4,5,6,7
# print(t1)
# print(t2)
# print(type(t1))
# print(type(t2))
#
# # 解包操作
# # 基础解包(变量数量与容器的元素个数一致)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
#
# # *扩展解包 (收集剩余的所有元素,最终封装到列表list中)
# a,*b = t1
# print(a)
# print(*b)
# print(type(a))
# print(type(b))
#
#
# *a,b = t1
# print(*a)
# print(b)

# 案例:现有两个变量,分别为:a = 10,b = 20 ,现需要将这两个变量值交换,然后输出到控制台
# a = 10
# b = 20
# t1 = (a,b)                                 组包与解包操作可合并为
# print(t1)                                      :b,a=a,b
# b, a = t1
# print("交换后b的值为:",b)
# print("交换后a的值为:",a)

# 案例:现有三个变量,分别为:a = 100,b = 200,c = 300,现需要将这三个变量值进行交换,
# 将a,b,c的值分别赋值给c,a,b,并将其输出到控制台
# a = 100
# b = 200
# c = 300
# t1 = (a,b,c)  #进行组包
# print(t1)
# c,a,b = t1 #解包操作
# print("c=",c)
# print("a=",a)
# print("b=",b)

# 例题:
# 1.计算每个学生的总分,各科平均分,然后一并输出出来
# 2.统计各科成绩的最低分,最高分,平均分,并输出
# 3.查找成绩优秀(平均分大于90)的学生,并输出
student = (
("S001","王琳",85,92,78),
("S002","李慕婉",92,88,78),
("S003","十三",78,85,82),
("S004","曾牛",88,79,91),
("S005","周轶",95,96,89),
("S006","王卓",76,82,77),
("S007","红蝶",89,91,94),
("S008","徐立国",75,69,82),
("S009","许木",86,89,98),
("S010","遁天",66,59,72),
)

# 1.计算每个学生的总分,各科平均分,然后一并输出出来   -->{avg:.1f}保留一位小数
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
for i in student:
    total = i[2]+i[3]+i[4]
    avg = total/3
    print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {total} {avg:.1f}")

# 2.统计各科成绩的最低分,最高分,平均分,并输出
chinese_list = [i[2] for i in student]
math_list = [i[3] for i in student]
english_list = [i[4] for i in student]
print(f"{min(chinese_list)} {max(chinese_list)} {sum(chinese_list)/len(chinese_list)}")
print(f"{min(math_list)} {max(math_list)} {sum(math_list)/len(math_list)}")
print(f"{min(english_list)} {max(english_list)} {sum(english_list)/len(english_list)}")



# 3.查找成绩优秀的学生(平均分大于等于90),并输出
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
for h in student:
    total = h[2]+h[3]+h[4]
    avg = total/3
    if avg >= 90:
        print(h)