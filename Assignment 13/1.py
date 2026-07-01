n=int(input("enter the number:"))
temp=n
sum=0
rev=0
while n>0:              
      digit=n%10
      rev=rev*10+digit
      sum=sum+digit  
      n=n//10
print("Reverse :",rev)
print("the sum is:",sum)
diff=rev-temp
print("the difference is:",diff)
final=sum+diff
print("final=",final)
while final>=1:
      if final%2==0:
         print("not prime number")
         break
      final=final+1
else:
     print("prime number")