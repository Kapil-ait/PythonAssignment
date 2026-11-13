import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
id=int(input("enter id:"))
name=input("enter name")
sal=float(input("enter salary"))
query="insert into dbemployee2(id,name,salary) values(%s,%s,%s)"
cursor.execute(query,(id,name,sal))
conn.commit()
print("success")

conn.close()
