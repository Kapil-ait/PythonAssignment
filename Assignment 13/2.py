n=int(input("enter the number:"))
sum=0
pro=1
while n>0:              
      digit=n%10
      sum=sum+digit 
      pro=pro*digit 
      n=n//10
print("the sum is:",sum)
print("the product is:",pro)
diff=pro-sum
print("difference is:",diff)
temp=diff
count=0
while diff>0: 
      digit=diff%10
      count=count+1
      diff=diff//10
print("the count of difference is:",count)
final=temp+count
print("final result:",final)
if final<=1:
   print("Not prime number")
else:
  i=2
  while i<final//2:
      if final%i==0:
         print("Not prime number")
         break
      i+=1
  else:
     print("prime number")
      
      
