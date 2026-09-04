import datetime
from PIL import Image, ImageOps
from pathlib import Path

from .fonts import font_massiv, fill_main
from .helpers import draw_centered_text

BASE_DIR = Path(__file__).resolve().parent.parent
moon_full_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon-phases_1.svg"
moon_3_4_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon-phases_2.svg"
moon_half_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon-phases_3.svg"
moon_1_4_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon-phases_4.svg"

def display_welcome(draw, image, x_start, y_start, moon_data):
    
    
    x_end = 1200 - 2 * x_start
    y_end = font_massiv.size + y_start
    now = datetime.datetime.now()   
    now_hour = now.hour
    
    if 4 <= now_hour < 12:
        text = 'Good Morning'
    elif 12 <= now_hour < 18:
        text = 'Good Afternoon'
        display_moon_phase(image, x_end, y_start, moon_data)
    elif 18 <= now_hour < 21:
        text = 'Good Evening'
    else:
        text = 'Good Night'
        display_moon_phase(image, x_end, y_start, moon_data)
    draw_centered_text(draw, text,(x_start, y_start, x_end, y_end), font_massiv, fill_main)
    
    
def display_moon_phase(image, x_start, y_start, moon_data):
    icon_size = 80
    illumination = moon_data['illumination']
    
    if illumination > 87:
        moon_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon_full.svg"
    elif illumination > 62:
        moon_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon_3_4.svg"
    elif illumination > 37:
        moon_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon_half.svg"
    else:
        moon_icon_path = BASE_DIR / "assets" / "moon_symbol" / "moon_1_4.svg"
    
    if illumination > 2:
        moon_icon = Image.open(moon_icon_path).convert("RGBA")    
        moon_icon = moon_icon.resize((icon_size, icon_size))
        if moon_data['waxing']:
            moon_icon = ImageOps.mirror(moon_icon)
        image.paste(moon_icon, (x_start, y_start), moon_icon)