"""8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4"""

a=int(input("enter the number:"))
b=int(input("enter the number:"))
count=0
if a<=b:
   while a<=b:
         if a%5==0:
            print(a)
            count=count+1
         a+=1
else:
     while a >= b:
        if a % 5 == 0:
           count=count+1
           print(a)
        a -= 1
print("the count of the dov 5 is:",count)

