a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while a<=b:
      n=a
      if n>1:
         i=2
         while i<=n//2:
               if n%i==0:
                  break
               i=i+1
         else:
              print(n)
      a=a+1
