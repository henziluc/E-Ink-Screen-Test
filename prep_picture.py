from PIL import Image, ImageEnhance, ImageOps

# --------------------------------------------------
# Settings
# --------------------------------------------------

INPUT = "picdir/lighthouse2.jpeg"
OUTPUT = "picdir/prepared.png"

WIDTH = 1200
HEIGHT = 1600

SATURATION = 1.6
CONTRAST = 1.25
BRIGHTNESS = 1.05
SHARPNESS = 1.2

# Spectra 6 palette
PALETTE = [
    (0, 0, 0),        # Black
    (255, 255, 255),  # White
    (255, 0, 0),      # Red
    (255, 255, 0),    # Yellow
    (0, 0, 255),      # Blue
    (0, 255, 0),      # Green
]


# --------------------------------------------------
# Load image
# --------------------------------------------------

image = Image.open(INPUT).convert("RGB")


# --------------------------------------------------
# Crop and resize
# --------------------------------------------------

image = ImageOps.fit(
    image,
    (WIDTH, HEIGHT),
    method=Image.Resampling.LANCZOS,
    centering=(0.5, 0.5)
)


# --------------------------------------------------
# Enhance image
# --------------------------------------------------

image = ImageEnhance.Color(image).enhance(SATURATION)

image = ImageEnhance.Contrast(image).enhance(CONTRAST)

image = ImageEnhance.Brightness(image).enhance(BRIGHTNESS)

image = ImageEnhance.Sharpness(image).enhance(SHARPNESS)


# --------------------------------------------------
# Create 6-color palette
# --------------------------------------------------

palette_image = Image.new("P", (1, 1))

palette_data = []

for color in PALETTE:
    palette_data.extend(color)

# Fill remaining palette entries
palette_data.extend([0] * (256 * 3 - len(palette_data)))

palette_image.putpalette(palette_data)


# --------------------------------------------------
# Convert to Spectra 6 colors
#
# Floyd-Steinberg dithering creates the illusion
# of additional colors by mixing pixels.
# --------------------------------------------------

image = image.quantize(
    palette=palette_image,
    dither=Image.Dither.FLOYDSTEINBERG
)


# --------------------------------------------------
# Save
# --------------------------------------------------

image.save(OUTPUT)

print(f"Saved: {OUTPUT}")
print(f"Resolution: {WIDTH} x {HEIGHT}")
print("Spectra 6 palette + dithering applied")