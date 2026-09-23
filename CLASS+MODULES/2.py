"""============================================================
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM
=========================================

Create an Employee class inside:

models/employee.py

ATTRIBUTES:

* employee_id
* name
* salary
* department

TASKS:

1. Take details of 5 employees from the user.
2. Create Employee objects.
3. Store the objects inside a list.
4. Display all employees.
5. Display employees whose salary is greater than 40,000.
6. Display employees who belong to the IT department.
7. Find the employee having the highest salary.
8. Calculate total salary of all employees.
9. Calculate average salary.

SAMPLE INPUT:

101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

EXPECTED OUTPUT:

All Employees:
101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

Employees with salary greater than 40000:
101 Amit 45000 IT
103 Priya 60000 IT
104 Neha 50000 Finance

Employees from IT Department:
101 Amit 45000 IT
103 Priya 60000 IT

Highest Salary Employee:
103 Priya 60000 IT

Total Salary:
220000

Average Salary:
44000
"""
class employee:
    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department
    def employee(self):
        n=int(input("enter number of employees:"))
        for i in range(n):
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Employee Salary: "))
            department = input("Enter Employee Department: ")
            e = employee(employee_id, name, salary, department)
            employee.append(e)
    def display_all_employees(self):
        print("All Employees:")
        for e in employee:
            print(f"{e.employee_id} {e.name} {e.salary} {e.department}")
    def display_employees_with_salary_greater_than_40000(self):
        print("Employees with salary greater than 40000:")
        for e in employee:
            if e.salary > 40000:
                print(f"{e.employee_id} {e.name} {e.salary} {e.department}")
    def display_employees_from_it_department(self):
        print("Employees from IT Department:")
        for e in employee:
            if e.department.lower() == "it":
                print(f"{e.employee_id} {e.name} {e.salary} {e.department}")    
    def highest_salary_employee(self):
        highest_salary = max(employee, key=lambda e: e.salary)
        print("Highest Salary Employee:")
        print(f"{highest_salary.employee_id} {highest_salary.name} {highest_salary.salary} {highest_salary.department}")
    def total_salary(self):
        total = sum(e.salary for e in employee)
        print("Total Salary:")
        print(total)
    def average_salary(self):
        average = sum(e.salary for e in employee) / len(employee)
        print("Average Salary:")
        print(average)
emp=employee(101, "Amit", 45000, "IT")
employee=[]
emp.employee()
emp.display_all_employees()
emp.display_employees_with_salary_greater_than_40000()
emp.employee.display_employees_from_it_department()
emp.highest_salary_employee()
emp.employee.total_salary()
emp.employee.average_salary()
