import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
name=input("enter name")
sal=float(input("enter salary"))
query="select * from dbemployee2 where name=%s and salary>%s"
cursor.execute(query,(name,sal))
rows=cursor.fetchall()
print(rows)
print("success")

conn.close()
