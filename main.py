#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = "picdir/"
libdir = "e_ink_lib"
if os.path.exists(libdir):
    sys.path.append(libdir)

import epd13in3E
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
from PIL import Image
import pandas as pd
import json

def display_schedule(draw, df, x_start, y_start, font, fill):
    y = y_start
    for _, row in df.iterrows():
        if row['route_short_name'] == "3":
            fill_route_short_name = "green"
        elif row['route_short_name'] in ["S11", "S26"]:
            fill_route_short_name = "black"
        else:
            fill_route_short_name = "black"
        draw.text((x_start, y),row['route_short_name'],font=font_small,fill=fill_route_short_name)
        
        headsign = row["trip_headsign"].replace("Winterthur, ", "")
        draw.text((x_start + 30, y),headsign ,font=font_small,fill=fill) 
        
        delay = round(int(row['delay'])/60)
        if delay > 1:
            draw.text((x_start + 150, y),f"+{delay}min",font=font_small,fill="red") 
            
        draw.text((x_start + 250, y),row['departure_time'][:-3],font=font_small,fill=fill)
      
        y += 20
    return draw



font_large = ImageFont.truetype(
    "fonts/RobotoCondensed-Bold.ttf",
    60
)

font_small = ImageFont.truetype(
    "fonts/GoogleSans-Regular.ttf",
    15
)

from test_data import (
    hourly_weather_df,
    daily_weather_df,
    seen_df,
    etzberg_df,
)

epd = epd13in3E.EPD()
try:
    epd.Init()
    print("clearing...")
    epd.Clear()

    image = Image.new("RGB", (1200, 1600), "white")
    draw = ImageDraw.Draw(image)

    # Title
    draw.text(
        (50, 50),
        "Next Trains",
        font=font_large,
        fill="black"
    )

    # Print DataFrame rows
    draw = display_schedule(draw, seen_df, 50, 150, font_small, "black")
    draw = display_schedule(draw, etzberg_df,50 , 250, font_small, "black")
    
    draw.rectangle(
    (20, 20, 1180, 1580),
    outline="black",
    width=5)
    
    draw.rectangle(
    (500, 700, 700, 900),
    fill="yellow")

    draw.ellipse(
    (500, 700, 700, 900),
    fill="red")
    
    draw.line(
    (500, 700, 700, 900),
    fill="black",
    width=4)
    draw.line(
    (500, 900, 700, 700),
    fill="black",
    width=4)
    
    
    epd.display(epd.getbuffer(image))
    time.sleep(20)

    print("clearing...")
    epd.Clear()

    print("goto sleep...")
    epd.sleep()
except:
    print("goto sleep...")
    epd.sleep()








