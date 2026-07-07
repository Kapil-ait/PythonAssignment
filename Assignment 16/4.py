a=int(input("enter number:"))
sum=0
pro=1
while a>0:
      digit=a%10
      sum=sum+digit
      pro=pro*digit
      a=a//10
if sum==pro:
   print("spy number")

else:
    print("not spy")