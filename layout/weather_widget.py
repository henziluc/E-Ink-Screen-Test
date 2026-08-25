import datetime

from .fonts import font_very_small, font_small, font_medium, font_large, fill_main, spacing_small, spacing_large
from .helpers import draw_centered_text

def display_weather(draw, df_hourly, df_daily, x_start, y_start):
    y = y_start
    
    # Draw widget title
    draw.text((x_start, y), 'Weather Forecast', font=font_large, fill=fill_main)
    y += spacing_large
    
    # Initalize x position of values
    x_weather_code = x_start + 100
    x_min_temp = x_weather_code + 150
    x_max_temp = x_min_temp + 100
    x_wind_speed = x_max_temp + 100
    x_precipitation = x_wind_speed + 100
    x_sunshine = x_precipitation + 100
    
    # Draw the column titels
    draw.text((x_start, y),'Date',font=font_small,fill=fill_main)
    draw.text((x_weather_code, y),'Weather Code',font=font_small,fill=fill_main)
    draw.text((x_min_temp, y),'Min Temp.',font=font_small,fill=fill_main)
    draw.text((x_max_temp, y),'Max Temp.',font=font_small,fill=fill_main)
    draw.text((x_wind_speed, y),'Wind Speed',font=font_small,fill=fill_main)
    draw.text((x_precipitation, y),'Precipitation',font=font_small,fill=fill_main)
    draw.text((x_sunshine, y),'Sunshine Duration',font=font_small,fill=fill_main)
    y += spacing_small
    
    # Draw daily weather data
    for _, row in df_daily.iterrows():
        
        # Get weather description from weather code
        weather_code = get_weather_description(row['weather_code'])
        
        # draw weather data
        draw.text((x_start, y),str(row['date'])[:10],font=font_small,fill=fill_main)
        draw.text((x_weather_code, y),weather_code,font=font_small,fill=fill_main)
        draw.text((x_min_temp, y),str(round(row['temperature_2m_min'],1)),font=font_small,fill=fill_main)
        draw.text((x_max_temp, y),str(round(row['temperature_2m_max'],1)),font=font_small,fill=fill_main)
        draw.text((x_wind_speed, y),str(round(row['wind_speed_10m_max'],1)),font=font_small,fill=fill_main)
        draw.text((x_precipitation, y),str(round(row['precipitation_sum'],1)),font=font_small,fill=fill_main)
        draw.text((x_sunshine, y),str(round(row['sunshine_duration']/3060,1)) + 'h',font=font_small,fill=fill_main)
        y += spacing_small 
           
    return draw



# new function that is on top of the screen and shows the temperatur curve and rain from now for the next 48h.
# Plus daily maximum and minimum temperatur with a weather picture
def display_weather_curve(draw, df_hourly, df_daily, x_start, y_start):
    y = y_start
    graph_hight = 100
    
    now = datetime.datetime.now()
    now_hour = now.hour
        
    # Draw widget title
    draw.text((x_start, y), 'Weather Forecast', font=font_large, fill=fill_main)
    y += spacing_large
    
    hour_spacing = (1200 - x_start * 2) / 48
    
    draw.line([(x_start, y), (1200-x_start, y)], fill= fill_main, width = 0)
    
    
    y += graph_hight
    
    for i in range(0, 49):
        hour = now_hour + i
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
            
            
        draw.line([(x_start + i * hour_spacing, y), (x_start + i * hour_spacing, y - 5)], fill= fill_main, width = 0)
        draw_centered_text(draw, hour + ':00',(x_start + i * hour_spacing - 20, y + 5, x_start + i * hour_spacing + 20, y + 15), font_very_small, fill_main)
    draw.line([(x_start, y), (1200-x_start, y)], fill= fill_main, width = 0)
    
    return draw






def get_weather_description(code):

    weather_codes = {
        0: "Klar",
        1: "Überwiegend klar",
        2: "Teilweise bewölkt",
        3: "Bewölkt",

        45: "Nebel",
        48: "Raureifnebel",

        51: "Leichter Nieselregen",
        53: "Mäßiger Nieselregen",
        55: "Starker Nieselregen",

        56: "Leichter gefrierender Nieselregen",
        57: "Starker gefrierender Nieselregen",

        61: "Leichter Regen",
        63: "Mäßiger Regen",
        65: "Starker Regen",

        66: "Leichter gefrierender Regen",
        67: "Starker gefrierender Regen",

        71: "Leichter Schneefall",
        73: "Mäßiger Schneefall",
        75: "Starker Schneefall",

        77: "Schneekörner",

        80: "Leichte Regenschauer",
        81: "Mäßige Regenschauer",
        82: "Starke Regenschauer",

        85: "Leichte Schneeschauer",
        86: "Starke Schneeschauer",

        95: "Gewitter",
        96: "Gewitter mit leichtem Hagel",
        99: "Gewitter mit starkem Hagel"
    }

    return weather_codes.get(code, "Unbekannt")