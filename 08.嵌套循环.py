#打印一个长度为m,宽为n的长方形
# 错误示范
# m = int(input("请输入您要打印的长:"))
# n = int(input("请输入您要打印的宽:"))
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print("*") #print()语句自带换行效果

# 正确示范
# m = int(input("请输入您要打印的长:"))
# n = int(input("请输入您要打印的宽:"))
# for i in range(n):  #控制行
#     for j in range(m): #控制列
#         print("*",end=(" "))
#     print()  #起换行效果

#打印99乘法表
#错误示范
a = 1
b = 1
for i in range(1,10):
    for j in range(b):
        print(f"{a} * {b} =",a * b,end=("      "))
    b  += 1
    print()
    