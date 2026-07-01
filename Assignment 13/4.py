"""4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code
"""
a=int(input("enter the number:"))
sum=0
while a>0:
      digit=a%10
      print(digit)
      sum=digit 
      a=a//10 
      if sum==digit:
         print("unique code")
         break 
      else:
          print("not unique")
      a+=1  
else:
    print("not unique code")
            
      