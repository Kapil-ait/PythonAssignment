a=int(input("enter marks:"))
b=int(input("enter income:"))
c=input("enter category(OBC/general/STSC):")
if a>=85:
   if b<=300000 and c!="general":
      print("full scholarship")
   else:
       print("give 75% scholarship")
   if b>300000:
      print("give 50% scholarship")
elif a>=70 and a<=84:
     if b<=2000000:
        print("give 50% scholarship ")
     else:
         print("give 25% scholarship")
elif a<70:   
     print("no scholarship is given")

