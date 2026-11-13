import mysql.connector
print("started")
try:
   conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
   if conn.is_connected():
          print("CONNECTED DB SUCCESFULLY")
except Exception as e:
     print("connection issue")
finally:
     print("connection closed")
print("done with code")
cursor=conn.cursor()
cursor.execute("insert into dbemployee2 values(1,'deepika',90000)")
conn.commit()
print("success")
cursor.close()
conn.close()
