from PIL import Image, ImageDraw


image = Image.new("RGB", (96, 256))

d = ImageDraw.Draw(image)

d.text((10,10), "Hello World")

image.show()