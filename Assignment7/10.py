a=float(input("enter daily limit:"))
if a>3:
   print("premium Plan")
elif a<3 and a>1:
     print("Standard Plan")
elif a<1:
     print("Basic Plan")