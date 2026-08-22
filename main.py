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
    display_schedule(draw, seen_df, 150, font_small, "black")
    display_schedule(draw, etzberg_df, 250, font_small, "black")
    
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
    time.sleep(10)

    print("clearing...")
    epd.Clear()

    print("goto sleep...")
    epd.sleep()
except:
    print("goto sleep...")
    epd.sleep()



def display_schedule(draw, df, y_start, font, fill):
    y = y_start
    for _, row in df.iterrows():
        text = (
            f"{row['departure_time']}  "
            f"{row['route_short_name']}  "
            f"{row['trip_headsign']}  "
            f"+{row['delay']}s"
        )
        draw.text(
            (50, y),
            text,
            font=font,
            fill=fill
        )
        y += 20


def center_text(draw, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]

    x = (1200 - width) // 2

    draw.text((x, y), text, font=font, fill=fill)