a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
for i in range(a,b+1):
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
           sum+=j
    if sum==i:
       print(i)  
    