n = int(input("Enter the last ID: "))

num = n + 1

while True:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print("Next Prime =", num)
        break

    num = num + 1