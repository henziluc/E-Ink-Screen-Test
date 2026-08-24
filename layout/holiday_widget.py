import datetime
from .helpers import draw_centered_text
from .fonts import font_small, font_medium, font_large, fill_main

def display_holiday(draw, df, x_start, y_start):
    y = y_start
    spacing = 30
    next_holiday = 1
    now = datetime.datetime.now()
    
    draw.text((x_start, y_start), 'Next Holiday', font=font_large, fill=fill_main)
    
    y += 60
    
    for _, row in df.iterrows():
        
        delta = row['start_date'] - now
        
        if delta >= datetime.timedelta(0):
            days = delta.days
            if next_holiday == 1:
                draw_centered_text(draw, row['location'], (x_start , y, x_start + 280, y + 27), font_large, fill_main)
                y += 60
                draw_centered_text(draw,)
                draw.text((x_start, y, x_start + 280, y + 15), f"{days} days to go", font=font_medium, fill=fill_main)
                next_holiday = 0
                y += 40
                
            else:
                draw.text((x_start, y), row['location'], font=font_small, fill=fill_main)
                draw.text((x_start + 120, y), f"{days} days to go", font=font_small, fill=fill_main)
                
            y += spacing
                            
    return draw