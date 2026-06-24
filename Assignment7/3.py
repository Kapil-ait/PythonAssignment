a = int(input("Enter yearly income: "))

if a <= 250000:
    print("No Tax")
elif a <= 500000:
    print("Tax =", a * 5 / 100)
elif a <= 1000000:
    print("Tax =", a * 20 / 100)
else:
    print("Tax =", a * 30 / 100)