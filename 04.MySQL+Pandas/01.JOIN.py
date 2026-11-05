"""
MySQL 中的 JOIN · 速查笔记

整理日期：2026-11-05
说明：本文件是纯笔记（只有一个多行字符串），不含可执行逻辑，直接打开阅读即可。
      练习数据的建表语句和 10 道题在文末「附录 A」。


============================================================
0. 一句话本质
============================================================
JOIN = 拿"主表"的每一行，去"从表"里找能配上的行，拼成一行。
配不上的怎么办？——这就是各种 JOIN 的唯一区别。

判断只看一个问题：哪边的行"一个都不能少"？


============================================================
1. 五种连接：谁被保留
============================================================
类型    配不上时          一句话口诀                  示例数据行数
------  ----------------  --------------------------  ------------
INNER   两侧都不留        只留配对成功的              3
LEFT    右侧补 NULL       左表全留                    5
RIGHT   左侧补 NULL       右表全留                    4
FULL    两侧都补 NULL     两边全留（MySQL 不支持）    6
CROSS   不判断配对        全部组合 m×n                16

示例数据：4 个用户、4 条订单（其中 user_id=9 的用户不存在）。
同一份数据，五种连接得到 3 / 5 / 4 / 6 / 16 行——记住这五个数，比背定义管用。

口诀：内连接不留孤儿，左连接保左，右连接保右，全连接谁都保，交叉连接乱点鸳鸯。

写法：

    -- 内连接
    SELECT a.字段1, b.字段2 FROM 表A a INNER JOIN 表B b ON a.键 = b.键;

    -- 左连接 / 右连接
    SELECT a.字段1, b.字段2 FROM 表A a LEFT  JOIN 表B b ON a.键 = b.键;
    SELECT a.字段1, b.字段2 FROM 表A a RIGHT JOIN 表B b ON a.键 = b.键;

    -- 交叉连接
    SELECT a.字段1, b.字段2 FROM 表A a CROSS JOIN 表B b;

    -- 全外连接：MySQL 不支持 FULL JOIN，必须用 UNION 模拟
    SELECT a.字段1, b.字段2 FROM 表A a LEFT  JOIN 表B b ON a.键 = b.键
    UNION
    SELECT a.字段1, b.字段2 FROM 表A a RIGHT JOIN 表B b ON a.键 = b.键;


============================================================
2. 怎么选（决策顺序）
============================================================
问：哪张表的行不能丢？
    ├─ 右表（业务主表）     → LEFT JOIN
    ├─ 左表（业务主表）     → RIGHT JOIN（或换个书写顺序改用 LEFT）
    ├─ 都不能丢             → FULL（MySQL 用 LEFT UNION RIGHT）
    ├─ 只关心能对上的       → INNER JOIN
    └─ 要生成所有组合       → CROSS JOIN

工程里 90% 用 LEFT JOIN。用 INNER 前先问："配不上的那行数据丢了要紧吗？"


============================================================
3. 三对双胞胎（必考）
============================================================
A              B               区别
-------------  --------------  --------------------------------------
COUNT(*)       COUNT(b.id)     数行数（含 NULL 补的行） vs 数非空
WHERE          HAVING          分组前筛行 vs 分组后筛组
UNION          UNION ALL       去重（慢） vs 不去重（快）

没下过单的用户：COUNT(*) 给 1，COUNT(o.id) 给 0。
统计"每人几单"必须用 COUNT(o.id)。

WHERE 里不能写 SUM() / COUNT() 这类聚合函数，那是 HAVING 的活。


============================================================
4. NULL 三条铁律
============================================================
1) NULL 不能用 = 比较。NULL = NULL 的结果是 UNKNOWN，不是真。
   判断用 IS NULL / IS NOT NULL。

2) 聚合函数会跳过 NULL：COUNT(列)、SUM、AVG 都不理 NULL；
   但 COUNT(*) 数的是行。

3) 对空集聚合得到 NULL，不是 0。SUM() 在没有行时是 NULL，
   所以 HAVING SUM(x) > 100 会把这组过滤掉。
   要显示 0 就写 COALESCE(SUM(x), 0)。


============================================================
5. 手写模板 + 执行顺序
============================================================
    SELECT a.列, COUNT(b.id) AS 数量
    FROM 主表 a
    LEFT JOIN 从表 b ON a.键 = b.键      -- 一个 JOIN 配一个 ON
    WHERE 行级条件                        -- 不能用聚合函数
    GROUP BY a.主键, a.列
    HAVING COUNT(b.id) > 0                -- 这里才能用聚合
    ORDER BY 数量 DESC
    LIMIT 10;

执行顺序：
    FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

这张顺序图决定了 WHERE 和 HAVING 的分工，不要死记。


============================================================
6. 三种变形题
============================================================
反连接：找出没下单的用户
    SELECT u.name FROM users u
    LEFT JOIN orders o ON o.user_id = u.id
    WHERE o.id IS NULL;

自连接：同表找同类（同城市用户）
    SELECT a.name, b.name, a.city
    FROM users a JOIN users b ON a.city = b.city AND a.id < b.id;

    细节：必须加 a.id < b.id，否则 A-B 与 B-A 都出现，还会自己配自己。
          NULL 天生配不上（NULL = NULL 不成立），反而帮你避了坑。

多表链：订单 → 明细 → 商品
    SELECT o.id, u.name, p.name, i.qty
    FROM orders o
    JOIN users u       ON u.id = o.user_id
    JOIN order_items i ON i.order_id = o.id
    JOIN products p    ON p.id = i.product_id;

    注意：一对多会把结果行数放大（一个订单有两条明细就出两行）。


============================================================
7. 五个事故现场
============================================================
1) ON 忘了写 → 退化成笛卡尔积，几万行变几亿行。

2) LEFT JOIN 后又用 WHERE 过滤从表 → 外连接被悄悄退化成内连接。
   写在 ON 里：保留左表所有行，只影响能否配上。
   写在 WHERE 里：配不上的（NULL）行直接被筛掉。

3) 统计从表数量用 COUNT(*) → 没有记录的人也被算成 1。

4) GROUP BY 后 SELECT 了未聚合的列 → 报 ONLY_FULL_GROUP_BY 错。

5) 用 = 比较可能为 NULL 的列 → 明明该匹配却查不出来。


============================================================
8. pandas 对照
============================================================
SQL                                    pandas
-------------------------------------  ------------------------------------------
INNER / LEFT / RIGHT / FULL JOIN       merge(..., how='inner/left/right/outer')
UNION ALL                              pd.concat([a, b])
UNION                                  concat 后 .drop_duplicates()
COUNT(*)                               .size()   （不跳 NaN）
COUNT(列)                              .count()  （跳过 NaN）


============================================================
9. 自测 6 题（先自己答，再看答案）
============================================================
1) 只想看"下过单的用户和订单"用哪种连接？
2) 想看"所有用户，没下单的订单号显示为空"用哪种？
3) MySQL 怎么实现全外连接？
4) LEFT JOIN 后统计每人订单数，用哪个 COUNT？
5) 怎么找出从没下过单的用户？
6) WHERE SUM(x) > 10 这样写对吗？

答案：
1) INNER JOIN
2) LEFT JOIN
3) LEFT UNION RIGHT
4) COUNT(o.id)
5) LEFT JOIN ... WHERE o.id IS NULL（反连接）
6) 不对，聚合条件必须放 HAVING


============================================================
10. 复习节奏（每次 5 分钟）
============================================================
今天    合上这一页，默写「谁被保留」5 行 + 3 对双胞胎
明天    只看第 1 节的表格，把 3/5/4/6/16 对应的 SQL 各写一遍
后天    盲写"反连接"和"每人订单数"，不看答案
一周后  做一遍附录 A 的 10 条题，全对才算真的会

记忆的敌人不是"不懂"，是"看懂了的错觉"。每次复习都要动手写 SQL。


============================================================
附录 A：最小数据集 + 10 条练习题
============================================================

-- 建库建表
CREATE DATABASE IF NOT EXISTS lab_join;
USE lab_join;

CREATE TABLE users(id INT PRIMARY KEY, name VARCHAR(20), city VARCHAR(20));
CREATE TABLE orders(id INT PRIMARY KEY, user_id INT, amount DECIMAL(10,2));
CREATE TABLE products(id INT PRIMARY KEY, name VARCHAR(20), price DECIMAL(10,2));
CREATE TABLE order_items(id INT PRIMARY KEY, order_id INT, product_id INT, qty INT);

INSERT INTO users VALUES
  (1,'张三','北京'),(2,'李四','上海'),(3,'王五','广州'),(4,'赵六',NULL);
INSERT INTO orders VALUES
  (101,1,99.00),(102,1,20.00),(103,2,50.00),(104,9,10.00);
INSERT INTO products VALUES
  (1,'键盘',199.00),(2,'鼠标',99.00),(3,'显示器',899.00);
INSERT INTO order_items VALUES
  (1001,101,1,2),(1002,101,2,1),(1003,102,1,1),(1004,103,3,5),(1005,104,2,1);

-- 10 道题
 1. 内连接：每个订单对应的用户名
 2. 左连接：每个用户和他的订单（没下单的也要出现）
 3. 反连接：找出没有下过单的用户
 4. 右连接：所有订单 + 用户名（注意 9 号"野"订单）
 5. 全外连接：用 LEFT UNION RIGHT 实现
 6. 自连接：找出同城市的用户对（先插一个北京用户才看得到结果）
 7. 三表连接：订单里有什么商品（orders → order_items → products）
 8. 分组 + HAVING：订单总额 > 100 的用户
 9. LEFT JOIN + COUNT(o.id)：每人订单数；再加一列 COUNT(DISTINCT ...)
10. CROSS JOIN：理解笛卡尔积（4 用户 × 4 订单 = 16）

-- 参考写法（先自己做，别急着看）
-- 1
SELECT u.name, o.id FROM orders o JOIN users u ON u.id = o.user_id;
-- 2
SELECT u.name, o.id FROM users u LEFT JOIN orders o ON o.user_id = u.id;
-- 3
SELECT u.name FROM users u LEFT JOIN orders o ON o.user_id = u.id WHERE o.id IS NULL;
-- 4
SELECT o.id, u.name FROM users u RIGHT JOIN orders o ON o.user_id = u.id;
-- 5
SELECT u.name, o.id FROM users u LEFT JOIN orders o ON o.user_id = u.id
UNION
SELECT u.name, o.id FROM users u RIGHT JOIN orders o ON o.user_id = u.id;
-- 6
SELECT a.name, b.name, a.city FROM users a JOIN users b
  ON a.city = b.city AND a.id < b.id;
-- 7
SELECT o.id, u.name, p.name, i.qty, p.price * i.qty AS 小计
FROM orders o
JOIN users u       ON u.id = o.user_id
JOIN order_items i ON i.order_id = o.id
JOIN products p    ON p.id = i.product_id;
-- 8
SELECT u.name, SUM(o.amount) AS 总额 FROM users u LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name HAVING SUM(o.amount) > 100;
-- 9
SELECT u.name, COUNT(*) AS 星号, COUNT(o.id) AS 列计数
FROM users u LEFT JOIN orders o ON o.user_id = u.id GROUP BY u.id, u.name;
-- 10
SELECT COUNT(*) FROM users CROSS JOIN orders;


============================================================
附录 B：勘误与提醒
============================================================
1) MySQL 没有 FULL OUTER JOIN。之前写的
       FROM 表A a FULL JOIN 表B b
   在 MySQL 里会直接报语法错误，正确写法见第 1 节的 LEFT UNION RIGHT。

2) UNION 自带去重（要对整行排序比较，慢）；确定不会重复时用 UNION ALL。

3) SQLite / PostgreSQL 支持 FULL JOIN，网上示例不一定适用于 MySQL——
   照抄前先看数据库类型。

4) 本文件是笔记，不是可运行脚本；要练 SQL 请把附录 A 的语句放到
   MySQL 客户端（或 Navicat / DBeaver）里执行。
"""