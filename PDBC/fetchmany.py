import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
cursor.execute("select * from dbemployee2")
print("getting data from cursor")
print(cursor.fetchmany(2))
print("success")

conn.close()
