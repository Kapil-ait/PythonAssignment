n=int(input("enter the number:"))
max=0
while n>0:
      d=n%10
      if d>=max:
         max=d
      n=n//10
      
print("greatest number is:",max)