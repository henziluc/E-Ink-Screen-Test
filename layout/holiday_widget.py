import datetime

def display_holiday(draw, df, x_start, y_start, font_large, font_small, fill):
    y = y_start
    spacing = 30
    next_holiday = 1
    now = datetime.datetime.now()
    
    draw.text((x_start, y_start), 'Next Holiday', font=font_large, fill=fill)
    
    y += 70
    
    for _, row in df.iterrows():
        
        delta = row['start_date'] - now
        
        if delta >= datetime.timedelta(0):
            days = delta.days
            if next_holiday == 1:
                draw.text((x_start, y), row['location'], font=font_large, fill=fill)
                y += 60
                draw.text((x_start, y), f"{days} days to go", font=font_small, fill=fill)
                next_holiday = 0
                
            else:
                draw.text((x_start, y), row['location'], font=font_small, fill=fill)
                draw.text((x_start + 120, y), f"{days} days to go", font=font_small, fill=fill)
                
            y += spacing
                            
    return draw