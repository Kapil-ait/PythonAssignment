n = int(input("Enter a number: "))
count = 0
fact=0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        fact=fact+i


print("Factors Count =", count)
print(fact)