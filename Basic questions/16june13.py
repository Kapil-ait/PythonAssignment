
p=int(input("enter principal:"))
r=int(input("enter rate:"))
t=int(input("enter time:"))
amount = int(p*(1+r/100)**t)
ci = int(amount-p)
print("Amount :",amount)
print("Ci :",ci)