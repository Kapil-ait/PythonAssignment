a=int(input("enter the stock:"))
b=input("enter priority(high/low):")
c=int(input("enter distance"))
if a>=100:
   if b=="high" and c<=200:
      print("dispatch immediately")
   else:
       print("dispatch via fast courier")
elif b=="low":
     if a>=300:
        print("bulk dispatch")
     else: 
         print("normal dispatch")
elif a<100:
     if a>=50 and b=="high":
        print("partially dispatch")
     else:
         print("hold")
elif a<50:
     print("out of stock")