a=int(input("enter total cart value:"))
if a>5000:
   dis=a *20/100
   final=a-dis
   print("price is:",final)
elif a>2000:
     dis=a*10/100
     final=a-dis
     print("price is:",final)
elif a<2000:
     dis=a*5/100
     final=a-dis
     print("price is:",final)