num=int(input("enter the number:"))
digit=int(input("enter digit:"))
count=0
while num>0:
      if digit==num%10:
         count+=1
      num=num//10
print(count)

"""FOR"""
num=int(input("enter the number:"))
digit=int(input("enter digit:"))
count=0
for i in range(len(str(num))):
    if digit==num%10:
       count+=1
    num=num//10
print(count)