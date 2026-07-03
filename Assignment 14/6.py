a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

for n in range(a,b+1):   
    temp=n 
    count=0
    while temp>0:
          digit=temp%10
          count=count*10+digit
          temp=temp//10
    if count==n:
       print(n)

    