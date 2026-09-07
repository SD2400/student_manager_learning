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

#打印99乘法表,外层循环控制行,内层循环控制列
#错误示范
# a = 1
# b = 1
# for i in range(1,10):
#     for j in range(b):
#         print(f"{a} * {b} =",a * b,end=("      "))
#
#     b  += 1
#     print()

#正确示范
# for i in range(1,10):  #外层控制行,从一开始共输出九行
#     for j in range(1,i+1):  #内层控制列,从一开始每一行加一列
#         print(f"{j} x {i} = {j*i}",end = "\t")  #\t是一个制表符
#     print() #print()自带换行效果


# 根据输入的直角边边长,打印等腰直角三角形
# i = int(input("请输入直角边边长:"))
# for i in range(1,i+1):
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()
#根据输入的数字,打印对应的数字金字塔
# num = int(input("请输入对应的数字:"))
# for num in range(1,num+1):
#     for j in range(1,num+1):
#         print(f"{j}",end="\t")
#     print()

#打印国际象棋棋盘(8行8列,第一行第一列是■,□
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print("■",end="\t")
        else:
            print("□",end="\t")
    print()
