import datetime

from .fonts import font_massiv, fill_main
from .helpers import draw_centered_text

def display_welcome(draw, x_start, y_start):
    x_end = 1200 - 2 * x_start
    y_end = font_massiv.size + y_start
    now = datetime.datetime.now()   
    now_hour = now.hour
    
    if 4 <= now_hour < 11:
        draw_centered_text(draw, 'Good Morning',(x_start, y_start, x_end, y_end), font_massiv, fill_main)
    elif 11 <= now_hour < 18:
        draw_centered_text(draw, 'Good Day',(x_start, y_start, x_end, y_end), font_massiv, fill_main)
    elif 18 <= now_hour < 21:
        draw_centered_text(draw, 'Good Evening',(x_start, y_start, x_end, y_end), font_massiv, fill_main)
    else:
        draw_centered_text(draw, 'Good Night',(x_start, y_start, x_end, y_end), font_massiv, fill_main)
    

    return draw