n=int(input("enter size:"))
arr=[]
i=0
while i<n:
    arr.append(int(input()))
    i+=1
last=arr[n-1]
i=n-1
while i>0:
    arr[i]=arr[i-1]
    i-=1
arr[0]=last
print(arr)