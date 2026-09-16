#三步操作:打开文件  -->读/写文件 -->关闭文件

# 读取文件
#打开文件
# f = open("C:/Users/15451/Desktop/望庐山瀑布.txt","r",encoding="utf-8")
# #
# # #读取文件
# # ①
# # content = f.read()
# # print(password)
# #
# ②content = f.readlines()
# for i in content:
#     print(i.strip())
#
#
# #
# # #关闭文件
# f.close()


# 写文件
# 打开文件
# f = open("C:/Users/15451/Desktop/静夜思.txt","w",encoding="utf-8")
#
# # 写文件
# f.write("静夜思 (李白)\n")
# f.write("床前明月光\n")
# f.write("疑是地上霜\n")
# f.write("举头望明月\n")
# f.write("低头思故乡\n")
#
# #关闭文件
# f.close()


##################################文件操作(资源释放)#########################
# 如果操作文件过程中出现了异常,文件无法关闭了,该怎么办?
# ①try:   finally:
# f = open("C:/Users/15451/Desktop/静夜思.txt","w",encoding="utf-8")
#
# try:
#     f.wirte("静夜思(李白)\n\n")
#     f.write("床前明月光\n")
#     i = 1/0
#     f.write("疑是地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")

# finally:
#     f.close()
#     print("文件关闭")


# ②with open() 最佳实践
with open("C:/Users/15451/Desktop/静夜思.txt","w",) as f:
    f.wirte("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
