#列表的定义
# 列表名 = [元素1,元素2,元素3,元素4...]
# 特点:①列表内的元素可以是不同类型②列表内的元素是有序的,可重复的③列表内的元素可以进行修改
# s = [1,45,2.5,"Python",True]
# print(type(s))
#
# # 索引
# print(s[0])
# print(s[-5])
# print(s[3])
# print(s[-2])
#
# # 查询,当索引超出范围,将会报错
# print(s[2])
#
# # print(s[7])
#
# # 修改
# s[0] = 18
# print(s)
#
# # 删除
# del s[1]
# print(s)
#
# # 遍历
# for i in s:
#     print(i)


# 切片:对操作的书局截取其中的一部分
# 语法:序列数据[开始索引:结束索引:步长],不包含结束索引位置对应的元素(开始索引未指定默认为0,结束
# 索引未指定默认直到列表末尾,步长未指定默认为1)
# s = ["A","C","D","G","R","G"]

#截取A到G(包含G)之间的元素
# print(s[0:4:1])
# print(s[:4:])
# print(s[:4])
#
# print(s[0:5:2])
# print(s[:5:2])
#
# print(s[0:-1:1])
# print(type(s[0:-1:1]))



# 列表常用方法
# 创建一个列表
# s = [24,45,3,65,34,654,234,1234]
# print(s)
#
# # append() -->在列表尾部追加元素
# s.append(33)
# print(s)
#
# # insert() -->在指定索引之前,插入该元素
# s.insert(4,24)
# print(s)
#
# # remove() -->移除列表中(元素相同时)第一个匹配到的值
# s.remove(24)
# print(s)
#
# # pop() -->删除列表中指定索引位置的元素(如果未指定则删除最后的元素)
# s.pop(1)
# print(s)
# s.pop()
# print(s)
#
# # sort() -->对列表进行排序 (要求:元素类型必须一致)
# s.sort()
# print(s)
#
#
# # reserve -->反转列表元素
# s.reverse()
# print(s)


# 例题
# 将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值,最大值和平均值
# 定义一个列表
# s = []
#
# # 用户输入数字
# for i in range(10):
#     num = int(input("请输入一个数字:"))
#     s.append(num)
# print(s)
#
# # 将列表中的数字进行排序
# s.sort()
# print(s)
# # 输出其中的最小值,最大值和平均值 -----求最小值min(),求最大值max(),求和sum(),求元素个数len()
# print(min(s))
# print(max(s))
# print(sum(s)/len(s))


# 例题二
# 合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# # 合并两个列表中的元素,可以用for循环的遍历进行合并
# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
# new_list =[]
# # 对合并的结果进行去重
# for num in num_list1:
#     if num not in new_list:  #去重,判断元素是否已经存在于新列表new_list中
#         new_list.append(num)
# print(new_list)

# 优化(合并两组列表)
# ①num_list = [*num_list1,*num_list2]  #解包:将列表这一类容器解开成一个一个独立的元素
# ②num_list = num_list1 + num_list2

# 例题三:生成一个1-20的平方列表
# list = []
# for i in range(1,21):
#     list.append(i**2)
# print(list)

# 优化 -->列表推导式1:[要插入的值 for i in 序列/列表 ]
list = [i**2 for i in range(1,21)]
print(list)

# # 例题四:从如下数字列表中提取所有偶数,,并计算其平方,,组成一个新的列表
# new_list = []
# for i in list:
#     if i % 2 == 0:
#         new_list.append(i**2)
# print(new_list)

# 优化:列表推导式2-->[要插入的值 for i in 序列/列表 if 条件]
new_list = [i**2 for i in list if i%2==0]
print(new_list)
