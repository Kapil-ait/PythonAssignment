"""11.=========================================
PRODUCT SALES ANALYSIS
======================
sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
Write a program to:
* Count sales of each product.
* Display products in sorted order.
Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
---"""

n=int(input("Enter number:"))
d={}
for i in range(n):
    x=input("Enter product:")
    d[x]=d.get(x,0)+1

for k in sorted(d):
    print(k,":",d[k])