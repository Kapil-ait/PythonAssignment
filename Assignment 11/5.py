a=int(input("enter a number:"))
temp=a
while a>1:
      digit=a%10
      print(digit)
      a=a//10

print(a)
print("the sum is:",digit+a)

if temp%(digit+a)==0:
   print("Harshad number")
else:
    print("not Harshad number")
   
