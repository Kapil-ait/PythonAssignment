a=int(input("enter age:"))
b=int(input("enter BMI:"))
c=int(input("enter running time:"))
d=input("enter medical(fit/not):")
if a>=18 and a<=25:
   if b<=18 and b>=25 and c<=15  and d=="fit":
      print("select")
   else:
       print("reject")
   if c>15:
      print("physical fail")
   if b>b:
      print("BMI fail")
elif a>=26 and a<=30:
     if c<=14 and d=="fit":
        print("selection")
     else:
         print("reject")
elif a>30 and a<18:
     print("not eligible")