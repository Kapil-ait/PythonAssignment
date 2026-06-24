a=int(input("enter performance rating 1-5:"))
b=int(input("enter salary:"))
if a==1:
   print(b)
elif a==2:
     sal=b*5/100
     final=b+sal
     print(final)
elif a==3:
     sal=b*10/100
     final=b+sal
     print(final)
elif a==4:
     sal=b*20/100
     final=b+sal
     print(final)
elif a==5:
     sal=b*25/100
     final=b+sal
     print(final)
if b<20000 and a>=4:
   final=final+2000
   print("final amount is :",final)
