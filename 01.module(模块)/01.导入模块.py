#一个.py就是一个模块,模块是Python程序的基本组织单位

# 导入模块    import ...
# 1.
# import random  #直接导入模块名
# for i in range(100):
#     print(random.randint(1,100))    #调用时:模块名.功能名

# 2.
# import random as rd  #为模块名起一个别名
# for i in range(10):
#     print(rd.randint(1,10))  #调用时:别名.功能名


# 导入模块中的功能  from ... impport ...
# 1.
# from random import randint   #从模块命中直接导入功能名
# for i in range(10):
#     print(randint(0,100)) #调用时:功能名

# 2.
# from random import randint as rint  #为导入的功能名起一个别名
# for i in range(10):
#     print(rint(1,100))  #调用时:别名

# 3.
from random import *
for i in range(10):
    print(randint(1,10))