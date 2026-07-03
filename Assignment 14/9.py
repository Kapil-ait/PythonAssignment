s=int(input("enter start year:"))
e=int(input("enter end year:"))
count=0
for i in range(s,e+1):
    if i%4==0 and i%400:
       if i%100==0:
          print(i,"-No Event-")
       else:
           count=count+1
           print(i,"-Event Scheduled-")
    else:
        print(i,"-No Event-")
print("total leap year=",count)
print("total Event scheduled=",count)