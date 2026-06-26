"""2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2"""

n=int(input("enter the number:"))
max=n
while n>0:
      d=n%10
      if d<=max:
         max=d
      n=n//10
      
print("smallest number is:",max)