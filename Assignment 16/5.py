n=int(input("Enter a number: "))
sq=n*n
temp =n
while temp > 0:
    if temp % 10 != sq % 10:
        print("Not Automorphic Number")
        break
    temp = temp //10
    sq = sq //10
else:
    print("Automorphic Number")