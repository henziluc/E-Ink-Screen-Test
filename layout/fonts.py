from PIL import ImageFont

font_large = ImageFont.truetype(
    "fonts/RobotoCondensed-Bold.ttf",
    56
)

font_medium = ImageFont.truetype(
    "fonts/RobotoCondensed-Regular.ttf",
    38
)

font_normal = ImageFont.truetype(
    "fonts/RobotoCondensed-Regular.ttf",
    29
)

font_small = ImageFont.truetype(
    "fonts/RobotoCondensed-Regular.ttf",
    20
)

fill_main = 'black'


spacing_small = font_small.size + 10

spacing_normal = font_medium.size + 10

spacing_large = font_large.size + 10