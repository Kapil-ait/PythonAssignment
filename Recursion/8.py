"""
4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password"""

password=input("Enter Password:")
def check_even_digits(num):
    if num == 0:
        return True
    else:
        last_digit = num % 10
        if last_digit % 2 != 0:
            return False
        else:
            return check_even_digits(num // 10)

if check_even_digits(int(password)):
    print("Strong Password")
else:
    print("Weak Password")
