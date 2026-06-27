a=int(input("enter age:"))
b=input("Severity(critical/moderate/low):")
c=input("insurance(yes/no):")
if b=="critical":
   if a>=60:
      print("assign immediate ICU")
   else:
       print("assign emergency ward")
elif b=="moderate":
     if c=="yes":
        print("priority treatment")
     else:
         print("assign general queue")
elif b=="low":
     if a<10:
        print("assign Pediatric Priority")
     else:
         print("assign wait")
     