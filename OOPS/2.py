"""Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
Question 3: Online Shopping System
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
Final Amount      : ₹63000.0
"""

class Customer:
    def __init__(self, customer_id, customer_name, units_consumed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        cost_per_unit = 8
        fixed_charge = 150
        total_bill = (self.units_consumed * cost_per_unit) + fixed_charge
        return total_bill

    def display_bill(self):
        total_bill = self.calculate_bill()
        print("------ Electricity Bill ------")
        print(f"Customer ID       : {self.customer_id}")
        print(f"Customer Name     : {self.customer_name}")
        print(f"Units Consumed    : {self.units_consumed}")
        print(f"Total Bill Amount : ₹{total_bill:.1f}")


cus=Customer(input("Enter Customer ID : "), input("Enter Customer Name : "), int(input("Enter Units Consumed : ")))
cus.display_bill()


