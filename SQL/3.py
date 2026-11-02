mysql> select department, count(*) from employees group by department having count(*)>2;
+------------+----------+
| department | count(*) |
+------------+----------+
| HR         |        3 |
| IT         |        4 |
| Finance    |        3 |
+------------+----------+
3 rows in set (0.00 sec)

mysql> select department, sum(salary) from employees group by department order by sum(salary) desc;
+------------+-------------+
| department | sum(salary) |
+------------+-------------+
| IT         |    19800.00 |
| Finance    |    17500.00 |
| HR         |    14200.00 |
+------------+-------------+
3 rows in set (0.00 sec)

mysql> select job_role, sum(salary) from employees group by job_role having sum(salary)>10000 order by sum(salary) desc;
+-----------+-------------+
| job_role  | sum(salary) |
+-----------+-------------+
| Manager   |    13000.00 |
| Developer |    10500.00 |
| Analyst   |    10500.00 |
+-----------+-------------+
3 rows in set (0.00 sec)

mysql> select job_role, avg(salary) from employees where hire_date>'2022-12-31' group by job_role having avg(salary)>4500;
+----------+-------------+
| job_role | avg(salary) |
+----------+-------------+
| Tester   | 4650.000000 |
| Manager  | 7000.000000 |
+----------+-------------+
2 rows in set (0.00 sec)

mysql> select department, sum(salary) from employees group by department having sum(salary)>10000 order by department asc;
+------------+-------------+
| department | sum(salary) |
+------------+-------------+
| Finance    |    17500.00 |
| HR         |    14200.00 |
| IT         |    19800.00 |
+------------+-------------+
3 rows in set (0.01 sec)
