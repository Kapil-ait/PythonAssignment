a=int(input("enter marks:"))
b=int(input("enter backlogs:"))
c=int(input("enter project:"))
if a>=75:
   if b==0 and c>=80:
      print("First class with distinction")
   else:
       print("first class")
   if b>0:
      print("first class")
elif a>=60 and a<=74:
     if b<=2:
        print("second class")
     else:
         print("pass class")
elif a>=50:
     if a<=59:
        print("pass")
     else:
         print("fail")