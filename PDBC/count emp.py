import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
cursor.execute("select * from dbemployee2 ")
rows=cursor.fetchall()
print("len is",len(rows))

print("success")

conn.close()
