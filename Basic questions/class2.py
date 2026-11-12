"""a=[1,2,3,4]
b=[i*3 for i in a]
print(b)"""


"""a=[1,2,3,4,5,6]
r=[val for val in a if val%2==0]
print(r)"""


"""a=[1,2,3,4,5,6]
r=[val*val for val in a if val>3 and val%2==0]
print(r)"""


"""a=[1,2,3,4,5,6]
r=["even" if val%2==0 else "odd" for val in a]
print(r)"""


"""a=["java","python","c++"]
r=[len(w) for w in a]
print(r)"""

"""a=["java","python","c++"]
r=[w.upper() for w in a]
print(r)"""\

"""a=["java","python","c++"]
r=[w for w in a if len(w)>3]
print(r)"""

a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
