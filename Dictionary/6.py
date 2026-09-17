"""6.=========================================
MOBILE APP DOWNLOAD COUNTER
===========================
Downloads received from different cities:
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
Write a program to:
* Count downloads city-wise.
* Display city with maximum downloads.
Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
"""

cities=["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
d={}
for user in cities:
  d[user]=d.get(user,0)+1
print(d)
for k,v in d.items():
  print(k,"visited",v,"times")
h=max(d,key=d.get)
print("most dowmload:",h)