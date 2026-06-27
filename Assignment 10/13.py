a=int(input("enter amount:"))
b=input("enter location(domestic/international):")
c=input("device(new/not new):")
d=int(input("enter transaction count:"))
e=input("enter unusual activity(yes/no):")
if a>=50000:
   if b=="international" and c=="new" and d>3:
      print("high risk block")
   else:
       print("medium risk")
   if c!="new":
      print("medium risk")
elif a<50000:
     if e=="yes" and c=="new":
        print("medium risk")
     else:
         print("low risk")
     if e=="no":
        print("safe")