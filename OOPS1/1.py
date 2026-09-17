"""Assignment 1: Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%"""


class student:
    def details(self,rollno,marks1,marks2,marks3):
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3
    def calculate_percentage(self):
        total = self.calculate_total()
        return (total / 300) * 100
s1=student()
s1.details(101, 80, 80, 80)
print("Student Name: Ajay")
print("Roll Number:", s1.rollno)
print("Total Marks:", s1.calculate_total())
print("Percentage:", s1.calculate_percentage(), "%")
