a=input("enter a number:")
rev=""
for i in a:
    rev=i+rev
print(rev)

"""WHILE"""
b=int(input("enter a number:"))
rev=0
i=1
while b>0:
      rev=rev*10+b%10
      b=b//10
      i+=1 

print(rev)
