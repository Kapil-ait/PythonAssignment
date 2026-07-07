a=int(input("enter the number:"))
temp=a
rev=0
rev1=0
sq=a*a
while a>0:
      digit=a%10
      rev=rev*10+digit
      a=a//10
      digit1=sq%10
      rev1=rev1*10+digit
print(sq)
print(rev)
sq1=rev*rev
print(sq1)
rev2=0
a=temp
while sq1>0:
      digit=sq1%10
      rev2=rev2*10+digit
      sq1=sq1//10
print(rev2)
if sq==rev2:
   print("Adam Number")
else:
    print("Not a Adam Number")

       