"""Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0"""

class employee:
    def __init__(self, employee_id, employee_name, basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary
    def hra(self):
        return self.basic_salary * 0.20
    def da(self):
        return self.basic_salary * 0.15
    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()
    def display_salary_details(self):
        print("------ Employee Salary Details ------")
        print(f"Employee ID      : {self.employee_id}")
        print(f"Employee Name    : {self.employee_name}")
        print(f"Basic Salary     : {self.basic_salary}")
        print(f"HRA              : {self.hra()}")
        print(f"DA               : {self.da()}")
        print(f"Gross Salary     : {self.gross_salary()}")
emp=employee(input("Enter Employee ID : "), input("Enter Employee Name : "), float(input("Enter Basic Salary : ")))
emp.display_salary_details()
