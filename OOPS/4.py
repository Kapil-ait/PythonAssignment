"""Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B"""

class student:
    def __init__(self, roll_number, student_name, marks1, marks2, marks3):
        self.roll_number = roll_number
        self.student_name = student_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3

    def calculate_percentage(self):
        return self.calculate_total() / 3

    def determine_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"
st=student(input("Enter Roll Number : "), input("Enter Student Name : "), int(input("Enter Marks in Subject 1 : ")), int(input("Enter Marks in Subject 2 : ")), int(input("Enter Marks in Subject 3 : ")))
print("------ Student Result ------")
print("Roll Number      :", st.roll_number)
print("Student Name     :", st.student_name)
print("Total Marks      :", st.calculate_total())
print("Percentage       :", round(st.calculate_percentage(), 2))
print("Grade            :", st.determine_grade())
