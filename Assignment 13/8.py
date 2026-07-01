"""8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.
Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700
Output:

Notes = 7
"""
a=int(input("enter the withdraw amount:"))
count=0
while a>=100:   
      count=count+1
      a=a-100
print("total 100 RS notes will be:",count)
    
     
         
