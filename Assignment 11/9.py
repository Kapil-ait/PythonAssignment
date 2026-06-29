"""9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number"""

"""n=int(input("enter the numbers:"))
sum=0
rev=0
while n>0:
      digit=n%10
      print(digit,end=" ")
      sum=sum+digit
      n=n//10
print(sum)"""

n = int(input("Enter the number: "))
temp = n
rev = 0

# Reverse the number
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

prev = rev % 10
rev = rev // 10

sum = 0
largest = 0
count = 1

print("Step Differences:", end=" ")

while rev > 0:
    digit = rev % 10

    if prev > digit:
        diff = prev - digit
    else:
        diff = digit - prev

    print(diff, end=" ")

    sum = sum + diff

    if diff > largest:
        largest = diff

    prev = digit
    rev = rev // 10
    count = count + 1

print("\nSum =", sum)
print("Largest =", largest)

if sum % count == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")
      
