a = int(input("Enter the number: "))

rem = 0
while a > 0:
    digit = a % 10
    rem = rem + digit * digit
    a = a // 10

print(rem)

total = 0
while rem > 0:
    digit = rem % 10
    total = total + digit
    rem = rem // 10

print("the sum is:",total)