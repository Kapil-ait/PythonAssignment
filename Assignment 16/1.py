a=int(input("enter starting year:"))
b=int(input("enter last year:"))
i=a
count=0
while i<=b:
      if i%4==0:
           if i%100==0:
               if i%400==0:
                   print(i,"--Event Scheduled ")
                   count=count+1
               else:
                    print(i,"--Event not Scheduled ")
           else:
                print(i,"--Event Scheduled ")
                count+=1
      else:
            print(i,"--Event not Scheduled ") 
      i+=1
print("Total leap years:",count)
print("Total Events Scheduled:",count)
