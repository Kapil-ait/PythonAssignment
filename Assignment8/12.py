a=int(input("enter the numbers:"))
count=1
while a>0:
      count=count*(a%10)
      a=a//10
print(count)
if count%2==0:
   print("even")
else:
     print("odd")

"""FOR"""
a=int(input("enter the numbers:"))
count=1
for i in range(len(str(a))):
     count=count*(a%10)
     a=a//10
print(count)
if count%2==0:
   print("even")
else:
     print("odd")