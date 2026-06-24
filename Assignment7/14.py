a=input("enter course category(programming/design/marketing):")
b=input("enter user type(student/working professional/others):")
if b=="student" and a=="programming" :
   bill=5000*20/100
   final=5000-bill
   print(final)
elif b=="student" and a=="design" :
   bill=4000*20/100
   final=4000-bill
   print(final)
elif b=="student" and a=="marketing" :
   bill=3000*20/100
   final=3000-bill
   print(final)
if b=="working professional" and a=="programming" :
   bill=5000*10/100
   final=5000-bill
   print(final)
elif b=="working professional" and a=="design" :
   bill=4000*10/100
   final=4000-bill
   print(final)
elif b=="working professional" and a=="marketing" :
   bill=3000*10/100
   final=3000-bill
   print(final)
if b=="others" and a=="programming" :
   
   print("amount to be paid:5000")
elif b=="others" and a=="design" :
     print("amount to be paid:4000")
elif b=="others" and a=="marketing" :
     print("amount to be paid:3000")


