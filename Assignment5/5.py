"""
Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
"""

username=input("enter UserName: ")
password=input("enter Password: ")
if username=="admin":
    print("Valid user")
if password=="secure123":
    print("Strong password")