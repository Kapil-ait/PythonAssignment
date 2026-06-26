"""7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32"""

a=int(input("enter the numbers:"))
b=int(input("enter the power:"))
out=1
while b:
      out=out*a
      b-=1
print(out)
