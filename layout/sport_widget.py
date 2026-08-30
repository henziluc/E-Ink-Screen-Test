from PIL import Image
from pathlib import Path

from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large

BASE_DIR = Path(__file__).resolve().parent.parent

def display_health_widget(draw, image, x_start, y_start, health_data):
    y = y_start
    icon_size = 25
    
    step_icon_path = BASE_DIR / "assets" / "sport_symbol" / "shoe-prints.png"
    battery_full_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-full.png"
    battery_three_quarters_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery_three-quarters.png"
    battery_half_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-half.png"
    battery_quarter_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-quarter.png"
    battery_empty_icon_path = BASE_DIR / "assets" / "sport_symbol" / "battery-empty.png"   
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
    step_battery = Image.open(battery_full_icon_path).convert("RGBA")
    step_battery = step_battery.resize((icon_size, icon_size))
    image.paste(step_battery, (x_start, y), step_battery)    
    y += spacing_small
    
    step_battery = Image.open(battery_three_quarters_icon_path).convert("RGBA")
    step_battery = step_battery.resize((icon_size, icon_size))
    image.paste(step_battery, (x_start, y), step_battery)    
    y += spacing_small
        
    step_battery = Image.open(battery_half_icon_path).convert("RGBA")
    step_battery = step_battery.resize((icon_size, icon_size))
    image.paste(step_battery, (x_start, y), step_battery)    
    y += spacing_small
            
    step_battery = Image.open(battery_quarter_icon_path).convert("RGBA")
    step_battery = step_battery.resize((icon_size, icon_size))
    image.paste(step_battery, (x_start, y), step_battery)    
    y += spacing_small
                
    step_battery = Image.open(battery_empty_icon_path).convert("RGBA")
    step_battery = step_battery.resize((icon_size, icon_size))
    image.paste(step_battery, (x_start, y), step_battery)    
    y += spacing_small
    # draw sleep
     