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

import json

font_large = ImageFont.truetype(
    "fonts/RobotoCondensed-Bold.ttf",
    60
)

font_small = ImageFont.truetype(
    "fonts/GoogleSans-Regular.ttf",
    30
)


epd = epd13in3E.EPD()
try:
    epd.Init()
    print("clearing...")
    epd.Clear()

    image = Image.new("RGB", (1200, 1600), "white")
    draw = ImageDraw.Draw(image)

    draw.text((50, 50), "Weather", fill="black")
    draw.text((50, 100),"22 °C",font=font_large,fill="black")
    draw.text((50, 150), "Sunny", fill="yellow")
    
    draw.rectangle(
    (100, 50, 150, 100),
    outline="black",
    width=5)
    
    draw.rectangle(
    (200, 50, 250, 100),
    fill="yellow")

    draw.ellipse(
    (300, 50, 350, 100),
    fill="red")
    
    draw.line(
    (400, 50, 450, 100),
    fill="black",
    width=4)
    epd.display(epd.getbuffer(image))

    print("goto sleep...")
    epd.sleep()
except:
    print("goto sleep...")
    epd.sleep()


