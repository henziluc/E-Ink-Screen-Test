from PIL import Image
from pathlib import Path

from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large

BASE_DIR = Path(__file__).resolve().parent.parent
path_weather = BASE_DIR / "assets" / "status_symbol" / "partly-cloudy-day.png"
path_transport = BASE_DIR / "assets" / "status_symbol" / "train.png"
path_health = BASE_DIR / "assets" / "status_symbol" / "heart.png"
path_moon = BASE_DIR / "assets" / "status_symbol" / "moon.png"
path_news = BASE_DIR / "assets" / "status_symbol" / "news.png"
path_quote = BASE_DIR / "assets" / "status_symbol" / "quote.png"


def display_software_status(draw, image, x_start, y_start, status_data):
    icon_size = 15
    x = x_start
    
    icon_weather = Image.open(path_weather).convert("RGBA")
    icon_weather = icon_weather.resize((icon_size, icon_size)) 
    
    icon_transport = Image.open(path_transport).convert("RGBA")
    icon_transport = icon_transport.resize((icon_size, icon_size))
    
    icon_health = Image.open(path_health).convert("RGBA")
    icon_health = icon_health.resize((icon_size, icon_size))
    
    icon_moon = Image.open(path_moon).convert("RGBA")
    icon_moon = icon_moon.resize((icon_size, icon_size))
    
    icon_news = Image.open(path_news).convert("RGBA")
    icon_news = icon_news.resize((icon_size, icon_size))
    
    icon_quote = Image.open(path_quote).convert("RGBA")
    icon_quote = icon_quote.resize((icon_size, icon_size))
    