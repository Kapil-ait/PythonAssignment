"""4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31"""

import math
n=int(input("enter the number:"))
while True:
      n+=1
      i=2
      while i<=math.sqrt(n):
            if  n%i==0:
                break
            i+=1
      else:
          print("next prime nu is:",n)
          break