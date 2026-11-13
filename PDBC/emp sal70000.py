import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
cursor.execute("select * from dbemployee2 where salary>7000")
for i in cursor:
    print(i)
print("success")

conn.close()
