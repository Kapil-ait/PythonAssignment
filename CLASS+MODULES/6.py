"""============================================================
ASSIGNMENT 6 – CUSTOMER MANAGEMENT SYSTEM
=========================================

Create a Customer class inside:

models/customer.py

ATTRIBUTES:

* customer_id
* customer_name
* city
* purchase_amount

TASKS:

1. Take details of 5 customers.
2. Create Customer objects.
3. Store all objects in a list.
4. Display all customers.
5. Display customers from a particular city.
6. Display customers whose purchase amount is greater than 10,000.
7. Find the customer having the highest purchase amount.
8. Calculate total sales.
9. Calculate average purchase amount.
10. Search customer using Customer Id.

SAMPLE DATA:

101 Amit Indore 12000
102 Rahul Bhopal 8000
103 Priya Indore 15000
104 Neha Pune 22000
105 Rohit Indore 7000

EXPECTED OUTPUT:

Customers from Indore:

101 Amit 12000
103 Priya 15000
105 Rohit 7000

Customers with purchase amount greater than 10000:

101 Amit 12000
103 Priya 15000
104 Neha 22000

Highest Purchase Customer:

104 Neha 22000

Total Sales:

64000

Average Purchase Amount:

12800

Search Customer Id: 103

Customer Found:

103 Priya Indore 15000"""
class Customer:

    def __init__(self, customer_id, customer_name, city, purchase_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.city = city
        self.purchase_amount = purchase_amount


customers = []

# Take details of 5 customers
for i in range(5):
    print("\nEnter Customer", i + 1)

    id = int(input("Customer ID: "))
    name = input("Customer Name: ")
    city = input("City: ")
    amount = float(input("Purchase Amount: "))

    customers.append(Customer(id, name, city, amount))


# Display all customers
print("\n--- All Customers ---")
for c in customers:
    print(c.customer_id, c.customer_name, c.city, c.purchase_amount)


# City search
city = input("\nEnter city: ")

print("\n--- Customers from", city, "---")
for c in customers:
    if c.city.lower() == city.lower():
        print(c.customer_id, c.customer_name, c.purchase_amount)


# Purchase greater than 10000
print("\n--- Purchase Greater Than 10000 ---")
for c in customers:
    if c.purchase_amount > 10000:
        print(c.customer_id, c.customer_name, c.purchase_amount)


# Highest purchase
highest = customers[0]

for c in customers:
    if c.purchase_amount > highest.purchase_amount:
        highest = c

print("\n--- Highest Purchase Customer ---")
print(highest.customer_id, highest.customer_name, highest.purchase_amount)


# Total sales
total = 0

for c in customers:
    total += c.purchase_amount

print("\nTotal Sales:", total)


# Average
average = total / len(customers)

print("Average Purchase Amount:", average)


# Search by Customer ID
search_id = int(input("\nEnter Customer ID: "))

for c in customers:
    if c.customer_id == search_id:
        print("\nCustomer Found:")
        print(c.customer_id, c.customer_name, c.city, c.purchase_amount)
        break
else:
    print("Customer Not Found")