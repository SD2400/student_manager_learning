#常量(不会发生变化的数据;常量的名称一般用大写)
PI = 3.1415926
NAME ="张三"
__all__=["PI","log_separator1"]  #__all__:控制的是from 自定义模块 import * 语句导入的是哪些功能

# 函数
def log_separator1():
    print("-" * 30)

def log_separator2():
    print("+" * 30)

def log_separator3():
    print("*" * 30)

def log_separator4():
    print("#" * 30)


# 测试函数
# __name__:Python中的内置变量,当直接运行当前模块时,__name__的值为"__main__".当该模块被导入时,__name__的值就是模块名称.
if __name__ == "__main__":
    log_separator1()

