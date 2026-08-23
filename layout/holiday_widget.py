import datetime

def display_holiday(draw, df, x_start, y_start, font_large, font_small, fill):
    y = y_start
    spacing = 30
    
    now = datetime.datetime.now()
    
    draw.text((x_start, y_start), 'Next Holiday', font=font_large, fill=fill)
    
    y += 70
    
    for _, row in df.iterrows():
        
        delta = row['start_date'] - now
        
        if delta >= datetime.timedelta(0):
            days = delta.days
            draw.text((x_start, y), row['location'], font=font_small, fill=fill)
            draw.text((x_start + 100, y), f"{days} days to go", font=font_small, fill=fill)
            y += spacing
            
    return draw