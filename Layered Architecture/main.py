from service.employeeservice import EmployeeService
from model.Employee import Employee

print("welcome")

employee = Employee(1011, "raju", 40000)
service = EmployeeService()
service.addemployee(employee)
