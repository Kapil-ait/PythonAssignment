"""Assignment 5: Shopping Bill Calculator

 A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity.

calculate_discount() – Calculate the discount amount.

calculate_gst() – Calculate GST on the discounted amount.

calculate_final_bill() – Calculate the final payable amount.

display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST"""

class prodctbill:
    def __init__(self, product_name, product_price, quantity, discount_percentage, gst_percentage):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity
        self.discount_percentage = discount_percentage
        self.gst_percentage = gst_percentage
    def calculate_subtotal(self):
        return self.product_price * self.quantity
    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.discount_percentage / 100
    def calculate_gst(self):
        discounted_amount = self.calculate_subtotal() - self.calculate_discount()
        return discounted_amount * self.gst_percentage / 100
    def calculate_final_bill(self):
        discounted_amount = self.calculate_subtotal() - self.calculate_discount()
        gst = self.calculate_gst()
    
        return discounted_amount + gst
    def display_bill(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        gst = self.calculate_gst()
        final_bill = self.calculate_final_bill()
        print(f"Product Name: {self.product_name}")
        print(f"Product Price: {self.product_price}")
        print(f"Quantity: {self.quantity}")
        print(f"Subtotal: {subtotal}")
        print(f"Discount ({self.discount_percentage}%): {discount}")
        print(f"GST ({self.gst_percentage}%): {gst}")
        print(f"Final Bill: {final_bill}")
p=prodctbill("Laptop", 50000, 1, 10, 18)
p.calculate_discount()
p.calculate_gst()
p.calculate_final_bill()
p.display_bill()