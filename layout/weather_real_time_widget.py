from PIL import Image
from pathlib import Path

from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large

BASE_DIR = Path(__file__).resolve().parent.parent
path_humidity = BASE_DIR / "assets" / "weather_symbol" / "humidity.png"
path_wind = BASE_DIR / "assets" / "weather_symbol" / "windsock.png"
path_temperature = BASE_DIR / "assets" / "weather_symbol" / "thermometer.png"

def display_real_time_weather(draw, image, x_start, y_start, real_time_weather_data):
    y = y_start
    x = x_start
    icon_size = 20
    
    icon_temperature = Image.open(path_temperature).convert("RGBA")
    icon_temperature = icon_temperature.resize((icon_size, icon_size))
    
    icon_wind = Image.open(path_wind).convert("RGBA")
    icon_wind = icon_wind.resize((icon_size, icon_size))
    
    icon_humidity = Image.open(path_humidity).convert("RGBA")
    icon_humidity = icon_humidity.resize((icon_size, icon_size))

    draw.text((x, y), "Inside", font=font_medium, fill=fill_main)
    y += spacing_medium
    
    image.paste(icon_temperature, (x, y), icon_temperature)
    draw.text((x + icon_size + 5, y), f"{real_time_weather_data['temperature_inside']} °C", font=font_small, fill=fill_main)
    y += spacing_small
    
    image.paste(icon_humidity, (x, y), icon_humidity)
    draw.text((x + icon_size + 5, y), f"{real_time_weather_data['humidity_inside']} %", font=font_small, fill=fill_main)
    y += spacing_small

    x += 160
    y = y_start
    
    draw.text((x, y), "Outside", font=font_medium, fill=fill_main)    
    y += spacing_medium
    
    image.paste(icon_temperature, (x, y), icon_temperature)
    draw.text((x + icon_size + 5, y), f"{real_time_weather_data['temperature_outside']} °C", font=font_small, fill=fill_main)
    y += spacing_small
    
    image.paste(icon_humidity, (x, y), icon_humidity)
    draw.text((x + icon_size + 5, y), f"{real_time_weather_data['humidity_outside']} %", font=font_small, fill=fill_main)
    y += spacing_small
    
    image.paste(icon_wind, (x, y), icon_wind)
    draw.text((x + icon_size + 5, y), f"{real_time_weather_data['wind_speed_outside']} m/s", font=font_small, fill=fill_main)