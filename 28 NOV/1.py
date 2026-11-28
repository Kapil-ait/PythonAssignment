
n = int(input("Enter the size of matrix: "))

matrix = []

print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(*row)

# Main Diagonal Elements
print("\nMain Diagonal Elements:")
for i in range(n):
    print(matrix[i][i], end=" ")

# Secondary Diagonal Elements
print("\n\nSecondary Diagonal Elements:")
for i in range(n):
    print(matrix[i][n - 1 - i], end=" ")

# Transpose Matrix
transpose = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    transpose.append(row)

print("\n\nTranspose Matrix:")
for row in transpose:
    print(*row)

# Swap Main and Secondary Diagonal Elements
for i in range(n):
    j = n - 1 - i
    transpose[i][i], transpose[i][j] = transpose[i][j], transpose[i][i]

print("\nFinal Matrix After Diagonal Swapping:")
for row in transpose:
    print(*row)
