a=int(input("enter number:"))
b=a*a
for i in range(1,a+1):
      digit=a%10
      digit1=b%10
if digit==digit1:
   print("automorphic")
else:   
    print("not automorphic")