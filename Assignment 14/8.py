a=int(input("enter the classes:"))
b=int(input("enter the students:"))
c=int(input("enter the subjects:"))
for i in range(1,a+1):
    print("classes",i)
    for j in range(1,b+1):
        print("student",j)
        sum=0
        for k in range(1,c+1):
            a=int(input("enter the marks:"))
            sum=sum+a
        print("student",j,"total",sum)
        print()
    print()      
