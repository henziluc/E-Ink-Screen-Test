from PIL import Image, ImageEnhance, ImageOps

INPUT = "picdir/lighthouse2.jpeg"
OUTPUT = "picdir/prepared.png"

WIDTH = 1200
HEIGHT = 1600

# Load image
image = Image.open(INPUT).convert("RGB")

# Crop + resize without distortion
image = ImageOps.fit(
    image,
    (WIDTH, HEIGHT),
    method=Image.Resampling.LANCZOS,
    centering=(0.5, 0.5)
)

# Color enhancement
image = ImageEnhance.Color(image).enhance(1.6)

# Increase contrast
image = ImageEnhance.Contrast(image).enhance(1.25)

# Slight brightness boost
image = ImageEnhance.Brightness(image).enhance(1.05)

# Sharpen details
image = ImageEnhance.Sharpness(image).enhance(1.3)

# Save as RGB PNG
image.save(OUTPUT)

print(f"Saved {OUTPUT}")
print(f"Size: {image.size}")