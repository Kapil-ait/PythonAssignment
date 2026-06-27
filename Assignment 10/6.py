a=int(input("enter experience:"))
b=int(input("enter rating:"))
c=int(input("enter projects:"))
d=int(input("enter salary:"))
if a>=5:
   if b>=4 and c>=3 and d<=50000:
      e=d*30/100
      d=d+e
      print(d)
   else:
       f=d*20/100
       d=d+f
       print(f)
elif c<3:
     g=d*10/100
     d=d+g
     print(g)
elif b<4:
     print("no promotion")
elif a<5: 
     if b==5:
        print("fast track promotion")
     else:
         print("no promotion")
     