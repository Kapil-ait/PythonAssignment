import mysql.connector

print("Started")

conn=mysql.connector.connect(
    
       host="localhost",port=3306,user="root",password="Pratik@2006",database="batch19"
)

cursor = conn.cursor()

# Create Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_pdbc (
    eid INT PRIMARY KEY,
ename VARCHAR(50),
department VARCHAR(40),
salary DECIMAL(10,2),
city VARCHAR(30)
)
""")

while True:
     print()
     print("""===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit""")
     
     choice=int(input("enter your choice :"))
     match(choice):
           case 1:
                 query="insert into employee_pdbc(eid,ename,department,salary,city)values(%s,%s,%s,%s,%s)"
                 n=int(input("enter number of records :")) 
                 data=[]
                 for i in range(n):
                     eid=int(input("enter employee id :"))
                     ename=input("enter employee name :")
                     department=input("enter department :")
                     salary=float(input("enter salary :"))
                     city=input("enter city :")
                     data.append((eid,ename,department,salary,city))
                 
                 cursor.executemany(query,data)
                 print("Inserted succesfully....")
                 conn.commit() 
                 
           case 2:
                cursor.execute("select * from employee_pdbc")
                result=cursor.fetchall()               
                print("\nID\tName\tdepartment\tSalary \t City")
                print("---------------------------------------------")
                for row in result:
                    print(row[0], row[1], row[2], row[3] ,  row[4] ,sep="\t")    
                    
                    
           case 3:
                search_name = input("Enter name to search: ")
                
                query = "SELECT * FROM employee_pdbc WHERE ename LIKE %s"
                
                cursor.execute(query, ('%' + search_name + '%',))
                result = cursor.fetchall()
                
                if result:
                    print("\nMatching students:")
                    for row in result:
                       print(row)
                else:
                    print("\no result find")    
           
           case 4:
               
                 eid = int(input("Enter employee ID: "))
                 salary = float(input("Enter New salary: "))
                 
                 query = "UPDATE employee_pdbc SET salary=%s WHERE eid=%s"
                 
                 cursor.execute(query, (salary, eid))
                 conn.commit()      
                 
           case 5:
                eid = int(input("Enter employee ID: "))
                query="delete from employee_pdbc where eid=%s"      
                
                cursor.execute(query,(eid,)) 
                conn.commit()
                print("Delelted Succesfully..........")
                
           case 6:
                 print("Thankyou for using this system ")
                 break     
                                  
