a=int(input("enter policy age:"))
b=int(input("enter claim amount:"))
c=input("enter accident type(major/minor):")
if a>=2 :
   if b<=50000 and c=="minor":
      print("approve the claim")
   else:
        print("approve with an inspection")
elif a>=50001 and  a<=200000:
     if c=="major":
        print("approve with investigation")
     else:
          print("Rejcet")
elif a>200000:
     print("Reject")
elif a<2 :
     if c=="minor":
        print("Reject")
     else:
          print("mark as pending review")
