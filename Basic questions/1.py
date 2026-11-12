"""a=[[10,20],[30,40]]
a[0]=[9,9]
print(a)
"""

"""a=[[10,20],[30,40]]
a.append([8.9])
print(a)
a[0].append(11)
print(a)
a[0].remove(10)
print(a)"""

"""a=[[1,2],[30,40]]
print(a)
a.pop(1)
print(a)"""

"""a=[
    [1,2],
    [3,4]
]
print(a)"""

"""a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])"""

""""a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in a:
    print(row)"""

"""matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for value in row:
        print(value,end=" ")
    print()"""


"""matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for value in row:
        if value %2==0:
           print(value,end=" ")
    print()"""

"""row=int(input("enter size of row:"))
col=int(input("enter size of col:"))
matrix=[]
print("enter the elements of matrix:")
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print("the matrix is:")
for row in matrix:
    for value in row:
        print(value,end=" ")
    print()"""


row=int(input("enter size of row:"))
col=int(input("enter size of col:"))
matrix=[]
print("enter the elements of matrix:")
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print("the matrix is:")
sum=0
for row in matrix:
    for value in row:
        sum+=value
    print("sum of row:",sum)
