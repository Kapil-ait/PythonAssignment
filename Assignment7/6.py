a=int(input("enter salary:"))
b=int(input("enter years of experience:"))
if b>10:
   sal=a*20/100
   print("salary is:",sal)
elif b>5:
     sal=a*10/100
     print("salary is:",sal)
elif b>2:
     sal=a*5/100
     print("salary is:",sal)
elif b<2:
     sal=a
     print("salary is:",sal)