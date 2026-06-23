totalseconds=int(input("enter the numbers in seconds:"))
hours= totalseconds // 3600
remainingseconds=totalseconds % 3600
minutes=remainingseconds // 60
seconds=remainingseconds % 60
print("total hours:",hours,"total minutes:",minutes,"total seconds:",seconds)
