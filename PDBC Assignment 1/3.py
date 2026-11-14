"""=========================================================
ASSIGNMENT 3: PRODUCT INVENTORY MANAGEMENT SYSTEM
=========================================================

SCENARIO
--------
A retail shop wants to manage product details, prices,
categories, and available stock using Python PDBC.

CONCEPTS TO PRACTICE
--------------------
1. INSERT
2. SELECT
3. UPDATE
4. DELETE
5. LIKE operator
6. Parameterized queries
7. commit()
8. fetchall()
9. Menu-driven programming


TABLE STRUCTURE
===============

Table Name: product_pdbc

Column       Data Type
--------------------------------
pid          INT PRIMARY KEY
pname        VARCHAR(60)
category     VARCHAR(40)
price        DECIMAL(10,2)
quantity     INT


SAMPLE DATA
===========

pid   pname       category       price       quantity
------------------------------------------------------------
301   Laptop      Electronics    55000.00    10
302   Mouse       Electronics      800.00    50
303   Keyboard    Electronics     1500.00    30
304   Notebook    Stationery       100.00   100
305   Pen         Stationery        20.00   200


MENU
====

===== PRODUCT INVENTORY SYSTEM =====
1. Add Product
2. Display All Products
3. Search Product by Name
4. Update Product Price
5. Delete Product
6. Exit

Enter your choice:


TASK 1: ADD PRODUCT
===================

INPUT
-----
Enter your choice: 1
Enter Product ID: 306
Enter Product Name: Monitor
Enter Category: Electronics
Enter Price: 12000
Enter Quantity: 15

OUTPUT
------
Product inserted successfully.


TASK 2: DISPLAY ALL PRODUCTS
============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
303   Keyboard      Electronics      1500.00    30
304   Notebook      Stationery        100.00   100
305   Pen           Stationery         20.00   200
306   Monitor       Electronics     12000.00    15


TASK 3: SEARCH PRODUCT BY NAME USING LIKE
=========================================

INPUT
-----
Enter your choice: 3
Enter product name to search: o

OUTPUT
------
Matching products:

ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
304   Notebook      Stationery        100.00   100
306   Monitor       Electronics     12000.00    15

NOTE
----
Use:
WHERE pname LIKE %s

Pass:
'%' + search_name + '%'


TASK 4: UPDATE PRODUCT PRICE
============================

INPUT
-----
Enter your choice: 4
Enter Product ID: 302
Enter New Price: 900

OUTPUT
------
Product price updated successfully.


TASK 5: DELETE PRODUCT
======================

INPUT
-----
Enter your choice: 5
Enter Product ID: 305

OUTPUT
------
Product deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Product Inventory System.


add these scenarios also:--

1. Display all products from Electronics category.
2. Display all products from Stationery category.
3. Search products whose names contain 'oo'.
4. Search products whose names start with 'M'.
5. Search products whose names end with 'e'.
6. Display products whose price is greater than 1000.
7. Display products whose quantity is less than 20.
8. Update product quantity.
9. Update product category.
10. Delete a product by ID.
11. Display products whose category contains 'tron'.
12. Search products by a user-provided price range.



SUGGESTED SUCCESS MESSAGES
==========================

INSERT:
Record inserted successfully.

SELECT:
Records displayed successfully.

UPDATE:
Record updated successfully.

DELETE:
Record deleted successfully.

NOT FOUND:
No record found for the given ID.

INVALID CHOICE:
Invalid choice. Please try again.

EXIT:
Thank you for using the system."""

import mysql.connector
print("started")
conn=mysql.connector.connect(
       host="localhost",port=3307,user="root",password="Kapil@123",database="batch19")
cursor=conn.cursor()
cursor.execute("create table if not exists product_pdbc(pid int primary key,pname varchar(60),category varchar(40),price decimal(10,2),quantity int)")

data= [
    (301, 'Laptop', 'Electronics', 55000.00, 10),
    (302, 'Mouse', 'Electronics', 800.00, 50),
    (303, 'Keyboard', 'Electronics', 1200.00, 25),
    (304, 'Notebook', 'Stationery', 100.00, 100),
    (305, 'Pen', 'Stationery', 20.00, 50)
     ]
cursor.executemany("insert into product_pdbc values(%s,%s,%s,%s,%s)",data)
conn.commit()

print("Records inserted successfully.")

cursor.execute("select * from product_pdbc")

rows = cursor.fetchall()

print("success")
print("Records displayed successfully.")
while True:
    print("\n===== PRODUCT INVENTORY SYSTEM =====")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product by Name")
    print("4. Update Product Price")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        pid = int(input("Enter Product ID: "))
        pname = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        cursor.execute("insert into product_pdbc values(%s,%s,%s,%s,%s)", (pid, pname, category, price, quantity))
        conn.commit()
        print("Product inserted successfully.")

    elif choice == '2':
        cursor.execute("select * from product_pdbc")
        rows = cursor.fetchall()
        print("\nID\tProduct\t\tCategory\tPrice\tQuantity")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

    elif choice == '3':
        search_name = input("Enter product name to search: ")
        cursor.execute("select * from product_pdbc where pname like %s", ('%' + search_name + '%',))
        rows = cursor.fetchall()
        if rows:
            print("\nMatching products:")
            print("\nID\tProduct\t\tCategory\tPrice\tQuantity")
            print("-" * 60)
            for row in rows:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
        else:
            print("No matching products found.")

    elif choice == '4':
        pid = int(input("Enter Product ID: "))
        new_price = float(input("Enter New Price: "))
        cursor.execute("update product_pdbc set price=%s where pid=%s", (new_price, pid))
        conn.commit()
        if cursor.rowcount > 0:
            print("Product price updated successfully.")
        else:
            print("No record found for the given ID.")

    elif choice == '5':
        pid = int(input("Enter Product ID: "))
        cursor.execute("delete from product_pdbc where pid=%s", (pid,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Product deleted successfully.")
        else:
            print("No record found for the given ID.")
    elif choice == '6':
        print("Thank you for using Product Inventory System.")
        break

cursor.close()
conn.close()

