"""
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
"""
import math
n=int(input("Enter number :"))
temp=n
while True:
      n+=1
      i=2
      while i<math.sqrt(n):
         if n%i==0:
            break
         i+=1
      else:
         print("next number is :",n)
         break
print("difference is:",n-temp)
      
   