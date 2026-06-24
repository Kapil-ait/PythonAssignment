a=int(input("enter stock:"))
b=input("enter priority(high/low):")
c=int(input("enter distance"))
if a>=100:
   if b=="high" and c<=200:
      print("dispatch immediately")
   else:
        print("dispatch via fast courier")
elif b!="high":
     if a>=300:
        print("Bulk dispatch")
     else:
          print("Normal dispatch")
elif a<100:
     if a>=50:
        if priority=="high" :
           print("partially dispatch")
     else:
           print("partially dispatch")
elif a<50:
     print("mark out of the stock")

