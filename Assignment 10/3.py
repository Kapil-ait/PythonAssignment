a=int(input("enter the transaction amount:"))
b=input("enter location(domestic/international):")
c=int(input("enter account age:"))
d=input("enter OTP verification(verified/not):")
e=input("enter unusual activity(yes/no):")
if a>=10000:
   if b=="international" and d=="verified":
      print("allow")
   else:
       print("block")
elif b=="domestic":
     if a>=50000 and c>=2:
        print("allow")
     else:
         print("flag")
elif a<50000:
     print("allow")
elif a<10000 and e=="yes":
     print("yes")
else:
    print("allow")
