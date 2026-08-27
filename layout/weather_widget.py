import datetime
import math

from .fonts import font_very_small, font_small, font_medium, font_large, fill_main, spacing_small, spacing_large
from .helpers import draw_centered_text, draw_smooth_curve

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
    graph_height = 150
    print_hour = 1
    x_day_start = []
    
    now = datetime.datetime.now()
    now_hour = now.hour
        
    # Draw widget title
    draw.text((x_start, y), 'Weather Forecast', font=font_large, fill=fill_main)
    y += spacing_large + spacing_small
    
    # calulate hour spacing on the graph
    hour_spacing = (1200 - x_start * 2) / 48
    
    # draw top horizontal line of the graph
    draw.line([(x_start, y), (1200-x_start, y)], fill= fill_main, width = 0)
    
    #draw vertical line at beginning of graph
    draw.line([(x_start, y),(x_start, y + graph_height)], fill= fill_main, width = 0)
    
    y += graph_height
    
    # draw graph
    for i in range(0, 49):
        hour = now_hour + i
        
        # Reduce hour to 24h format
        if hour > 48:
            hour -= 48
        elif hour > 24:
            hour -= 24
        
        # Add leading zero for hour smaller 10
        if hour < 10:
            hour = '0' + str(hour)       
        else:
            hour = str(hour)
        
        # Draw vertical line where the day ends
        if hour == '24':
            draw.line([(x_start + i * hour_spacing, y),(x_start + i * hour_spacing, y - graph_height)], fill= fill_main, width = 0)
            x_day_start.append(x_start + i * hour_spacing)
        
        draw.line([(x_start + i * hour_spacing, y), (x_start + i * hour_spacing, y - 5)], fill= fill_main, width = 0)
        
        # Draw text at every second hour    
        if  print_hour == 1:
            draw_centered_text(draw, hour + ':00',(x_start + i * hour_spacing - 20, y + 5, x_start + i * hour_spacing + 20, y + 15), font_very_small, fill_main)
            print_hour = 0
        else:
            print_hour = 1
            
    # draw bottom horizontal line of the graph       
    draw.line([(x_start, y), (1200-x_start, y)], fill= fill_main, width = 0)
    
    y -= graph_height + spacing_small
    
    # Draw daily weather overview
    draw = draw_daily_wether_decription(draw, df_daily, x_start, y , x_day_start[0], 0)
    draw = draw_daily_wether_decription(draw, df_daily, x_day_start[0], y , x_day_start[1], 1)
    draw = draw_daily_wether_decription(draw, df_daily, x_day_start[1], y , 1200 - x_start, 2)
    
    y +=  spacing_small
    
    draw = draw_weather_curve(draw, df_hourly, x_start, y, graph_height, hour_spacing, now_hour)
    
    return draw


def draw_daily_wether_decription(draw, df_daily, x_start, y_start, x_end, day):
    x = x_start
    y = y_start
    x_delta = x_end - x_start
    
    
    
    text = str(round(df_daily.loc[day, 'temperature_2m_min'], 1)) + '°C / ' + str(round(df_daily.loc[day, 'temperature_2m_max'], 1)) + '°C'
    
    if x_delta > 200:
        draw_centered_text(draw, text, (x_start, y_start, x_end, y + 20), font_small, fill_main) 
        
    
    return draw


def draw_weather_curve(draw, df_hourly, x_start, y_start, graph_height, hour_spacing, hour):
    offset = 8
    positions = []
    
    # get hourly data from now on
    index = df_hourly[df_hourly['date'].dt.hour == hour].index[0]
    df_from_now = df_hourly.loc[index: index+48]
    df_from_now = df_from_now.reset_index(drop=True) 
    
    # calculate spacing per degree
    temp_min = math.floor(df_from_now['temperature_2m'].min())
    temp_max = math.ceil(df_from_now['temperature_2m'].max())
    temp_delta = math.ceil(temp_max - temp_min)
    degrees_spacing = (graph_height - offset * 2) / temp_delta
    
    # calculate x and y position of every hourly temperature value
    for i in range(0, 49):
        # define X positions of curve
        positions_x = i * hour_spacing + x_start
        
        # define X positions of curve
        temperature = df_from_now.loc[i,'temperature_2m']
        positions_y = (temp_max - temperature) * degrees_spacing + offset + y_start

        positions.append((positions_x, positions_y))
    
    # draw temperature curve    
    draw_smooth_curve(draw, positions, fill_main, 1)
    
    # draw temperature scale
    for i in range(0, temp_delta + 1):
        y = y_start + offset + i * degrees_spacing
        draw.line([(x_start, y),(x_start + 5, y)], fill= fill_main, width = 0)
        temp = str(temp_max - i)
        if i % 2 == 0:
            draw.text((x_start - 2, y), temp, font=font_small, fill=fill_main, anchor= 'rm')
        
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