"""EXPENSES tracker"""
print("======================================================")
print("======welcome to my expenses tracker portal=====")
print("======================================================")
sal=int(input("enter the monthly salary:"))
if sal < 10000:
    limit = 1
else:
    limit = sal // 10000
print("you can only do {} expenses ".format(limit))
ex = int(input("Enter number of expenses: "))
if ex > limit:
    print("ALERT 🚨You can only enter", limit, "expense(s).")
print("1. Food\n2. Grocery\n3. Rent\n4. Electricity Bill\n5. Water Bill\n6. Gas Cylinder\n7. Internet / Wi-Fi\n8. Mobile Recharge\n9. Travel / Fuel\n10. Shopping")
cat=0
if sal<=10000:
   cat=1
elif sal<=50000:
     cat=2
elif sal<=100000:
     cat=3
elif sal<=500000:
     cat=4
else:
    cat=5
match cat:
      case 1:
           ex=input("enter 1st expense:")
           am=int(input("enter amount of 1st expense:"))
           print("expense of {} is {}".format(ex,am))
           if am>sal:
              print("your expense amount is more than your salary:")
           rem=sal-am
           print("remaining salary is:",rem)
           avg=am/1
           print("Average is:",avg)
           
      case 2:
           ex=input("enter 1st expense:")
           am=int(input("enter amount of 1st expense:"))
           total=am
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)
           ex1=input("enter 2nd expense:")
           am1=int(input("enter amount of 2nd expense:"))
           total=total+am1
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)
           print("expense of {} is {} and expense of{} is{}".format(ex,am,ex1,am1))
           total=am+am1
           if total>sal:
              print("your expense amount is more than your salary:")
           rem=sal-total
           print("remaining salary is:",rem)
           highest=max(am,am1)
           if highest==am:
              print("highest is:",am)
           else:
               print("highest is:",am1)
           avg=(am+am1)/2
           print("Average is:",avg)        

      case 3:
           ex=input("enter 1st expense:")
           am=int(input("enter amount of 1st expense:"))
           total=am
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)
           ex1=input("enter 2nd expense:")
           am1=int(input("enter amount of 2nd expense:"))
           total=total+am1
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)  
           ex2=input("enter 3rd expense:")
           am2=int(input("enter amount of 3rd expense:"))
           total=total+am2
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal) 
           print("expense of {} is {} and expense of{} is{} and expense of{} is {}".format(ex,am,ex1,am1,ex2,am2)) 
           total=am+am1+am2
           if total>sal:
              print("your expense amount is more than your salary:")
           rem=sal-total
           print("remaining salary is:",rem) 
           highest=max(am,am1,am2)
           if highest==am:
              print("highest is:",am)
           elif highest==am1:
                print("highest is:",am1)
           else:
               print("highest is:",am2)
           avg=(am+am1+am2)/3
           print("Average is:",avg)        
  
      case 4:
           ex=input("enter 1st expense:")
           am=int(input("enter amount of 1st expense:"))
           total=am
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)
           ex1=input("enter 2nd expense:")
           am1=int(input("enter amount of 2nd expense:"))
           total=am1
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)  
           ex2=input("enter 3rd expense:")
           am2=int(input("enter amount of 3rd expense:"))
           total=am2
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)            
           ex3=input("enter 4th expense:")
           am3=int(input("enter amount of 4th expense:"))
           total=am3
           if total > sal:
              print("⚠️ ALERT! Salary exceeded by", total - sal)  
           print("expense of {} is {} and expense of{} is{} and expense of {} is{} and expense of{} is {}".format(ex,am,ex1,am1,ex2,am2,ex3,am3)) 
           total=am+am1+am2+am3
           if total>sal:
              print("your expense amount is more than your salary:")
           rem=sal-total
           print("remaining salary is:",rem)
           highest=max(am,am1,am2,am3)
           if highest==am:
              print("highest is:",am)
           elif highest==am1:
                print("highest is:",am1)
           elif highest==am2:
                print("highest is:",am2)
           else:
               print("highest is:",am3)
           avg=(am+am1+am2+am3)/4
           print("Average is:",avg)
      case 5:
           print("you can do unlimited expenses as your salary is more than 500000")

         
           
        
      
       

