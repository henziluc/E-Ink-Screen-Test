import datetime

from .fonts import font_massiv, fill_main
from .helpers import draw_centered_text

def display_welcome(draw, x_start, y_start):
    x_end = 1200 - 2 * x_start
    y_end = font_massiv.size + y_start
    now = datetime.datetime.now()   
    now_hour = now.hour
    
    if 4 <= now_hour < 12:
        text = 'Good Morning'
    elif 12 <= now_hour < 18:
        text = 'Good Afternoon'
    elif 18 <= now_hour < 21:
        text = 'Good Evening'
    else:
        text = 'Good Night'
    
    draw_centered_text(draw, text,(x_start, y_start, x_end, y_end), font_massiv, fill_main)