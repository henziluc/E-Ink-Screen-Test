from PIL import Image
from pathlib import Path

from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large

BASE_DIR = Path(__file__).resolve().parent.parent

def display_health_widget(draw, image, x_start, y_start):
    y = y_start
    
    draw.text((x_start, y), 'Health Stats', font=font_large, fill=fill_main)
    
    y += spacing_large
    
    icon_path = BASE_DIR / "assets" / "sport_symbol" / "shoe-print.png"
        
    icon = Image.open(icon_path).convert("RGBA")
    icon = icon.resize((30, 30))
            
    image.paste(icon, (x_start, y), icon)
     