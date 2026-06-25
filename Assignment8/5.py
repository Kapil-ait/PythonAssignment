a=int(input("enter the number:"))
temp=a
count=0
while a>0:
      count=count*10+a%10
      a=a//10
if count==temp:
   print("palindrome")
else:
     print("not palindrome")

"""for"""
a=int(input("enter the number:"))
temp=a
count=0
i=0
for i in range(len(str(a))):
   count=count*10+a%10
   a=a//10
   i+=1
if count==temp:
   print("palindrome")
else:
     print("not palindrome")


      