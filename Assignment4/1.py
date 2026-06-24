a=int(input("enter total bill amount:"))
b=int(input("enter GST percentage:"))
c=int(input("enter service charges percentage:"))
d=int(input("enter number of friends:"))
gsttotal=a*b/100
servictotal=a*c/100
totalbill=a+gsttotal+servictotal
print("final bill:",totalbill)
pay=totalbill/d
print("each should pay:",pay)