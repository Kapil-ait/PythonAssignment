d,m,p=map(int,input("Enter distance mileage petrol price").split())
petrol_used = d/m
total_cost = petrol_used*p
print("petrol used: ",petrol_used)
print("Total Cost :",total_cost)