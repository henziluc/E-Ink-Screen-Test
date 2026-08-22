import datetime as dt



def display_weather(draw, df_hourly, df_daily, x_start, y_start, font, fill):
    y = y_start
    spacing = 25
    draw.text((x_start, y),'Date',font=font,fill=fill)
    draw.text((x_start + 100, y),'Weather Code',font=font,fill=fill)
    draw.text((x_start + 200, y),'Min Temperature',font=font,fill=fill)
    draw.text((x_start + 300, y),'Max Temperature ',font=font,fill=fill)
    draw.text((x_start + 400, y),'Max Wind Speed',font=font,fill=fill)
    draw.text((x_start + 500, y),'Precipitation',font=font,fill=fill)
    draw.text((x_start + 600, y),'Sunshine Duration',font=font,fill=fill)
    y += spacing
    
    for _, row in df_daily.iterrows():
        
        weather_code = get_weather_description(row['weather_code'])
        
        draw.text((x_start, y),str(row['date'])[:10],font=font,fill=fill)
        draw.text((x_start + 100, y),weather_code,font=font,fill=fill)
        draw.text((x_start + 200, y),str(row['temperature_2m_min']),font=font,fill=fill)
        draw.text((x_start + 300, y),str(row['temperature_2m_max']),font=font,fill=fill)
        draw.text((x_start + 400, y),str(row['wind_speed_10m_max']),font=font,fill=fill)
        draw.text((x_start + 500, y),str(row['precipitation_sum']),font=font,fill=fill)
        draw.text((x_start + 600, y),str(row['sunshine_duration']),font=font,fill=fill)
        
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