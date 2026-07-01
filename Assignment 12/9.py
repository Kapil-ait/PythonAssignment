"""9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime"""


n=int(input("enter the number:"))
count=0
count1=0
i=2
while n>=1:
      digit=n%10
      print(digit)
      if digit%i==0:
         count=count+1
      if digit%i!=0:
         count1=count1+1      
      n=n//10
print("the even count is:",count)
print("the even count is:",count1)
print("difference is:",count-count1)
"""15"""
diff=count-count1
i=2
while True:
      if diff%i==0:
         print("not prime")
         break
else:
    print("prime")




   
    
