"""
日常基本循环:
编辑 -> status -> diff -> add -> diff -- staged -> commit
先确认发生了什么,再选择内容,最后保存成历史
一句话:写代码之前确认分支,提交之前确认状态和差异
"""

"""
git init 与 git clone

git init 
把现有目录初始化为Git仓库:
# 切换终端当前目录;后续 Git 命令作用于该目录所在仓库
cd my-project
# 在当前目录初始化仓库; -b main 同时指定初始化分支名
git init

Git 会创建隐藏的 .git 目录,里面保存对象,引用和配置.
指定初始化分支:
#在当前目录初始化仓库; -b main 同时指定初始化分支名.
git init -b main
不要手动修改或删除 .git .删除它不会删除项目文件,但会失去其中的Git历史和本地分支信息.

"""