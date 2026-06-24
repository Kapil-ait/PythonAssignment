a=int(input("enter distance:"))
b=input("enter class:")
if a<100 and b=="AC":
   if b=="Sleeper": 
      print(" Sleeper - 100") 
   else: 
        print("AC - 200")
elif a>100 and a<500:
      if b=="sleeper": 
         print( "Sleeper - 300") 
      else: 
          print("AC - 600")
elif a>=500:
     if b=="sleeper": 
        print( "Sleeper - 500") 
     else: 
          print("AC - 1000")
      
	