"""1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6"""


n=int(input("enter  number:"))
d={}
for i in range(n):
    key=input("enter key:")
    value=int(input("enter value:"))
    d[key]=value
for k,v in d.items():
    print(k,"and",v)
s=sum(d.values())
print("sum is:",s)