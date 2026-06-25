n = int(input("Enter a number: "))
count = 0
while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        count += 1
    n = n // 10
print("Even digits count =", count)



"""for"""
n = int(input("Enter a number: "))
count = 0 
for i in range(len(str(n))):
     digit = n % 10
 
     if digit % 2 == 0:
        count += 1
     n = n // 10
print("Even digits count =", count)