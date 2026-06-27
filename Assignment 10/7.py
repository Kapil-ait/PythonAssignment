a=int(input("enter order amount:"))
b=input("enter customer type(VIP/not VIP):")
c=input("enter the payment mode(online/cash):")
if a>=2000:
   if b=="VIP" and c=="online":
      print("give free dessert and 20 percent discount")
   else:
       print("only free desert")
elif b!="VIP":
     if a>=5000:
        print("give 15% discount")
     else:
         print(" give 10 % discount")
elif a<2000:
     if a>=1000 and b=="VIP":
        print("give 10% discount")
     else:
         print("give 5% discount")
elif a<1000:
    print("no Offer")
    
 
      
