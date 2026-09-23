"""============================================================
ASSIGNMENT 4 – BANK ACCOUNT SYSTEM
==================================

Create an Account class inside:

models/account.py

ATTRIBUTES:

* account_no
* customer_name
* balance

METHODS:

* deposit()
* withdraw()
* display()

TASKS:

1. Create 5 Account objects.
2. Store all Account objects in a list.
3. Display all accounts.
4. Search an account using Account Number.
5. Deposit money into a selected account.
6. Withdraw money from a selected account.
7. Display accounts having balance greater than 50,000.
8. Find the account having the highest balance.

SAMPLE DATA:

101 Amit 45000
102 Rahul 75000
103 Priya 35000
104 Neha 90000
105 Rohit 55000

SAMPLE OPERATIONS:

Enter Account No: 101

Enter amount to deposit: 10000

After Deposit:
101 Amit 55000

Enter Account No: 103

Enter amount to withdraw: 5000

After Withdrawal:
103 Priya 30000

EXPECTED OUTPUT:

Accounts having balance greater than 50000:

102 Rahul 75000
104 Neha 90000
105 Rohit 55000

Highest Balance Account:

104 Neha 90000"""
class Account:

    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(self.account_no, self.customer_name, self.balance)


# Create 5 accounts
accounts = [
    Account(101, "Amit", 45000),
    Account(102, "Rahul", 75000),
    Account(103, "Priya", 35000),
    Account(104, "Neha", 90000),
    Account(105, "Rohit", 55000)
]


# Display all accounts
print("All Accounts:")
for account in accounts:
    account.display()


# Search account
acc_no = int(input("\nEnter Account No: "))

for account in accounts:
    if account.account_no == acc_no:
        print("Account Found:")
        account.display()

        # Deposit
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

        print("After Deposit:")
        account.display()
        break
else:
    print("Account not found")


# Withdrawal
acc_no = int(input("\nEnter Account No for withdrawal: "))

for account in accounts:
    if account.account_no == acc_no:
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

        print("After Withdrawal:")
        account.display()
        break
else:
    print("Account not found")


# Balance greater than 50000
print("\nAccounts having balance greater than 50000:")

for account in accounts:
    if account.balance > 50000:
        account.display()


# Highest balance
highest = accounts[0]

for account in accounts:
    if account.balance > highest.balance:
        highest = account

print("\nHighest Balance Account:")
highest.display()