import mysql.connector

print("Started")

conn=mysql.connector.connect(
    
       host="localhost",port=3306,user="root",password="Pratik@2006",database="batch19"
)

cursor = conn.cursor()

# Create Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_pdbc (
    sid INT PRIMARY KEY,
    sname VARCHAR(50),
    course VARCHAR(50),
    fees DECIMAL(10,2),
    city VARCHAR(30)
)
""")


while True:
   print("""===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit""")
   choice=int(input("Enter your choice :")) 
   match(choice):
     case 1:   
               query="insert into student_pdbc(sid,sname,course,fees,city)values(%s,%s,%s,%s,%s)"
               n=int(input("enter no of rows :"))

               data=[]

               for i in range(n):
                  sid=int(input("enter ID :"))
                  sname=input("enter name :")
                  course=input("enter course :")
                  fees=float(input("enter fees :"))
                  city=input("enter city :")
                  data.append((sid,sname,course,fees,city))
       
               
               cursor.executemany(query,data)
               print("Inserted succesfully")
               conn.commit()
               
     case 2:
            
            cursor.execute("select * from student_pdbc")
            result=cursor.fetchall()
            
            print("\nID\tName\tCourse\tFees\tCity")
            print("---------------------------------------------")
            for row in result:
                   print(row[0], row[1], row[2], row[3] ,  row[4] ,sep="\t")
          
     case 3:
           search_name = input("Enter name to search: ")

           query = "SELECT * FROM student_pdbc WHERE sname LIKE %s"

           cursor.execute(query, ('%' + search_name + '%',))
           result = cursor.fetchall()

           if result:
              print("\nMatching students:")
              for row in result:
                print(row)
           else:
               print("\no result find")     
               
     case 4:
           sid = int(input("Enter Student ID: "))
           fees = float(input("Enter New Fees: "))

           query = "UPDATE student_pdbc SET fees=%s WHERE sid=%s"

           cursor.execute(query, (fees, sid))
           conn.commit()
           
     case 5:
           sid = int(input("Enter Student ID: "))

           query = "DELETE FROM student_pdbc WHERE sid=%s"

           cursor.execute(query, (sid,))
           conn.commit()       
      
     case 6:
           print("Thanku for using this system ")           
           break               
conn.close()
cursor.close()       import mysql.connector

print("Started")

conn=mysql.connector.connect(
    
       host="localhost",port=3306,user="root",password="Pratik@2006",database="batch19"
)

cursor = conn.cursor()

# Create Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_pdbc (
    sid INT PRIMARY KEY,
    sname VARCHAR(50),
    course VARCHAR(50),
    fees DECIMAL(10,2),
    city VARCHAR(30)
)
""")


while True:
   print("""===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit""")
   choice=int(input("Enter your choice :")) 
   match(choice):
     case 1:   
               query="insert into student_pdbc(sid,sname,course,fees,city)values(%s,%s,%s,%s,%s)"
               n=int(input("enter no of rows :"))

               data=[]

               for i in range(n):
                  sid=int(input("enter ID :"))
                  sname=input("enter name :")
                  course=input("enter course :")
                  fees=float(input("enter fees :"))
                  city=input("enter city :")
                  data.append((sid,sname,course,fees,city))
       
               
               cursor.executemany(query,data)
               print("Inserted succesfully")
               conn.commit()
               
     case 2:
            
            cursor.execute("select * from student_pdbc")
            result=cursor.fetchall()
            
            print("\nID\tName\tCourse\tFees\tCity")
            print("---------------------------------------------")
            for row in result:
                   print(row[0], row[1], row[2], row[3] ,  row[4] ,sep="\t")
          
     case 3:
           search_name = input("Enter name to search: ")

           query = "SELECT * FROM student_pdbc WHERE sname LIKE %s"

           cursor.execute(query, ('%' + search_name + '%',))
           result = cursor.fetchall()

           if result:
              print("\nMatching students:")
              for row in result:
                print(row)
           else:
               print("\no result find")     
               
     case 4:
           sid = int(input("Enter Student ID: "))
           fees = float(input("Enter New Fees: "))

           query = "UPDATE student_pdbc SET fees=%s WHERE sid=%s"

           cursor.execute(query, (fees, sid))
           conn.commit()
           
     case 5:
           sid = int(input("Enter Student ID: "))

           query = "DELETE FROM student_pdbc WHERE sid=%s"

           cursor.execute(query, (sid,))
           conn.commit()       
      
     case 6:
           print("Thanku for using this system ")           
           break               
conn.close()
cursor.close()       