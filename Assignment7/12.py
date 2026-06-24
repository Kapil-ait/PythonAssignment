a=int(input("enter total bill amount:"))
if a<=1000:
   gst=a*10/100
   final=a+gst
   print("final bill amount:",final)
elif a>1001 and a<=5000:
     gst=a*12/100
     final=a+gst
     print("Fina; bill amount:",final)
elif a>5000:
     gst=a*18/100
     final=a+gst
     print("final bill amount:",final)
if a>3000:
   total=final+200
   print("total final bill:",total)