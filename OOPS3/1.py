"""============================================================
ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
=========================================

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:

Enter Programming Language:

If Manager:

Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.
"""

class employee:
    def __init__(self, employee_id,employee_name,__salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=__salary
    def display_details(self):
        print(self.employee_id,self.employee_name,self.__salary)
    def user(self):
        n=int(input("enter the number of user:"))
        for i in range(n):
            empid= int(input("Enter Roll No: "))
            empname = input("Enter Name: ")
            sal = float(input("Enter Marks: "))
            s = employee(empid,empname,sal)
            employee.append(s)

    @property
    def employee_id(self):
        return self.employee_id
    @salary.setter
    def salary(self,value):
        if value<0:
          print("enter sal greater than 0")
        else:
          return self.__salary
    @salary.deleter
    def salary(self):
        del self.__salary
    
       

class Developer(employee):
    def programming_language(self):
        pass
    

    def write_code():
        pass


class manager(employee):
   def team_size():
       



    def manage_team():
        pass
        