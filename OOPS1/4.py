"""Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8"""

class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

    def display_result(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f"Length: {self.length}")
        print(f"Breadth: {self.breadth}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

r=rectangle(15, 8)
r.display_result()  