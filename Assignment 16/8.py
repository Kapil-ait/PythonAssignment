a=int(input("enter number:"))
cu=a*a*a
digit=a%10
digit1=cu%10
if digit==digit1:
   print("Trimorphic Number")
else:
    print("Not Trimorphic Number")