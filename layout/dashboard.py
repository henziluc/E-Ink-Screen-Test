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
import datetime
import traceback
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
from PIL import Image
import pandas as pd
import json

from .welcome_widget import display_welcome
from .transport_widget import display_schedule_complet
from .weather_widget import display_weather, display_weather_curve
from .helpers import draw_grid
from .holiday_widget import display_holiday
from assets.holiday_data import holidays
from .fonts import font_small, font_medium, font_large, fill_main


def make_dashbord(weather_hourly, weather_daily, departures_seen, departures_etzberg):

    epd = epd13in3E.EPD()
    try:
        epd.Init()
        
        # Set background to white
        image = Image.new("RGB", (1200, 1600), "white")
        draw = ImageDraw.Draw(image)
        
        # Last refresh info
        now = datetime.datetime.now()
        now_str = str(now.date()) + ' ' + str(now.hour) + ':' + str(now.minute)
        draw.text((30, 1575),"Last refresh: " + str(now), font=font_small,fill=fill_main)
        
        # Draw welcome message
        draw = display_welcome(draw, 30, 30)
        
        # Draw transport schedule
        draw = display_schedule_complet(draw, 'Seen', departures_seen, 'Etzberg', departures_etzberg, 30, 130)
        
        # Draw weather forecast    
        draw = display_weather(draw, weather_hourly, weather_daily, 375, 130)
        
        # Draw weather curve
        draw = display_weather_curve(draw, weather_hourly, weather_daily, 30, 850)
        
        
        
        # Draw next holidays
        draw = display_holiday(draw, holidays, 30, 580)
        
        # Draw helper grid
        # draw = draw_grid(draw, 20, 1600, 1200)
        
        # Write picture on to screen
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
