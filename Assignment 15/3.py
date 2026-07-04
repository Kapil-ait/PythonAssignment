a=int(input("enter started year:"))
b=int(input("enter last year:"))
for i in range(a,b+1):
    if i%4==0:
       print("leap year is:",i)
       