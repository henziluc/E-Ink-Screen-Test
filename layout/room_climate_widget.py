
from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large
import pandas as pd

def display_room_climate_widget(draw, image, x_start, y_start, room_climate_data):
    y = y_start
    graph_height = 100
    graph_width = 1200 - x_start - 30  # Adjust the width based on your layout
    
    df = pd.DataFrame(room_climate_data)
    df["time"] = pd.to_datetime(df["time"])
    
    draw.text((x_start, y), "Room Climate", font=font_large, fill=fill_main)
    y += spacing_large
    
    # Draw temperature
    draw.text((x_start, y), "Temperature", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    draw.line((x_start, y, x_start + graph_width, y), fill=fill_main, width=2)
    draw_room_climate_graph(draw, x_start, y - graph_height, graph_width, graph_height, room_climate_data, "temperature", fill_main)
    
    y += spacing_small
    
    # Draw Humidity
    draw.text((x_start, y), "Humidity", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    draw.line((x_start, y, x_start + graph_width, y), fill=fill_main, width=2)
    draw_room_climate_graph(draw, x_start, y - graph_height, graph_width, graph_height, room_climate_data, "humidity", fill_main)
    y += spacing_small
        
    # Draw CO2
    draw.text((x_start, y), "CO2", font=font_normal, fill=fill_main)
    y += spacing_normal + graph_height
    
    draw.line((x_start, y, x_start, y - graph_height), fill=fill_main, width=2)
    draw.line((x_start, y, x_start + graph_width, y), fill=fill_main, width=2)
    draw_room_climate_graph(draw, x_start, y - graph_height, graph_width, graph_height, room_climate_data, "co2", fill_main)
    
    
    
    
def draw_room_climate_graph(draw, x_start, y_start, graph_width, graph_height, data, value_key, color):
    if len(data) < 2:
        return  # Not enough data to draw a graph
    
    min_value = min(data[value_key])
    max_value = max(data[value_key])
    
    if min_value == max_value:
        return  # Avoid division by zero
    
    # Normalize the data to fit within the graph height
    normalized_data = [(value - min_value) / (max_value - min_value) for value in data[value_key]]
    
    # Draw the graph line
    for i in range(1, len(normalized_data)):
        x1 = x_start + (i - 1) * (graph_width / (len(normalized_data) - 1))
        y1 = y_start - normalized_data[i - 1] * graph_height
        x2 = x_start + i * (graph_width / (len(normalized_data) - 1))
        y2 = y_start - normalized_data[i] * graph_height
        
        draw.line((x1, y1, x2, y2), fill=color, width=2)    