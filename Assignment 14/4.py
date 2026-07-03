a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
for i in range(a,b+1):
    temp=i
    c=len(str(i))
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**c
        temp=temp//10
    if sum==i:       
       print(i)