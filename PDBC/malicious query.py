import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
name=input("enter user")
query="select * from dbemployee2 where name='' or '1'='1'"
cursor.execute(query)
rows=cursor.fetchall()
print(rows)
print("success")

conn.close()
