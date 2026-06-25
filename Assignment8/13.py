"""a,b=map(int,input("enter numbers").split(" "))
if a<b:
   for i in range (a,b+1):
       print(i,end=" ")
elif a>b:
     for i in range(a,b-1,-1):
         print(i,end=" ")
else:
     print("both are same")"""

"""while"""
a,b=map(int,input("enter numbers").split(" "))
if a<b:
   while a<b:
         print(a,end=" ")
         a+=1
elif a>b:
   while a>b:
         print(a,end=" ")  
         a-=1
else:
     print("both are same")
