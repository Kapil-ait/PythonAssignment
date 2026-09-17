"""Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000"""

class BankAccount:
    def __init__(self, account_number, account_holder, balance,open_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.opening_balance = open_balance  # Store the opening balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def display_account(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Final Balance: {self.balance}")

b=BankAccount(1001, "Rahul", 25000, 25000)
b.deposit(5000)
b.withdraw(3000)
b.display_account()
