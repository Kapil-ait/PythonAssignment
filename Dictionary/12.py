"""12.=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
Write a program to:
* Count orders of each food item.
* Find the most ordered item."""

n=int(input("Enter number:"))
d={}

for i in range(n):
    x=input("Enter food:")
    d[x]=d.get(x,0)+1

for k,v in d.items():
    print(k,":",v)

m=max(d,key=d.get)
print("Most Ordered:",m)
