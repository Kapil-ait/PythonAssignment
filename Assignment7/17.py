a=int(input("enter marks of student:"))
b=int(input("enter entrance score:"))
c=input("enter category(ST,SC/OBC/general):")
if a>=70 and b>=80 and c=="general":
   print("Admit")

elif b<80 and a>=85:
     print("Admit under management quota")

elif a<70 and category=="OBC" and a>=60 and b>=70:
   print("waitlist")

elif a<70 and category=="ST,SC" and a>=60 and b>=70:
   print("waitlist")
else:
     print("Reject")

   
 