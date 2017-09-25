from PIL import Image, ImageDraw, ImageOps


image = Image.new("RGB", (96, 256))
plane = Image.open("Images/airport-512.ico")
whiteplane = ImageOps.invert(plane)
d = ImageDraw.Draw(image)

image.paste(whiteplane)
d.text((10, 10), "Hello World")

d.text((10, 10), "Hello World")


image.show()