"""8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime"""
 

n=int(input("enter the number:"))
max=0
min=n
while n>=1:
      digit=n%10
      print(digit)
      if digit>max:
         max=digit
      if digit<min:
         min=digit
      n=n//10
print("max number is:",max)
print("min is:",min)
           
      