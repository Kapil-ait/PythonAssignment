"""
5.
 Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found"""

id=input("enter patient id:")
digit=input("enter digit to search:")

def search_digit(num, target):
    if num == 0:
        return False
    else:
        last_digit = num % 10
        if last_digit == target:
            return True
        else:
            return search_digit(num // 10, target)

if search_digit(int(id), int(digit)):
    print("Digit Found")
else:
    print("Digit Not Found")