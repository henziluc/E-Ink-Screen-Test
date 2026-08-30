from PIL import Image
from pathlib import Path

from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large

BASE_DIR = Path(__file__).resolve().parent.parent

def display_health_widget(draw, image, x_start, y_start, health_data):
    y = y_start
    icon_size = 25
    
    # define all icon paths
    step_icon_path = BASE_DIR / "assets" / "sport_symbol" / "shoe-prints.png"
    battery_full_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-full.png"
    battery_three_quarters_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-three-quarters.png"
    battery_half_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-half.png"
    battery_quarter_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-quarter.png"
    battery_empty_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-empty.png"   
    sleep_icon_path = BASE_DIR / "assets" / "sport_symbol" / "bed.png"
    heart_icon_path = BASE_DIR / "assets" / "sport_symbol" / "heart.png"
    
    draw.text((x_start, y), 'Health Stats', font = font_large, fill = fill_main)
    
    y += spacing_large
    
    
    # draw actual steps / target steps    
    step_icon = Image.open(step_icon_path).convert("RGBA")
    step_icon = step_icon.resize((icon_size, icon_size))
    image.paste(step_icon, (x_start, y), step_icon)
    
    actual_steps = str(health_data['steps'])
    target_steps = str(health_data['step_goal'])
    draw.text((x_start + icon_size + 5, y), actual_steps + ' / ' + target_steps, font = font_small, fill = fill_main )
    
    y += spacing_small
    
    # draw body battery
    body_battery = health_data['body_battery']
    
        #choose which battery icon depening on body battery
    if body_battery >= 90:
        battery_icon = Image.open(battery_full_icon_path).convert("RGBA")
    elif body_battery >= 60:
        battery_icon = Image.open(battery_three_quarters_icon_path).convert("RGBA")
    elif body_battery >= 40:
        battery_icon = Image.open(battery_half_icon_path).convert("RGBA")
    elif body_battery >= 10:
        battery_icon = Image.open(battery_quarter_icon_path).convert("RGBA")
    else:       
        battery_icon = Image.open(battery_empty_icon_path).convert("RGBA")
    
    battery_icon = battery_icon.resize((icon_size, icon_size))
    image.paste(battery_icon, (x_start, y), battery_icon)    
    
    draw.text((x_start + icon_size + 5, y), str(body_battery), font = font_small, fill = fill_main )
    
    y += spacing_small
    
    # draw sleep
    sleep_icon = Image.open(sleep_icon_path).convert("RGBA")
    
    sleep_icon = sleep_icon.resize((icon_size, icon_size))
    image.paste(sleep_icon, (x_start, y), sleep_icon)
    
    sleep_hours = str(health_data['sleep_hours'])
    sleep_score = str(health_data['sleep_score'])
    
    draw.text((x_start + icon_size + 5, y), sleep_hours + 'h, ' + sleep_score + 'P' , font = font_small, fill = fill_main )    