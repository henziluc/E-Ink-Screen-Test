
from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large
import pandas as pd

def display_room_climate_widget(draw, image, x_start, y_start, room_climate_data):
    y = y_start
    graph_height = 150
    
    df = pd.DataFrame(room_climate_data)
    df["time"] = pd.to_datetime(df["time"])
    
    draw.text((x_start, y), "Room Climate", font=font_large, fill=fill_main)
    y += spacing_large
    
    # Draw temperature
    draw.text((x_start, y), "Temperature", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    
    
    y += spacing_small
    
    # Draw Humidity
    draw.text((x_start, y), "Humidity", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    
    y += spacing_small
        
    # Draw CO2
    draw.text((x_start, y), "CO2", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    