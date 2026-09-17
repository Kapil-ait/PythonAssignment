list1 = [41, 88, 90, 31,77]

result = list(map(lambda x: "A" if x > 80 else "B" if x > 60 else "C" if x > 40 else "FAIL", list1))

print(result)