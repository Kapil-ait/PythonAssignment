a = int(input("Enter a number: "))
temp=a
i=1
sum=0
while i<=a//2:
      if a%i==0:        
         sum=sum+i
      i+=1 
print("the sum is:",sum)
if sum==temp:
   print("reward unlocked")
else:
    print("try again")



