"""6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number"""

code=int(input("Enter Coupon Number:"))

def is_prime(n, divisor=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

if is_prime(code):
    print("Prime Number")
else:
    print("Not a Prime Number")