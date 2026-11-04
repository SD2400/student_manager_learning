"""
沙盒练习01 --- 三区模型
git status                    :查看当前仓库的状态.
git diff                         :查看工作区的状态.
git diff --staged         :查看暂存区的状态.
git add <文件>           :将文件提交到暂存区.
git add .                       :提交工作区所有文件
git commit -m "说明":将暂存区文件提交到仓库并做记录.
git log                         :查看历史记录

"""

"""
沙盒练习05 --- 解决合并冲突
git branch -v                              :列出本地所有分支,-v 表示同时显示每个分支最后一次提交的哈希值(版本号)和提交说明
git log --graph --oneline --all:git log 查看提交历史. 
                                                    -- graph 以图形化的方式(字符画)显示分支的合并轨迹. 
                                                    --oneline 让每次提交只在一行内显示
                                                    --all 显示所有分支的历史,而不仅仅是当前分支
git switch 分支1                          :切换到分支1
git merge 分支2                         :把分支2的代码合并到当前的分支里
git status                                   :再次查看状态
notepad 冲突文件.py               :使用记事本打开文件并进行操作(将冲突标记删除并保留最终想要的那行代码,然后保存并关闭记事本)
git add 冲突文件.py                       :将冲突文件放入暂存区
git commit -m "说明"             :提交这次合并结果
"""

"""
沙盒练习06 --- 临时切换任务
git ls-tree -r --name-only main
git stash                                    :收起当前改动
git stash push -m "说明"         :带备注,方便以后认
git stash list                              :看看抽屉里有什么
git stash pop                            : 取出来并删掉记录
git stash apply                         :取出来,但保留记录  
"""

"""
沙盒练习02 --- 整理提交历史
git log --graph --oneline --all
git rebase -i HEAD~3:
                     git rebase:变基.通常用来整理,合并,修改提交记录
                     -i        :是--interactive的缩写,意思是交互式.加上此参数,Git不会直接执行,而是会打开
                                一个文本编辑器,让我们手动选择要对提交记录做什么操作
                     注: 在文本编辑器中pick(p)的意思是保留这个提交(什么都不改)
                                    s(squash)压缩/合并.意思是把当前提交,合并到上一个提交里去
                    HEAD~3     :表示当前所在位置(HEAD)往前的3个提交
"""


"""
版本回退
作用:版本切换
命令形式:git reset --hard commitID     #commitID可以使用git-log 或git log指令查看
查看已经删除的记录:git reflog 

添加文件至忽略列表
可以在工作目录中创建一个名为.gitignore 的文件(文件名称固定),列出要忽略的文件模式

分支
查看分支: git branch
创建分支:git branch 分支名
切换分支:git switch 分支名
合并分支:①:git merge 分支名
        ②:git rebase 分支名
删除分支:git branch -d 分支名(删除分支时,需要做各种检查)
               git branch -D 分支名(不做任何检查,强制删除)

HEAD:是当前所在提交记录的符号名称. 分离HEAD就是让其指向一个具体的提交,而不是某个分支             

相对引用:
       ①使用^向上移动1个提交.(将此操作符加在引用名称的后面,表示让Git寻找指定提交记录的parent节点)
       ②使用~<num>向上移动多个提交记录,如~3

添加远程仓库
此操作是先初始化本地库,然后与已创建的远程库进行对接
git remote add <远端名称><仓库路径>  #远端名称:默认是origin,取决于远端服务器设置
                                                                    #仓库路径,从远端服务器获取此URL
查看远端仓库:git remote
推送到远程仓库
git push [-f][--set-upstream] [远端名称 [本地分支名] [:远端分支名]]
git push --set-upstream origin main
         如果远程分支名和本地分支名称相同,则可以只写本地分支
         git push origin main 


抓取和拉取
抓取 :git fetch [remote name] [branch name]
        抓取指令就是将仓库里的更新都抓取到本地,不会进行合并
        如果不指定远端名称和分支名,则抓取所有分支
拉取 :git pull [remote name] [branch name]
         拉取指令就是将远端仓库的修改拉到本地并自动进行合并,等同于fetch+merge
         如果不指定远端名称和分支名,则抓取所有并更新当前分支

解决合并冲突
A用户在本地修改代码后优先推送到远程仓库,此时B用户在本地修订代码,提交到本地仓库后,也需要推送到远程仓库,此时B用户晚于A用户,故需要先拉取远程仓库的提交,经过合并后才能推送到远端分支
"""

"""
撤销变更
撤销变更由底层部分(暂存单个文件或代码块)和上层部分(变更实际如何被撤销)组成.
git reset ...:通过将分支引用向后移动至一个更早的提交来撤销变更.
git revert ...:撤销变更并分享给别人
"""

"""
移动工作
git cherry-pick <提交1> <提交2> <提交3>:用来表达我们想将一些提交复制到当前所在的位置(HEAD)下面

"""