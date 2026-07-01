"""7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime"""

a=int(input("enter the number:"))
sum=0
while a>0:
      digit=a%10
      sum=sum+digit
      a=a//100
print("the sum is:",sum)
if sum%2==0:
    print("prime number")
else:
    print("Not prime number")
