a=input("enter subscription(premium/Basic):")
b=int(input("enter progress:"))
c=int(input("enter test score:"))
if a=="premium":
    if b>=80 and c>=70:
       print("Unlock Certificate")
    else:
       print("allow retry")
elif b<80:
     print("Complete the course")
elif a=="Basic" and a>=50 : 
     print("limited access")
else:
     print("deny access")