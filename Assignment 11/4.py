a = int(input("Enter a number: "))
temp = a
sum = 0

while a > 0:
    digit = a % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    a = a // 10

if sum == temp:
    print("Strong Number")
else:
    print("Not Strong Number")