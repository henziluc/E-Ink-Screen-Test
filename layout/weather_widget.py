import datetime as dt
from .fonts import font_small, font_medium, font_large, fill_main


def display_weather(draw, df_hourly, df_daily, x_start, y_start):
    y = y_start
    spacing = 30
    
    x_weather_code = x_start + 100
    x_min_temp = x_weather_code + 150
    x_max_temp = x_min_temp + 100
    x_wind_speed = x_max_temp + 100
    x_precipitation = x_wind_speed + 100
    x_sunshine = x_precipitation + 100
    
    
    
    
    
    
    draw.text((x_start, y),'Date',font=font_small,fill=fill_main)
    draw.text((x_weather_code, y),'Weather Code',font=font_small,fill=fill_main)
    draw.text((x_min_temp, y),'Min Temp.',font=font_small,fill=fill_main)
    draw.text((x_max_temp, y),'Max Temp.',font=font_small,fill=fill_main)
    draw.text((x_wind_speed, y),'Wind Speed',font=font_small,fill=fill_main)
    draw.text((x_precipitation, y),'Precipitation',font=font_small,fill=fill_main)
    draw.text((x_sunshine, y),'Sunshine Duration',font=font_small,fill=fill_main)
    y += spacing
    
    for _, row in df_daily.iterrows():
        
        weather_code = get_weather_description(row['weather_code'])
        
        draw.text((x_start, y),str(row['date'])[:10],font=font_small,fill=fill_main)
        draw.text((x_weather_code, y),weather_code,font=font_small,fill=fill_main)
        draw.text((x_min_temp, y),str(round(row['temperature_2m_min'],1)),font=font_small,fill=fill_main)
        draw.text((x_max_temp, y),str(round(row['temperature_2m_max'],1)),font=font_small,fill=fill_main)
        draw.text((x_wind_speed, y),str(round(row['wind_speed_10m_max'],1)),font=font_small,fill=fill_main)
        draw.text((x_precipitation, y),str(round(row['precipitation_sum'],1)),font=font_small,fill=fill_main)
        draw.text((x_sunshine, y),str(round(row['sunshine_duration']/3060,1)) + 'h',font=font_small,fill=fill_main)
        
        y += spacing    
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