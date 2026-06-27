a=int(input("enter marks:"))
b=int(input("enter attendance:"))
c=int(input("enter internal:"))
if a>=40:
   if a>=75 and c>=20:
      print("pass")
   else:
       print("grace pass")
elif a<40:
     if a>=35 and c>=25:
        print("reappear")
else:
    print("fail")