n=int(input("enter n:"))
i=1
while i<=n:
      print()
      j=i
      while j<=n-1:
            print(" ",end="")
            j=j+1
      j=1
      while j<=i:
            if j%2==0:
               print(0,end="")
            else:
                print(1,end="")
            j=j+1
      i+=1
      
      