a=int(input("enter demand:"))
b=int(input("enter stock:"))
c=input("enter user type(premium/not):")
d=input("enter festival(yes/no):")
if a>=80:
   if b<50 and c=="premium" and d=="yes":
      print("give 20% discount")
   else:
       print("give 10% discount")
elif a>=40:
     if a<=79 and d=="yes":
        print("give 10% discount")
     else:
         print("no discount")
elif a<40:
     if b>200:
        print("give 15% discount")
     else:
         print("no discount")
