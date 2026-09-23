"""============================================================



ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM
=============================================

A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:

* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.

Additional attribute:

* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:

* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:

display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:

Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account

For Savings Account:

Enter Interest Rate:

For Premium Savings Account:

Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000
"""
class Account:

    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
        else:
            self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

    def display_account(self):
        print("\nAccount Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient Balance")


class SavingsAccount(Account):

    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def display_account(self):
        super().display_account()
        print("Account Type: Savings Account")
        print("Interest Rate:", self.interest_rate, "%")


class PremiumSavingsAccount(SavingsAccount):

    def __init__(self, account_number, customer_name, balance,
                 interest_rate, cashback_percentage):
        super().__init__(account_number, customer_name, balance, interest_rate)
        self.cashback_percentage = cashback_percentage

    def display_account(self):
        super().display_account()
        print("Account Type: Premium Savings Account")
        print("Cashback Percentage:", self.cashback_percentage, "%")


# Input
account_number = int(input("Enter Account Number: "))
customer_name = input("Enter Customer Name: ")
initial_balance = float(input("Enter Initial Balance: "))

print("\n1. Savings Account")
print("2. Premium Savings Account")

account_type = int(input("Enter Account Type: "))

if account_type == 1:

    interest_rate = float(input("Enter Interest Rate: "))

    account = SavingsAccount(
        account_number,
        customer_name,
        initial_balance,
        interest_rate
    )

else:

    interest_rate = float(input("Enter Interest Rate: "))
    cashback_percentage = float(input("Enter Cashback Percentage: "))

    account = PremiumSavingsAccount(
        account_number,
        customer_name,
        initial_balance,
        interest_rate,
        cashback_percentage
    )


# Display account
print("\n## Account Details")
account.display_account()


# Deposit
deposit_amount = float(input("\nEnter amount to deposit: "))
account.deposit(deposit_amount)

print("\nAfter Deposit:")
print("Balance:", account.balance)


# Withdraw
withdraw_amount = float(input("\nEnter amount to withdraw: "))
account.withdraw(withdraw_amount)

print("\nAfter Withdrawal:")
print("Balance:", account.balance)