"""a=int(input("enter income:"))
b=int(input("enter credit score:"))
c=input("enter employment(private/government):")
d=int(input("enter debt:"))
if a>=50000:
   if b>=750 and d<=20000:
      print("approve premium card")
   else:
       print("approve gold card")
elif b<750:
     if c=="government" and b>650:
        print("approve gold card")
     else:
         print("reject")
elif a<50000:
     if a>=30000 and b>=700:
        print("approve silver")
else:
    print("reject")"""

a = int(input("Enter income: "))
b = int(input("Enter credit score: "))
c = input("Enter employment (private/government): ")
d = int(input("Enter debt: "))

if a >= 50000:
    if b >= 750 and d <= 20000:
        print("Approve Premium Card")
    else:
        print("Approve Gold Card")

elif a >= 30000:
    if b >= 700:
        print("Approve Silver Card")
    elif c == "government" and b > 650:
        print("Approve Gold Card")
    else:
        print("Reject")

else:
    print("Reject")