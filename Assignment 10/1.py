a=input("enter the subscription(premium/basic):")
b=int(input("enter progress:"))
c=int(input("enter test score:"))
if a=="premium":
    if b>=80 and c>=70:
       print("unlock certificate")
    elif b<80 :
         print("complete course")
    else:
        print(" retry")
elif a=="basic":
     if b>=50 :
        print("allow limited access")
     else:
         print("lock content")
else:
    print(" retry")

