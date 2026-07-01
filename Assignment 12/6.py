"""6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2"""

n=int(input("enter the number:"))
count=0
small=n//2
if n<=1:
    print("not composite")
    print("factor count is: ",n )
    print("smallest factor is: ",n)
else:
    i=2
    while i<=n//2:
          if n%i==0:
             count=count+1
             if i<=small:
                small=i
          i=i+1
if count>=2:
   print("composite number") 
   print("factor count is: ",count+2 )
   print("smallest factor is: ",small)
      