"""10.=========================================
EMAIL DOMAIN COUNTER
====================
emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]
Write a program to:
* Count users belonging to each email domain.
Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}
---
"""
n=int(input("Enter number:"))
d={}
for i in range(n):
    email=input("Enter email:")
    domain=email.split("@")[1]
    d[domain]=d.get(domain,0)+1
print(d)