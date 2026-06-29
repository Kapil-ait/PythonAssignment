a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
count=0
for i in range(a,b+1):
      if i%7==0:
         count=count+1
         print(i)
print("the total nu which is divide by 7 is:",count)
      
