"""
MySQL 窗口函数 · 学习笔记

整理日期：2026-11-07
前置：01.JOIN.py、02.子查询.py（窗口函数会和它们配合用）
数据：02.子查询-建表与数据.sql 里的 dept / job / emp
版本：MySQL 8.0 才支持窗口函数；5.7 及以前没有，遇到就升级或用变量模拟。

目录
     0. 学习路线（今天 3 小时版）
     1. 一句话理解：窗口函数解决什么问题
     2. 与 GROUP BY 的区别（最重要的一张对比）
     3. 语法骨架：OVER 里的三样东西
     4. 三类窗口函数总表
     5. 排序类三兄弟：ROW_NUMBER / RANK / DENSE_RANK
     6. 聚合类窗口：SUM / AVG / COUNT
     7. 偏移类：LAG / LEAD / FIRST_VALUE / LAST_VALUE / NTILE
     8. 窗口帧：ROWS / RANGE，以及 LAST_VALUE 的坑
     9. 执行顺序：为什么窗口函数不能写在 WHERE 里
    10. 六个经典题型（都能直接跑）
    11. 八个坑
    12. 性能提示
    13. 自测 6 题
    附录：emp 表字段速查


============================================================
0. 学习路线（今天 3 小时版）
============================================================
时间表（180 分钟，含一次休息）

    00:00-00:25  第 1 块   直觉 + 骨架
    00:25-00:55  第 2 块   排名三兄弟
    00:55-01:35  第 3 块   占比 + 累计
    01:35-01:50  休息（离开屏幕）
    01:50-02:25  第 4 块   窗口帧 + LAST_VALUE 坑
    02:25-02:55  第 5 块   三个必会题型
    02:55-03:00  收尾     自测 + 记笔记

第 1 块（25 分钟）直觉 + 骨架
    读：第 1、2、3 节（第 4 节的函数总表先跳过，用到再查）
    敲这两条，对比行数：

        SELECT dept_id, AVG(salary) FROM emp GROUP BY dept_id;          -- 4 行
        SELECT emp_name, salary,
               AVG(salary) OVER (PARTITION BY dept_id) AS 部门平均
        FROM emp;                                                        -- 12 行

    自查：能说出为什么一个 4 行、一个 12 行。

第 2 块（30 分钟）排名三兄弟
    读：第 5 节
    敲：部门内按薪资降序，同时输出 ROW_NUMBER / RANK / DENSE_RANK 三列
    再敲第 5 节那个 90/90/85/80 的造数据，看并列时的差异
    自查：给你 90、90、85 三个人，能立刻写出三列结果（1 1 3 / 1 1 2）。

第 3 块（40 分钟）占比 + 累计
    读：第 6 节的 (1)(2)(3)，其余先跳过
    敲：部门内薪资占比；dept_id = 1 的累计
    自查：张伟占比 37.31%；累计到吴磊是 67000。

休息（15 分钟）
    离开屏幕，别刷手机。

第 4 块（35 分钟）窗口帧 + LAST_VALUE 坑
    读：第 8 节
    敲：先跑"错的" LAST_VALUE，再跑"对的"（加 ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING），对比输出
    自查：能解释为什么错的版本每一行都等于自己。

第 5 块（30 分钟）三个必会题型
    读：第 10 节的题 1、题 2、题 6
    敲：每部门前 2 名、每人占比、每部门去重取第一
    自查：不看笔记能独立写出来，且知道外层为什么要包子查询。

收尾（5 分钟）
    做第 13 节自测 6 题；把今天卡住的点补到文件末尾。
    今天的产出：一张"三条排名函数 + TopN"的 SQL 截图，明天开工前看一眼。

今天不学（明天再补，不影响入门）
    LAG / LEAD 环比（第 7 节后半）
    NTILE 分档
    GROUP BY 再套窗口 SUM(SUM(salary)) OVER ()
    性能优化（第 12 节）
    CTE 写法（第 9 节最后）

如果只剩 1 小时（最小闭环）
    第 1 块 20 分钟 + 第 2 块 20 分钟 + 题 1 TopN 20 分钟。
    这三样会了，窗口函数就算入门，剩下的明天补。


============================================================
1. 一句话理解：窗口函数解决什么问题
============================================================
普通聚合（GROUP BY）会把多行压成一行，明细就没了。
窗口函数不压缩行：每一行都保留，同时能"看到"它所在的那一组。

    需求：显示每个员工的薪资，以及他所在部门的平均薪资。

用 GROUP BY 做不到（要么只剩 4 行，要么得再 JOIN 回去）：

    SELECT dept_id, AVG(salary) FROM emp GROUP BY dept_id;   -- 只剩 4 行

用窗口函数一步到位（12 行，每行都带部门平均）：

    SELECT emp_name, dept_id, salary,
           AVG(salary) OVER (PARTITION BY dept_id) AS 部门平均
    FROM emp;

"窗口"这个词的意思：当前行有一个"可见范围"（窗口），
聚合函数在这个范围里计算，然后把结果贴回当前行。


============================================================
2. 与 GROUP BY 的区别（最重要的一张对比）
============================================================
                     GROUP BY                   窗口函数
-------------------  -------------------------  --------------------------
输出的行数           每组一行（行数变少）        原样保留每一行
能不能看明细         不能                        能
能不能再排序取前 N   要 HAVING / 子查询绕         直接 ROW_NUMBER 后筛
写在哪里             GROUP BY 子句               SELECT 列表里
能不能出现在 WHERE   不能                        不能（要用子查询包一层）
典型用途             统计汇总                    排名、占比、累计、环比

一句话：
    GROUP BY 是"折叠"，窗口函数是"透视"。
    要汇总成几行 → GROUP BY；要在明细旁边加一列统计值 → 窗口函数。


============================================================
3. 语法骨架：OVER 里的三样东西
============================================================
    函数名(...) OVER (
        PARTITION BY 分组列     -- ① 分几组（不写 = 全表一组）
        ORDER BY    排序列       -- ② 组内怎么排（不写 = 顺序不确定）
        ROWS BETWEEN ... AND ... -- ③ 窗口帧：算到哪一行为止
    )

① PARTITION BY
    相当于 GROUP BY，但不会合并行。
    不写：整个结果集是一个窗口。
    写 PARTITION BY dept_id：每个部门各自一个窗口。

② ORDER BY
    决定"累计"的方向和"排名"的依据。
    不写：同组内所有行一视同仁（排名类函数会给出不确定的顺序）。

③ 窗口帧
    只在需要"逐行累计"时才用，默认值是 RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW。
    见第 8 节。

最常见的两种写法：

    -- 只分组，不排序（算组内平均、占比）
    AVG(salary) OVER (PARTITION BY dept_id)

    -- 分组 + 排序（算排名、累计）
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC)


============================================================
4. 三类窗口函数总表
============================================================
类别      函数                                  作用
--------  ------------------------------------  --------------------------
聚合类    SUM / AVG / COUNT / MAX / MIN         组内累计、组内平均、占比
排序类    ROW_NUMBER / RANK / DENSE_RANK / NTILE 编号、排名、分档
偏移类    LAG / LEAD                            取上一行 / 下一行
取值类    FIRST_VALUE / LAST_VALUE / NTH_VALUE  取组内首尾、第 N 个

记忆：聚合类算"数"，排序类排"名次"，偏移类看"前后"。


============================================================
5. 排序类三兄弟：ROW_NUMBER / RANK / DENSE_RANK
============================================================
先看并列时的差异（造的数据：A=90 B=90 C=85 D=80）：

    name  score  序号(ROW_NUMBER)  排名(RANK)  密集排名(DENSE_RANK)
    A     90     1                 1           1
    B     90     2                 1           1
    C     85     3                 3           2
    D     80     4                 4           3

    ROW_NUMBER  不管并列，硬编号 1 2 3 4（顺序不确定，除非 ORDER BY 能区分）
    RANK        并列同名次，后面的名次"跳号"（1 1 3 4）
    DENSE_RANK  并列同名次，后面的名次"不跳号"（1 1 2 3）

选择口诀：
    要"每人一个不重复的行号" → ROW_NUMBER
    要"第几名（允许并列、允许跳号）" → RANK
    要"第几档（并列不占名额）" → DENSE_RANK

在 emp 上的实际效果（各部门内的薪资排名）：

    SELECT d.dept_name, e.emp_name, e.salary,
           ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS 序号,
           RANK()       OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS 排名,
           DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS 密集排名
    FROM emp e
    JOIN dept d ON d.dept_id = e.dept_id
    ORDER BY e.dept_id, e.salary DESC;

    结果（数据里没有并列，所以三列一样）：
    研发部 张伟 25000 → 1 1 1
    研发部 李娜 18000 → 2 2 2
    研发部 王强 15000 → 3 3 3
    研发部 吴磊  9000 → 4 4 4
    市场部 刘洋 22000 → 1 1 1
    ...（共 12 行）

NTILE(n)
    把结果平均分成 n 档，返回档位 1..n。

    SELECT emp_name, salary, NTILE(4) OVER (ORDER BY salary DESC) AS 档位
    FROM emp ORDER BY salary DESC;

    12 人分 4 档 → 每档 3 人：
    1 档 张伟/刘洋/李娜，4 档 冯超/吴磊/孙悦。


============================================================
6. 聚合类窗口：SUM / AVG / COUNT
============================================================
(1) 组内平均（不排序 → 整组一起算）

    SELECT emp_name, dept_id, salary,
           AVG(salary) OVER (PARTITION BY dept_id) AS 部门平均
    FROM emp;

    研发部 4 人：16750
    市场部 4 人：14875
    财务部 2 人：12500
    人事部 2 人：9000

(2) 组内占比

    SELECT emp_name, dept_id, salary,
           ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY dept_id), 2) AS 占比
    FROM emp;

    张伟 25000 / 67000 = 37.31%
    李娜 18000 / 67000 = 26.87%
    王强 15000 / 67000 = 22.39%
    吴磊  9000 / 67000 = 13.43%

(3) 组内累计（要 ORDER BY，默认就是"从组内第一行累加到当前行"）

    SELECT emp_name, salary,
           SUM(salary) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS 累计
    FROM emp WHERE dept_id = 1 ORDER BY salary DESC;

    张伟 25000 → 25000
    李娜 18000 → 43000
    王强 15000 → 58000
    吴磊  9000 → 67000

(4) COUNT(*) OVER ()
    不写 PARTITION，等于"全表一共多少行"，可以给每一行贴一个总数。

    SELECT emp_name, salary, COUNT(*) OVER () AS 总人数 FROM emp;

(5) 与 GROUP BY 混用
    可以先用 GROUP BY 汇总，再用窗口函数在汇总结果上算占比：

    SELECT dept_id, SUM(salary) AS 部门总额,
           ROUND(SUM(salary) * 100.0 / SUM(SUM(salary)) OVER (), 2) AS 占公司比例
    FROM emp GROUP BY dept_id;

    注意 SUM(SUM(salary)) OVER ()：里层 SUM 是分组聚合，外层 SUM 是窗口聚合。


============================================================
7. 偏移类：LAG / LEAD / FIRST_VALUE / LAST_VALUE / NTILE
============================================================
LAG(列, n, 默认值)   取"往前第 n 行"的值，默认 n=1
LEAD(列, n, 默认值)  取"往后第 n 行"的值
    第一行没有"上一行"，LAG 返回 NULL（可以用第 3 个参数给默认值）。

    SELECT emp_name, hire_date,
           LAG(emp_name)  OVER (ORDER BY hire_date) AS 上一位入职,
           LAG(hire_date) OVER (ORDER BY hire_date) AS 上一位日期
    FROM emp ORDER BY hire_date;

    结果（前几行）：
    张伟 2015-06-01  NULL        NULL
    刘洋 2016-04-20  张伟        2015-06-01
    赵敏 2017-02-13  刘洋        2016-04-20
    李娜 2018-09-10  赵敏        2017-02-13
    郑爽 2019-05-05  李娜        2018-09-10

    常见用途：算环比（本月 vs 上月）、算两次事件间隔。
    MySQL 里算天数差：DATEDIFF(hire_date, LAG(hire_date) OVER (ORDER BY hire_date))

FIRST_VALUE(列)  取窗口内第一行
LAST_VALUE(列)   取窗口内最后一行
    这两个对"窗口帧"很敏感，见第 8 节。

NTH_VALUE(列, n) 取窗口内第 n 行


============================================================
8. 窗口帧：ROWS / RANGE，以及 LAST_VALUE 的坑
============================================================
窗口帧 = "当前行能看到哪一段"。写法：

    ROWS BETWEEN 起点 AND 终点

常用组合：
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW        从组内第一行到当前行（累计）
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING                前后各一行（移动平均）
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 整组
    ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING        当前行到最后

关键规则（MySQL 默认）：
    有 ORDER BY 时，默认帧是 RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    没有 ORDER BY 时，默认帧是整组

坑：LAST_VALUE 拿不到"组内最后一个"
    因为默认帧到"当前行"就结束了，所以 LAST_VALUE 得到的其实就是"当前行自己"。

    反例（dept_id = 1，按薪资升序）：

        SELECT emp_name, salary,
               LAST_VALUE(emp_name) OVER (PARTITION BY dept_id ORDER BY salary) AS 值
        FROM emp WHERE dept_id = 1 ORDER BY salary;

        吴磊 9000  → 吴磊
        王强 15000 → 王强
        李娜 18000 → 李娜
        张伟 25000 → 张伟        -- 全是自己，根本没有"最高薪者"

    正确写法：把帧显式扩大到整组

        SELECT emp_name, salary,
               LAST_VALUE(emp_name) OVER (
                   PARTITION BY dept_id ORDER BY salary
                   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
               ) AS 部门最高薪者
        FROM emp WHERE dept_id = 1 ORDER BY salary;

        吴磊 9000  → 张伟
        王强 15000 → 张伟
        李娜 18000 → 张伟
        张伟 25000 → 张伟        -- 四行都对了

ROWS 和 RANGE 的区别：
    ROWS  按"物理行数"数（前后几行）
    RANGE 按"排序值"数（值相同的行算一组，并列时行为可能不一样）
    初学者先统一用 ROWS，行为最好预测。


============================================================
9. 执行顺序：为什么窗口函数不能写在 WHERE 里
============================================================
    FROM → WHERE → GROUP BY → HAVING → 窗口函数 → SELECT → ORDER BY → LIMIT

窗口函数在 WHERE 之后才算出来，所以 WHERE 里根本看不到它。
这样写会报错：

    SELECT * FROM emp WHERE ROW_NUMBER() OVER (ORDER BY salary DESC) <= 3;
    -- ERROR 3593: You cannot use the window function 'row_number' in this context

正确做法：套一层子查询（或 CTE），在外面筛

    SELECT * FROM (
        SELECT emp_name, salary,
               ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
        FROM emp
    ) t
    WHERE rn <= 3;

    -- CTE 写法（MySQL 8 支持）
    WITH ranked AS (
        SELECT emp_name, salary,
               ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
        FROM emp
    )
    SELECT * FROM ranked WHERE rn <= 3;

记忆：窗口函数是"SELECT 阶段的产物"，想筛它，必须再包一层。


============================================================
10. 六个经典题型（都能直接跑）
============================================================
题 1  每个部门薪资前 2 名

    SELECT * FROM (
        SELECT d.dept_name, e.emp_name, e.salary,
               ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rn
        FROM emp e JOIN dept d ON d.dept_id = e.dept_id
    ) t
    WHERE rn <= 2
    ORDER BY dept_name, rn;

    结果 8 行（4 个部门 × 2 人）。
    想保留"并列第 2 名"就换成 RANK()，并把条件写成 rn <= 2。

题 2  每人在部门内的薪资占比

    SELECT emp_name, dept_id, salary,
           ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY dept_id), 2) AS 占比
    FROM emp;

题 3  部门内按薪资从高到低累计

    SELECT emp_name, salary,
           SUM(salary) OVER (PARTITION BY dept_id ORDER BY salary DESC
                             ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS 累计
    FROM emp WHERE dept_id = 1;

题 4  与部门平均对比（高出多少、低出多少）

    SELECT emp_name, salary,
           ROUND(AVG(salary) OVER (PARTITION BY dept_id), 2) AS 部门平均,
           ROUND(salary - AVG(salary) OVER (PARTITION BY dept_id), 2) AS 差额
    FROM emp;

    张伟 25000 / 16750 / +8250
    李娜 18000 / 16750 / +1250
    王强 15000 / 16750 / -1750
    吴磊  9000 / 16750 / -7750

题 5  按入职时间看"上一位入职的同事"（环比思路）

    SELECT emp_name, hire_date,
           LAG(emp_name) OVER (ORDER BY hire_date) AS 上一位入职
    FROM emp ORDER BY hire_date;

题 6  去重：每个部门只留薪资最高的一行

    SELECT * FROM (
        SELECT e.*,
               ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
        FROM emp e
    ) t
    WHERE rn = 1;

    结果 4 行：张伟 / 刘洋 / 赵敏 / 郑爽。


============================================================
11. 八个坑
============================================================
(1) 把窗口函数写进 WHERE
    ERROR 3593，必须包一层子查询。

(2) 以为 RANK 和 DENSE_RANK 一样
    有并列时才不同：RANK 跳号（1 1 3），DENSE_RANK 不跳（1 1 2）。

(3) LAST_VALUE / FIRST_VALUE 忘了窗口帧
    默认帧到当前行为止，LAST_VALUE 等于当前行自己（见第 8 节）。

(4) 只写 ORDER BY 不写 PARTITION
    整个结果集被当成一个窗口，排名会变成"全公司排名"而不是"部门内排名"。

(5) 以为 ROW_NUMBER 的顺序是稳定的
    如果 ORDER BY 的列有重复值，并列行的顺序由数据库决定，每次可能不同。
    要稳定就在 ORDER BY 里加一个唯一列（比如 emp_id）。

(6) 在 GROUP BY 的结果上再套窗口，写成了 SUM(SUM(x)) 却没加 OVER
    里层是分组聚合，外层必须写 OVER () 才是窗口聚合。

(7) 窗口函数嵌套
    SUM(AVG(x) OVER (...)) OVER (...) 不合法；需要分两步用子查询。

(8) 性能：窗口函数通常要排序
    数据量大时，PARTITION BY + ORDER BY 会触发排序；
    尽量让排序列有索引，或者先在子查询里过滤掉不需要的行。


============================================================
12. 性能提示
============================================================
1) 窗口函数在数据量小时随便写；上百万行时要看执行计划（EXPLAIN）。
2) PARTITION BY 的列优先走索引，能减少排序开销。
3) 先用 WHERE 缩小结果集，再算窗口，比先算再筛快得多。
4) 能用 GROUP BY 汇总解决的，不要用窗口函数（窗口不压缩行，内存占用更高）。
5) 相关子查询能改写成窗口函数的，通常更快（少一次逐行扫描）。


============================================================
13. 自测 6 题
============================================================
1) GROUP BY 和窗口函数最本质的区别是什么？
2) 90、90、85 三个人，RANK 和 DENSE_RANK 分别给出什么名次？
3) 想按部门排名，OVER 里必须写哪一句？
4) 为什么 WHERE rn <= 3 不能直接写在窗口函数同一层？
5) LAST_VALUE 取不到"组内最后一个"，原因是什么？怎么改？
6) ROWS 和 RANGE 有什么区别？

参考答案：
1) GROUP BY 把多行压成一行，窗口函数保留每一行
2) RANK：1 1 3；DENSE_RANK：1 1 2
3) PARTITION BY dept_id（再配 ORDER BY 排序列）
4) 窗口函数在 WHERE 之后才计算，必须包一层子查询/CTE
5) 默认窗口帧到当前行为止；显式写 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
6) ROWS 按物理行数，RANGE 按排序值（并列值会一起算）


============================================================
附录：emp 表字段速查
============================================================
    emp_id     员工编号
    emp_name   姓名
    salary     薪资
    bonus_ratio 奖金比例
    birthday   生日
    gender     性别
    phone / email / address / work_place
    hire_date  入职日期
    job_id     岗位编号  → job.job_id
    manager_id 领导编号  → emp.emp_id（自关联）
    dept_id    部门编号  → dept.dept_id

    dept：dept_id, dept_name, dept_desc
    job ：job_id, job_name, job_desc
"""