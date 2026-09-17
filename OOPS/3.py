"""Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0"""
class Product:
    def __init__(self, product_id, product_name, quantity, price_per_item):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item

    def calculate_final_amount(self):
        total_amount = self.quantity * self.price_per_item
        if total_amount > 5000:
            discount = total_amount * 0.10
        else:
            discount = total_amount * 0.05
        final_amount = total_amount - discount
        return total_amount, discount, final_amount

    def display_bill(self):
        total_amount, discount, final_amount = self.calculate_final_amount()
        print("------ Shopping Bill ------")
        print(f"Product ID        : {self.product_id}")
        print(f"Product Name      : {self.product_name}")
        print(f"Quantity          : {self.quantity}")
        print(f"Price Per Item    : {self.price_per_item:.1f}")
        print(f"Total Amount      : ₹{total_amount:.1f}")
        print(f"Discount          : ₹{discount:.1f}")
        print(f"Final Amount      : ₹{final_amount:.1f}")
pro=Product(input("Enter Product ID : "), input("Enter Product Name : "), int(input("Enter Quantity : ")), float(input("Enter Price Per Item : ")))
pro.display_bill()