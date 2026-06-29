n = int(input("Enter the number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)

diff = abs(temp - rev)
print("Difference =", diff)

count = 0
t = diff

if t == 0:
    count = 1
else:
    while t > 0:
        count = count + 1
        t = t // 10

print("Digits =", count)

if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")