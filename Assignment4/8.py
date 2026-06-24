p,r,t,=map(int,input("enter principle rate or time").split())
total_amount=p*(1+r/100)**t
print("Total amount :",total_amount)