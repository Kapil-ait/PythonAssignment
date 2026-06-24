"""
Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable
"""

salary=int(input("enter your Salary: "))
if salary>=30000:
    print("Eligible for PF")
if salary>=55000:
    print("Eligible for bonus")