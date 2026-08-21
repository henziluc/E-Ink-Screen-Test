from PIL import Image, ImageEnhance

image = Image.open("picdir/lighthouse2.jpeg")

# Resize to screen resolution
image = image.resize((1200, 1600))

# Make sure it's RGB
image = image.convert("RGB")

# Increase color saturation
image = ImageEnhance.Color(image).enhance(1.8)

# Increase contrast
image = ImageEnhance.Contrast(image).enhance(1.3)

# Slightly increase brightness
image = ImageEnhance.Brightness(image).enhance(1.05)

image.save("picdir/prepared.png")