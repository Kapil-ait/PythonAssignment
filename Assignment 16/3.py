n=int(input("enter n:"))
a=0
b=1
sum=0
count=0
for i in range(0,n):
    sum=sum+a
    print(a,end=" ")
    if a>5:
       count+=1
    c=a+b
    a=b
    b=c   
print()
print("sum is:",sum)
print("months with population >5 is:",count)
    
    
      