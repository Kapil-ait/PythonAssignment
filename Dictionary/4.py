"""4.=========================================
STUDENT GRADE ANALYSIS
======================
Store student marks in a dictionary.
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
Write a program to:
* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65"""

n=int(input("enter number:"))
d={}
for i in range(n):
  key=input("enter key:")
  value=int(input("enter value:"))
  d[key]=value

h=max(d,key=d.get)
l=min(d,key=d.get)
print("Highest Marks:",h,d[h])
print("Lowest Marks:",l,d[l])
