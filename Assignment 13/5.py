"""5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number"""

a=int(input("enter the number:"))
max=9
while a:
      digit=a%10
      print(digit)
      if digit<max:    
         max=digit
      else:
         print("Not stable number")
         break
      a=a+1
      a=a//10
else:
    print("stable")