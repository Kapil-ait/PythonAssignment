a,b=map(int,input("enter numbers").split(" "))
i=a
while i<=b:
      if i%2==0:
         print(i,end=" ")
      i+=1


"""for"""
a,b=map(int,input("enter numbers").split(" "))

for i in range(a,b,1):
    if i%2==0:
         print(i,end=" ")
     
