# 导入模块
# 1.
# import utils.my_fun  #import 包名.模块名
# utils.my_fun.log_separator1()  #调用模块时:包名.模块名.功能名
# utils.my_fun.log_separator2()
#
# import utils.my_var
# print(utils.my_var.NAME)

# 2.
# from utils import my_fun,my_var  #from ... 包名 import ... 模块名
# print(my_var.NAME,my_var.PI)   #调用功能时:模块名.功能名
# my_fun.log_separator1()

# 3.
# from utils import *   #使用该语句调用时,应确保__init__中有__all__=["模块名1","模块名2",...]
# print(my_var.NAME)
# my_fun.log_separator1()



# 导入模块中的功能
from utils.my_fun import log_separator1
log_separator1()

from utils.my_var import *
print(NAME)
print(PI)