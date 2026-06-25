"""14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor"""


"""a,b=map(int,input("enter the numbers:").split(" "))
if a<b:
   for i in range(a,b+1):
       print(i,end=" ")
elif a>b:
     for i in range(a,b-1,-1):
         print(i,end=" ")
else:
     print("both are on the same floor")"""


"""WHILE"""
a,b=map(int,input("enter the numbers:").split(" "))
if a<b:  
   while a<b:
         print(a,end=" ")
         a+=1
elif a>b:
     while a>b:
           print(a,end=" ")
           a-=1
else:
     print("both are on the same floor")

     
