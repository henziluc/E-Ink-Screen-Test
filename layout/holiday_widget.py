import datetime

def display_holiday(draw, df, x_start, y_start, font_large, font_small, fill):
    y = y_start
    now = datetime.datetime.now()
    draw.text(x_start, y_start, 'Next Holiday', font=font_large, fill=fill)
    draw.text(x_start, y_start + 70, 'Location', font=font_small, fill=fill)
    draw.text(x_start + 50, y_start + 70, '15 days to go', font=font_small, fill=fill)
        
    return draw