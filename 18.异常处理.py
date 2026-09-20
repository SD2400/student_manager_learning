#异常(又称Bug):程序运行过程中出现的错误,它会中断程序正常执行流程
# 作用:①保证数据,逻辑的正确性   ②在开发阶段,帮助发现更多问题
# 处理方案:①不做处理,整个程序因为一个Bug终端执行  ②捕获异常:按照我们自己的处理方式,处理完异常程序继续执行


# 捕获异常:
# try:
#     print("================")
#     print(my_name)
#     print("================")
# except NameError as e:   #捕获NameError类型的异常
#     print("程序运行时出现异常,异常类型:",e)

# try:
#     print("=============")
#     print(1 / 0)
#     print("============")
# except ZeroDivisionError as e:  #捕获ZeroDivisionError类型的异常
#     print("程序运行时出现异常,异常类型:",e)

# try :
#     print("===========")
#     print("ABC"[10])
#     print("==========")
# except IndexError as e:    #捕获IndexError类型的异常
#     print("程序运行时出现异常,异常类型:",e)

# try:
#     print("=======")
#     print(wsd)
#     print("=====")
# except Exception as e:    #可以捕获所有类型的异常值,等效于except:
#     print(e)
# finally: #无论有没有异常,finally语句最终都会被执行
#     print("资源释放~")


###############################异常的传递####################################
# 指异常在函数调用中层层上报的过程,直到有人处理它,或程序崩溃
def fun1():
    print("fun1.........running.........")
    fun2()
def fun2():
    print("fun2.........running.........")
    fun3()
def fun3():
    print("fun3.........running.........")
    print(Python)
if __name__=="__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行时出现异常,异常类型:",e)

