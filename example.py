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

print("13.3inch e-paper (E) Demo...")

epd = epd13in3E.EPD()
try:
    epd.Init()
    print("clearing...")
    epd.Clear()
    
    # read bmp file 
    print("read bmp 1.file")
    Himage = Image.open(os.path.join(picdir, 'prepared.png'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(10)
    
    print("read bmp 2.file")
    Himage = Image.open(os.path.join(picdir, 'prepared2.png'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(10)

    print("clearing...")
    epd.Clear()

    print("goto sleep...")
    epd.sleep()
except:
    print("goto sleep...")
    epd.sleep()


