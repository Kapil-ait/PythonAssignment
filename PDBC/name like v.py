import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
p=input("enter pattern")
query="select * from dbemployee2 where name like %s"
cursor.execute(query,(p+'%',))
for i in cursor:
    print(i)
conn.commit()
print("success")

conn.close()
