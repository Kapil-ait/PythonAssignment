a=int(input("enter salary:"))
b=int(input("enter age:"))
c=int(input("enter credit score:"))
d=int(input("enter EMI:"))
d=a*40/100
if a>=40000:
   if a>21 and a<60 and c>=750 and e<=d:
      print("approve at 8%")
   else:
       print("approve at 10%")
   if c<750 and c>=650:
      print("approve at 12%")
   else:
       print("reject")
elif a<40000:
     if a>=25000 and c>=700:
        print("approve at 13%")
     else:
         print("reject")