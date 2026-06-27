a=int(input("enter the demand:"))
b=input("enter time(peak/not):")
c=int(input("enter the distance:"))
if a>=80:
   if b=="peak" and c>=10:
      print("2x fair")
   else: 
       print("1.5x")
elif b=="not":
     if a>=90 :
        print("1.8x")
     else:
         print("1.3x")
elif a<80:
     if a>=50 and b=="peak":
        print("1.2x")
     else:
         print("normal fair")
elif a<50:
     print("normal fair")