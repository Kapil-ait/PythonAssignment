a=int(input("enter temperature:"))
if a<0:
   print("freezing")
elif a>0 and a<20:
     print("Weather Condition:cold")
elif a>21 and a<35:
     print("Weather Condition: warm")
elif a>35:
     print("Weather Condition: hot")
