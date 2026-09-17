"""Assignment 2: Employee Salary Calculator
A company wants to calculate an employee's gross salary.
Create a class Employee with the following attributes:
Employee ID
Employee name
Basic salary
HRA percentage
DA percentage
Create the following methods:
calculate_hra() – Calculate HRA.
calculate_da() – Calculate DA.
calculate_gross_salary() – Calculate gross salary.
display_salary() – Display employee salary details.
Formula:
HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA"""

class Employee:
    def __init__(self, emp_id, emp_name, basic_salary, hra_percentage, da_percentage):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.hra_percentage = hra_percentage
        self.da_percentage = da_percentage

    def calculate_hra(self):
        return (self.basic_salary * self.hra_percentage) / 100

    def calculate_da(self):
        return (self.basic_salary * self.da_percentage) / 100

    def calculate_gross_salary(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        return self.basic_salary + hra + da

    def display_salary(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        gross_salary = self.calculate_gross_salary()
        
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"HRA: {hra}")
        print(f"DA: {da}")
        print(f"Gross Salary: {gross_salary}")
emp=Employee(101, "John Doe", 50000, 20, 10)
emp.display_salary()
emp2=Employee(102, "Jane Smith", 60000, 25, 15)
emp2.display_salary()
