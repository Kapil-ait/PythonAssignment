from PIL import Image

image = Image.open("wallpaper.jpg")

print("Image Size:", image.size)
print("Image Format:", image.format)

image = image.resize((300, 300))

image.save("122951.png")

print("Image saved successfully")