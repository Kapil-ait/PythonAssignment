"""Console UI for the Employee Payroll Management System."""

from decimal import Decimal

from mysql.connector import Error

from service.employee_service import EmployeeService


def print_employee_table(employees):
    print("Employee ID | Name | Department | Salary | Experience")
    print("-" * 58)
    for emp_id, name, department, salary, experience in employees:
        print(f"{emp_id:<11} | {name:<4} | {department:<10} | {salary:.2f} | {experience}")


def print_employee_details(employees):
    for emp_id, name, department, salary, experience in employees:
        print(f"Employee ID: {emp_id}")
        print(f"Employee Name: {name}")
        print(f"Department: {department}")
        print(f"Salary: {salary:.2f}")
        print(f"Experience: {experience} Years")
        print()


def run():
    service = EmployeeService()
    while True:
        print("\n========== EMPLOYEE PAYROLL MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Display All Employees")
        print("4. Department-wise Employee Report")
        print("5. Salary Increment")
        print("6. Display Highest Paid Employee")
        print("7. Display Employees Above Average Salary")
        print("8. Exit")
        print("========================================================")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                employee = (
                    int(input("Enter Employee ID: ")),
                    input("Enter Employee Name: "),
                    input("Enter Department: "),
                    Decimal(input("Enter Salary: ")),
                    int(input("Enter Experience: ")),
                )
                _, message = service.add_employee(*employee)
                print(message)
            elif choice == "2":
                updated, message = service.update_employee(
                    int(input("Enter Employee ID: ")), input("Enter New Employee Name: "), Decimal(input("Enter New Salary: "))
                )
                print(message)
            elif choice == "3":
                print_employee_table(service.all_employees())
            elif choice == "4":
                department = input("Enter Department Name: ")
                employees, count, average = service.department_report(department)
                if not employees:
                    print("No employees found in this department!")
                else:
                    print(f"\nEmployees in {department} Department")
                    print_employee_table(employees)
                    print(f"Total Employees: {count}")
                    print(f"Average Salary: {average:.2f}")
            elif choice == "5":
                department = input("Enter Department Name: ")
                percentage = Decimal(input("Enter Increment Percentage: "))
                updated = service.increment_salary(department, percentage)
                if updated:
                    print("Salary increment applied successfully!")
                    print(f"Number of employees updated: {updated}")
                else:
                    print("No employees found in this department!")
            elif choice == "6":
                employees = service.highest_paid()
                if employees:
                    print("\nHighest Paid Employee Details\n--------------------------------")
                    print_employee_details(employees)
                else:
                    print("No employees found!")
            elif choice == "7":
                employees = service.above_average_salary()
                if employees:
                    print("\nEmployees Having Salary Above Average\n--------------------------------------")
                    print_employee_details(employees)
                else:
                    print("No employees have a salary above average!")
            elif choice == "8":
                print("Thank you for using Employee Payroll Management System!")
                break
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, Error) as error:
            print(f"Operation failed: {error}")


if __name__ == "__main__":
    run()
