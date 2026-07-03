a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for n in range(a, b + 1):
    square = n * n
    temp = square
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10
    if sum == n:
        print(n)