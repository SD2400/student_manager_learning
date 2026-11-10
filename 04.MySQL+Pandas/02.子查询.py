"""
MySQL 子查询 · 学习笔记

整理日期：2026-11-06
配套文件：
    02.子查询-建表与数据.sql   建表 + 数据（dept / job / emp）
    03.子查询-练习.sql         6 道动手练习

目录
     0. 一句话理解
     1. 什么是子查询
     2. 按"返回结果"分类（四种）
     3. 按"放置位置"分类（五个位置）
     4. 相关子查询 vs 不相关子查询
     5. 运算符与匹配方式
     6. 行构造器：每组取最大值
     7. 典型题型（结合 dept / job / emp）
     8. 八个坑（含 MySQL 报错编号）
     9. 子查询 vs JOIN，什么时候用哪个
    10. 自测 6 题


============================================================
0. 一句话理解
============================================================
子查询 = 把一条 SELECT 的结果，当成另一条 SELECT 的
         "一个值 / 一组值 / 一张临时表" 来用。

问：我需要的条件，能不能先用一条 SELECT 算出来？
能 → 就用子查询。


============================================================
1. 什么是子查询
============================================================
嵌套在另一个 SQL 语句内部的 SELECT，必须用小括号包起来。

    SELECT emp_name, salary
    FROM emp
    WHERE salary > (SELECT AVG(salary) FROM emp);   -- 括号里就是子查询

执行顺序（不相关子查询）：
    先算括号里的 → 得到一个值 → 外层拿这个值当条件

常见误区：以为子查询"必须写在 WHERE 里"。
实际上 WHERE / FROM / SELECT / HAVING 都能放，作用各不相同（见第 3 节）。


============================================================
2. 按"返回结果"分类（四种）
============================================================
类型        返回什么        常用运算符          例子
----------  --------------  ------------------  --------------------------------
标量子查询  1 行 1 列        =  >  <  >=  <=    salary > (SELECT AVG(salary) ...)
            一个值          <>                  dept_id = (SELECT dept_id ...)
列子查询    多行 1 列        IN / NOT IN         dept_id IN (SELECT dept_id ...)
            一组值          ANY / ALL
行子查询    1 行 多列        (a,b) = (...)       (dept_id, salary) IN (SELECT ...)
表子查询    多行 多列        FROM 里当表用       FROM (SELECT ...) t

记忆：先看子查询"吐出几行几列"，再决定外层用什么运算符。


============================================================
3. 按"放置位置"分类（五个位置）
============================================================
(1) WHERE 里：最常用，做过滤

    SELECT emp_name FROM emp
    WHERE salary > (SELECT AVG(salary) FROM emp);

(2) FROM 里：子查询当"临时表"（派生表），必须起别名

    SELECT d.dept_name, t.平均薪资
    FROM (SELECT dept_id, AVG(salary) AS 平均薪资
          FROM emp GROUP BY dept_id) t          -- t 这个别名不能省
    JOIN dept d ON d.dept_id = t.dept_id;

    注意：不起别名 MySQL 会报
          ERROR 1248: Every derived table must have its own alias

(3) SELECT 里：给每一行算一个值

    SELECT emp_name, salary,
           (SELECT ROUND(AVG(salary), 2) FROM emp) AS 公司平均
    FROM emp;

(4) HAVING 里：分组之后再过滤

    SELECT dept_id, AVG(salary) AS 平均
    FROM emp
    GROUP BY dept_id
    HAVING AVG(salary) > (SELECT AVG(salary) FROM emp);   -- 高于公司平均的部门

(5) EXISTS 里：只判断"有没有"

    SELECT d.dept_name
    FROM dept d
    WHERE EXISTS (SELECT 1 FROM emp e WHERE e.dept_id = d.dept_id);


============================================================
4. 相关子查询 vs 不相关子查询
============================================================
不相关（独立）
    子查询里不出现外层的列 → 只执行一次 → 结果可复用 → 快

    WHERE salary > (SELECT AVG(salary) FROM emp)

相关（correlated）
    子查询里引用了外层的列 → 外层每来一行，子查询就执行一次 → 慢

    WHERE e.salary = (SELECT MAX(e2.salary)
                      FROM emp e2
                      WHERE e2.dept_id = e.dept_id)   -- 用到外层的 e.dept_id

怎么判断：子查询里有没有出现"外层表的列"。有 → 相关。

直觉：不相关 = "先算好一个数"；相关 = "每行现算一次"。
数据量大时，相关子查询容易变慢，可以考虑改成 JOIN。


============================================================
5. 运算符与匹配方式
============================================================
运算符            右边允许什么                      说明
----------------  --------------------------------  --------------------------
=  >  <  >=  <=   单个值（标量子查询）              最严格，多行多列都不行
IN / NOT IN       一列多行，或"行"对多行            最常用，匹配集合
EXISTS / NOT      不看列，只看有没有行              过滤"存在/不存在"
EXISTS
ANY / SOME        > ANY(集合) = 大于最小值         等价于 > MIN(...)
ALL               > ALL(集合) = 大于最大值         等价于 > MAX(...)

ANY / ALL 的时间线对照：

    salary > ANY (SELECT salary FROM emp)   -- 比最低的那个人高就行
    salary > ALL (SELECT salary FROM emp)   -- 比所有人都高（= 最高）

记忆：
    = 管一个点，IN 管一堆点，EXISTS 管"有没有"，ANY/ALL 管比较的范围。


============================================================
6. 行构造器：每组取最大值
============================================================
需求：每个部门里薪资最高的那个人。

错误写法（很多人第一反应）：

    WHERE dept_id, salary = (SELECT dept_id, MAX(salary) FROM emp GROUP BY dept_id)

错在两个地方：
    1) WHERE 里不能用逗号并列条件 → ERROR 1064 语法错误
    2) = 右边要求单值，这里返回 2 列 × 多行 → 报 1241 / 1242

正确写法 A：行构造器 + IN（最简洁）

    SELECT emp_name, salary
    FROM emp
    WHERE (dept_id, salary) IN (
            SELECT dept_id, MAX(salary) FROM emp GROUP BY dept_id
          );

    (dept_id, salary) 是把两列当成一个"元组"整体比较，
    所以要求两边列数一致、顺序一致。

正确写法 B：相关子查询（逐行算）

    SELECT e.emp_name, e.salary
    FROM emp e
    WHERE e.salary = (SELECT MAX(e2.salary)
                      FROM emp e2 WHERE e2.dept_id = e.dept_id);

正确写法 C：派生表 JOIN

    SELECT e.emp_name, e.salary
    FROM emp e
    JOIN (SELECT dept_id, MAX(salary) AS m FROM emp GROUP BY dept_id) t
      ON t.dept_id = e.dept_id AND e.salary = t.m;

三种结果完全一样（4 行：张伟 / 刘洋 / 赵敏 / 郑爽）。
另外：如果某部门有两人并列最高，三种写法都会把两人都查出来。


============================================================
7. 典型题型（结合 dept / job / emp）
============================================================
题 1  薪资高于公司平均的人
    WHERE salary > (SELECT AVG(salary) FROM emp)

题 2  查某个部门的所有人
    WHERE dept_id IN (SELECT dept_id FROM dept WHERE dept_name = '研发部')

题 3  薪资最高的人
    WHERE salary = (SELECT MAX(salary) FROM emp)

题 4  每个部门薪资最高的人
    见第 6 节，三种写法

题 5  没有员工的部门
    WHERE dept_id NOT IN (SELECT dept_id FROM emp WHERE dept_id IS NOT NULL)
    或
    WHERE NOT EXISTS (SELECT 1 FROM emp e WHERE e.dept_id = d.dept_id)

题 6  比本部门平均薪资高的人（相关子查询）
    WHERE e.salary > (SELECT AVG(e2.salary) FROM emp e2
                      WHERE e2.dept_id = e.dept_id)

题型识别口诀：
    "高于平均/最高/最低"  → 标量子查询
    "属于某个集合"        → IN
    "没有/不存在"         → NOT IN 或 NOT EXISTS
    "每个部门/每组"       → 相关子查询或派生表


============================================================
8. 八个坑（含 MySQL 报错编号）
============================================================
(1) 子查询返回多行，却用 = 比较
    ERROR 1242 (21000): Subquery returns more than 1 row
    解决：改成 IN，或让子查询返回单值（加 LIMIT 1 / 聚合函数）

(2) 子查询返回多列，却当成一个值用
    ERROR 1241 (21000): Operand should contain 1 column(s)
    解决：只 SELECT 一列，或用行构造器 (a, b) IN (...)

(3) 在 WHERE 里用逗号并列两个条件
    ERROR 1064: You have an error in your SQL syntax
    解决：用 AND 连接

(4) NOT IN 遇到 NULL（最阴险的坑）
    如果子查询结果里含 NULL，NOT IN 会返回"空结果"，一行都查不到。
    因为 x NOT IN (NULL, ...) 等价于 x <> NULL，结果是 UNKNOWN，不是真。

    反例：
        WHERE dept_id NOT IN (SELECT dept_id FROM emp)
        -- 只要 emp.dept_id 里有 NULL，这条就永远查不出东西

    解决：子查询里加 WHERE dept_id IS NOT NULL，或改用 NOT EXISTS

(5) FROM 里的子查询没起别名
    ERROR 1248: Every derived table must have its own alias

(6) 把子查询写在 WHERE 里，但外层没用到索引
    相关子查询在大表上可能极慢，考虑改写为 JOIN

(7) 子查询里用 ORDER BY 却没 LIMIT
    大部分场景下没意义，MySQL 可能直接忽略

(8) 子查询套太深（三四层）
    能读懂，但难维护；先想想能不能拆成两步或用 JOIN


============================================================
9. 子查询 vs JOIN，什么时候用哪个
============================================================
看需求：

    只需要"过滤"（这个人符不符合条件）        → 子查询更直观
    需要"显示对方的列"（还要部门名称）        → JOIN
    需要"存在/不存在"的判断                   → EXISTS / NOT EXISTS
    需要"每组取最大/合计"再来筛选             → 派生表 + JOIN，或相关子查询

性能上的现实：
    现代 MySQL 优化器经常把 IN 子查询自动改写成 JOIN（半连接），
    所以"子查询一定比 JOIN 慢"是错的。
    真正要担心的是"相关子查询"在大表上逐行执行。

经验法则：
    先写清楚，再谈优化；用 EXPLAIN 看执行计划，别凭感觉。


============================================================
10. 自测 6 题
============================================================
1) 子查询返回 3 行，外层用 = 比较，会报什么错？
2) 想在 FROM 里用子查询，最容易漏掉什么？
3) NOT IN 什么时候会"查不出任何数据"？
4) "每个部门薪资最高的人"有哪三种写法？
5) 相关子查询和不相关子查询，怎么一眼判断？
6) EXISTS 和 IN 的区别是什么？

参考答案：
1) ERROR 1242 Subquery returns more than 1 row，改用 IN
2) 别名（ERROR 1248 Every derived table must have its own alias）
3) 子查询结果里含 NULL 时；解决：加 IS NOT NULL 或改用 NOT EXISTS
4) 行构造器 (a,b) IN (...)；相关子查询；派生表 JOIN
5) 看子查询里有没有引用外层的列；有就是相关
6) IN 比较的是"值在不在集合里"，EXISTS 只看"有没有行"；
   EXISTS 遇到 NULL 也不会出错，通常也更高效


============================================================
附：三张表的字段（方便写 SQL 时查）
============================================================
    dept：dept_id, dept_name, dept_desc
    job ：job_id, job_name, job_desc
    emp ：emp_id, emp_name, salary, bonus_ratio, birthday, gender,
          phone, email, address, work_place, hire_date,
          job_id, manager_id, dept_id

    外键：emp.job_id → job.job_id
          emp.dept_id → dept.dept_id
          emp.manager_id → emp.emp_id（自关联）
"""