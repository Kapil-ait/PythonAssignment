a=input("enter vehicle type(bike/car/bus):"
)
b=int(input("enter duration in hours:"))
if a=="bike":
   final=10*b
   print(final)
elif a=="car":
   final=20*b
   print(final)
elif a=="bus":
   final=50*b
   print(final)
if b>5:
   final=final+100
   print("after penalty:",final)