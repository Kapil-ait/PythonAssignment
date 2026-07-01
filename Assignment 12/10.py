"""10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime"""


n=int(input("enter the number:"))
count=0
sum=0
max=9
while n>0:
      digit=n%10
      n=n//10  
      sum=sum+digit
      if digit==0:
         count=count+1
      if digit<=max:
         max=digit

print("zero count is :",count)
print("the sum is:",sum)
print("smallest digit is:",max)
final=(sum+count)*max
print("final result is:",final)
while True:
      if final%2==0:
         print("not prime")
         break
else:
    print("prime")




      