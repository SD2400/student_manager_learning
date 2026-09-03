# # 字面量类型
# print(10)  #整数(int)
# print(3.14)  #浮点型(float)
# print("Hello Python")   #字符串(str)
# print(True)  #布尔(bool)
# print(False) #布尔(bool)
# print(None)  #空值(NoneType)
#
# #布尔类型本质也是整数类型(True -- 1,False -- 0)
# print(True+1)
# print(False-1)


#变量
# num = 1114.1
# print(num)
# num = num-0.1
# print(num)
# num = "OK"
# print(num)
# num = True
# print(num)

#练习
# a = 20.7 #基础播放量
# b = 50  #每个月新增播放量
# c = a+b #一个月后的视频播放量
# d = c+b #两个月后的视频播放量
# print("一个月之后的视频播放量:",c)
# print("两个月之后的视频播放量:",d)
#
# #一次性定义多个变量
# a,b = 20.7,50
# c = a+b #一个月后的视频播放量
# d = c+b #两个月后的视频播放量
# print("一个月之后的视频播放量:",c)
# print("两个月之后的视频播放量:",d)
#

#a = 10,b = 20,现需要将这两个变量值交换
# a = 10
# b = 20
# c = a
# a = b
# b = c
# print("a=",a)
# print("b=",b)

#a = 100,b = 200,c = 300,将a,b,c的值分别赋值给c,a,b,即a = 200,b = 300,c = 100
# a,b,c = 100,200,300
# d = a #a100,b200,c300,d100
# e = b #a100,b200,c300,d100,e200
# a = b #a200,b200,c300,d100,e200
# b = c #a200,b300,c300,d100,e200
# c = d
# print(a,b,c)
#
# d = a
# a = b
# b = c
# c = d
# print(a,b,c)

#常见数据类型
#type()
# print(type(10)) #int
# print(type(3.14)) #float
# print(type(False)) #bool
# print(type(True)) #bool
# print(type("OK")) #str
# print(type(None)) #NoneType
#
# a = 10
# print(type(a))
# b = 3.14
# print(type(b))

#isinstance(数据,类型),检查"数据"是否为"类型"类型
a = "10"
print(isinstance(a,int))
print(isinstance(a,str))
print(isinstance(10,float))
print(isinstance(10,int))
