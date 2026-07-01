n=int(input("enter number:"))
sum=0
while n>0:
     digit=n%10
     print(digit)
     sum=sum+digit
     n=n//10
print(sum)
while sum>0:
      if sum%2==0:
         print("lucky number")
         break
      sum=sum+1
else:
     print("not lucky number")