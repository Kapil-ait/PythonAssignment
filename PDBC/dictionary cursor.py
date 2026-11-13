import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor(dictionary=True)
cursor.execute("select * from dbemployee2")
row=cursor.fetchone()
print(row)
print(row['name'])
print("success")

conn.close()
