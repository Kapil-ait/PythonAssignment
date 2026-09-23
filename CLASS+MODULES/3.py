"""
============================================================
ASSIGNMENT 3 – PRODUCT INVENTORY SYSTEM
=======================================

Create a Product class inside:

models/product.py

ATTRIBUTES:

* product_id
* product_name
* price
* quantity

TASKS:

1. Take details of 5 products from the user.

2. Create Product objects.

3. Store all objects in a list.

4. Display all products.

5. Calculate total value of each product.

   Total Value = Price × Quantity

6. Display products whose quantity is less than 10.

7. Find the product having the highest price.

8. Calculate total inventory value.

9. Search a product using Product Id.

SAMPLE INPUT:

101 Laptop 55000 5
102 Mouse 800 25
103 Keyboard 1500 12
104 Monitor 12000 7
105 Printer 9000 15

EXPECTED OUTPUT:

All Products:
101 Laptop 55000 5
102 Mouse 800 25
103 Keyboard 1500 12
104 Monitor 12000 7
105 Printer 9000 15

Product Total Values:
Laptop = 275000
Mouse = 20000
Keyboard = 18000
Monitor = 84000
Printer = 135000

Low Stock Products:
Laptop
Monitor

Highest Price Product:
Laptop = 55000

Total Inventory Value:
532000

Search Product Id: 103

Product Found:
103 Keyboard 1500 12"""

from itertools import product


class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_id} {self.product_name} {self.price} {self.quantity}"
    def display_all_products(products): 
        print("All Products:")
        for p in products:
            print(p)
    def display_total_values(products):
        print("Product Total Values:")
        for p in products:
            print(f"{p.product_name} = {p.total_value()}")
    def display_low_stock(products):
        print("Low Stock Products:")
        for p in products:
            if p.quantity < 10:
                print(p.product_name)
    def highest_price_product(products):
        highest = max(products, key=lambda p: p.price)
        print("Highest Price Product:")
        print(f"{highest.product_name} = {highest.price}")
    def total_inventory_value(products):
        total_value = sum(p.total_value() for p in products)
        print("Total Inventory Value:")
        print(total_value)
    def search_product(products, product_id):
        for p in products:
            if p.product_id == product_id:
                print("Product Found:")
                print(p)
                return
        print("Product Not Found")
pro=[]
pro=product(101, "Laptop", 55000, 5)
pro.append(pro)
pro.display_all_products(pro)
pro=product(102, "Mouse", 800, 25)
pro.append(pro) 