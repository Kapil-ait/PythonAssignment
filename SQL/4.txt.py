mysql> select subject, avg(marks) from students group by subject having avg(marks)>80;
+---------+------------+
| subject | avg(marks) |
+---------+------------+
| Math    |    88.0000 |
+---------+------------+
1 row in set (0.00 sec)

mysql> select class, count(*) from students group by class order by class desc;
+-------+----------+
| class | count(*) |
+-------+----------+
|    10 |        5 |
|     9 |        5 |
+-------+----------+
2 rows in set (0.00 sec)

mysql> select subject, avg(marks) from students group by subject having avg(marks)>85 order by avg(marks) desc limit 1;
+---------+------------+
| subject | avg(marks) |
+---------+------------+
| Math    |    88.0000 |
+---------+------------+
1 row in set (0.00 sec)

mysql> select name, marks from students order by marks desc limit 1;
+------+-------+
| name | marks |
+------+-------+
| Bob  |    92 |
+------+-------+
1 row in set (0.00 sec)

mysql> select class, count(*) from students where marks>85 group by class having count(*)>2;
Empty set (0.00 sec)

mysql> select class, count(*) from students where marks>85 group by class having count(*)>2;
Empty set (0.00 sec)