seconds=int(input("Enter total seconds:"))
hrs=(seconds)//3600
seconds=seconds-hrs*3600
minutes=(seconds)//60
seconds=seconds-minutes*60

print("Hours :",hrs)
print("Minutes:",minutes)
print("Seconds :",seconds)