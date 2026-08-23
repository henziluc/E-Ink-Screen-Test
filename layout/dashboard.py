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
import datetime as dt
import traceback
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
from PIL import Image
import pandas as pd
import json


from .transport_widget import display_schedule
from .weather_widget import display_weather
from .helpers import draw_grid
from .holiday_widget import display_holiday
from assets.holiday_data import holidays

font_large = ImageFont.truetype(
    "fonts/RobotoCondensed-Bold.ttf",
    55
)

font_small = ImageFont.truetype(
    "fonts/RobotoCondensed-Regular.ttf",
    15
)

def make_dashbord(weather_hourly, weather_daily, departures_seen, departures_etzberg):

    epd = epd13in3E.EPD()
    try:
        epd.Init()
        
        image = Image.new("RGB", (1200, 1600), "white")
        draw = ImageDraw.Draw(image)
        
        # Last refresh info
        draw.text((600, 600),"Last refresh: ")
        
        # Title
        draw.text((50, 50), "Next Trains", font=font_large, fill="black")
        

        # Print DataFrame rows
        draw = display_schedule(draw, "Seen", departures_seen, 50, 120, font_small, "black")
        draw = display_schedule(draw, "Etzberg", departures_etzberg, 50 , 270, font_small, "black")
        
        draw = display_weather(draw, weather_hourly, weather_daily, 400, 120, font_small, "black")
        
        draw = display_holiday(draw, holidays, 50, 420, font_large, font_small, "black")
        
        draw = draw_grid(draw, 50, 1600, 1200)
        
        
        
        
        epd.display(epd.getbuffer(image))
        time.sleep(30)

        print("clearing...")
        epd.Clear()

        print("goto sleep...")
        epd.sleep()
        
    except Exception:
        print("ERROR:")
        traceback.print_exc()
        epd.sleep()

    return







