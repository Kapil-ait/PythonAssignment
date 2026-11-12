n=int(input("enter size:"))
k=int(input("enter target sum:"))
arr=[]
print("enter elements:")
for i in range(n):
    arr.append(int(input()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            count+=1
print("number of pairs with sum",k,"is:",count)