a=int(input("enter total price :"))
b=int(input("enter down payament:"))
c=int(input("enter interest rate:"))
d=int(input("enter total months:"))
remainingamount=a-b
e=remainingamount+c

totalemi=remainingamount/c
f=remainingamount+totalemi
final=f/d

print("remaining amount is:",remainingamount)
print("total with interest is:",f)
print("monthly EMI:",final)
