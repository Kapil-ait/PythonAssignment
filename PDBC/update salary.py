import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
id=int(input("enter id:"))
salary=float(input("enter salary:"))
query="update dbemployee2 set salary=%s where id=%s"
cursor.execute(query,(salary,id))
conn.commit()
print("success")

conn.close()
