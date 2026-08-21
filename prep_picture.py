from PIL import Image

image = Image.open("picdir/lighthouse2.jpeg")

# Resize to screen resolution
image = image.resize((1200, 1600))

# Make sure it's RGB
image = image.convert("RGB")

image.save("picdir/prepared.png")