a=input("enter class(economy/business):")
b=int(input("enter distance:"))
c=input("enter booking(early/not):")
if a=="business":
   if b>1000:
      print("price is 8000")
   else:
       print("5000")
elif a=="economy":
     if b>1000 and c=="early":
        print("price is 4000")
     else:
         print("5000")
     if b<=1000:
        print("price is 2500")