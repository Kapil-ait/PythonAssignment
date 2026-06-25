n=int(input("enter the numbers:"))
flag="Even"
while n>0:
      x=n%10
      if x%2==1:
         flag="Not Even"
      n=n//10
print(flag)


"""for"""
n=int(input("enter the numbers:"))
flag="Even"
for i in range(len(str(n))):
    x=n%10
    if x%2==1:
         flag="Not Even"
    n=n//10
print(flag)

