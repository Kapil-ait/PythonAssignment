a=int(input("enter number:"))
fact=1
i=1
for i in range(1,a//2+1):
      if a%i==0:
         fact=i+fact
      i=i+1
if fact>a:
   print("Abunded Number")
else:
    print("Not Abunded Number")
      