a = int(input("Enter the number: "))
temp = a
cum = 0

while a > 0:
    digit = a % 10
    cum = cum + digit * digit * digit
    a = a // 10

if cum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number") 

"""for"""
a = int(input("Enter the number: "))
temp = a
cum = 0
for i in range(len(str(a))):
    digit = a % 10
    cum = cum + digit * digit * digit
    a = a // 10
if cum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number") 
    