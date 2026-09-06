#打印十遍"人生苦短,我用Python"
# i = 1
# while i <=10:
#     i = i+1
#     print("人生苦短,我用Python")
# else :
#     print("循环正常结束")

#计算1-100之间所有偶数累加之和
# i =0
# total =0
# while i <=100 and i % 2 ==0:
#     print(total )
#     i += 2
#     total += i

# 正确代码:
i = 1
total = 0
while i <=100:
    if i % 2 ==0:
        total += i
    i += 1
print("1-100之间所有的偶数之和为:",total)