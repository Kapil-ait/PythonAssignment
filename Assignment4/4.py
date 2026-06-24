speed = int(input("Enter speed in kmph: "))
hours, minutes = map(int, input("Enter hours and minutes: ").split())

time = hours + minutes / 60
distance = speed * time

print("Distance is:", distance, "km")
