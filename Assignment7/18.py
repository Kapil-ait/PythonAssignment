a=int(input("enter salary:"))
b=int(input("enter credit score:"))
c=int(input("enter existing loan:"))
if a>=40000 and b>=750 and c==0:
   print("low risk")
elif a>=40000 and b>=750 and c<=2:
     print("mid risk")
elif a>=40000 and b>=750 and c>2:
     print("high risk")
elif a>=50000 and b>=650 :
     print("mid risk")
elif a<30000:
     print("not eligible")
else: 
     print("Reject")
       
