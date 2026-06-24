a=int(input("enter total attendance percentages:"))
if a>75:
   print("Status: Eligible")
elif a>60:
     print("Status: Eligible with warning:")
elif a<60:
     print("Status: Not Eligible")
