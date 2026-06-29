a=int(input("enter the number:"))
while a>0:
     
     digit=a%10
     print(digit)
     a=a//10
     if digit==0:
        print("duck number")
        break
else:
    print("not duck")
     
   
    
    
    
    
