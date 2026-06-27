a=int(input("enter the soil moisture:"))
b=int(input("enter temperature:"))
c=input("enter crop(wheat):")
r=input("check rainfall(expected/not)")
if a<=30:
   if b>=35 and c=="wheat":
      print("high water supply")
   else:
       print("moderate supply")
elif b<35:
     print("moderate supply")
elif a>30 :
     if a<=60 and r=="expected":
        print("delay irrigation")
     else:
         print("light irrigation")
else: 
     print("no irrigation")
     
