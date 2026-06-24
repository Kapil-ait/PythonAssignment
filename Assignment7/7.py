a=int(input("enter total balance:"))
if a<1000:
   print("withdrawal not allowed")
elif a>1000 and a<5000:
     print(" maximum withdrawal 1000")
elif a>5000:
     print("maximum withdrawal 5000")  