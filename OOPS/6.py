"""Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0"""

class guest:
    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_days = number_of_days
        self.room_charge_per_day = room_charge_per_day

    def calculate_bill(self):
        room_bill = self.number_of_days * self.room_charge_per_day
        gst = 0.12 * room_bill
        final_bill = room_bill + gst
        return room_bill, gst, final_bill

    def display_bill(self):
        room_bill, gst, final_bill = self.calculate_bill()
        print("------ Hotel Bill ------")
        print(f"Guest ID              : {self.guest_id}")
        print(f"Guest Name            : {self.guest_name}")
        print(f"Number of Days        : {self.number_of_days}")
        print(f"Room Charge Per Day   : ₹{self.room_charge_per_day}")
        print(f"Room Bill             : ₹{room_bill}")
        print(f"GST (12%)             : ₹{gst}")
        print(f"Final Bill            : ₹{final_bill}")
gt=guest(input("Enter Guest ID : "), input("Enter Guest Name : "), int(input("Enter Number of Days : ")), float(input("Enter Room Charge Per Day : ")))
gt.display_bill()
