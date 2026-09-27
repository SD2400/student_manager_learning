#pip=管理Python第三方库的工具,虚拟环境=给不同项目准备的"独立的Python小环境"
print("你好") #此代码可以直接运行,不需要安装其他东西,是因为print()是Python自带的

#Python本身还有很多模块,比如:
import json
import random
import os
# 这些属于Python自带的标准库,但有些功能Python默认没有,例如:
# requests ----网络请求
# numpy    ----数值计算
# pandas   ----数据处理
# flask    ----Web开发
#pygame    ----游戏开发
# 这些通常需要额外安装
# 这时候就需要 pip ,pip相当于Python的"软件下载/安装工具"
# 最常见的命令: pip install requests   意思是使用pip安装requests这个第三方包

# pip到底把东西安装到哪里?
# 假设电脑上只有一个Python,执行 pip install requests ,可能会把requests安装到当前Python环境的
# 第三方包目录中

# 虚拟环境:给每一个项目单独创建一个Python环境
# 例如:
# 电脑
#    -Python
#    -学生管理系统
#        -.venv
#            -Python
#            -第三方包
#    -数据分析项目
#        -.venv
#            -Python
#            -第三方包
# 两个项目相互隔离,其中.venv就是虚拟环境, .venv 只是一个常见的名字,也可以叫venv,或者my_environment
# 前面的 . 表示它通常是一个隐藏/不重要的项目辅助目录
# 建议:不要去虚拟环境中写代码