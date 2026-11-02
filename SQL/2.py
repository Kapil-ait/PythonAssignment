s = input().strip()

n = len(s)
lps = [0] * n

length = 0
i = 1

while i < n:
    if s[i] == s[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length != 0:
        length = lps[length - 1]
    else:
        lps[i] = 0
        i += 1

ans = lps[-1]

if ans == 0:
    print("Not Found")
else:
    print(s[:ans])