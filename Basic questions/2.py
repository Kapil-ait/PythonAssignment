a=input("enter 1st string:")
b=input("enter 2nd string:")
for i in a:
    for j in b:
        if ord(a[i])==ord(a[j]):
           print("equal")
        else:
           print("not equal")