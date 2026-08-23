import datetime

def display_holiday(draw, df, x_start, y_start, font_large, font_small, fill):
    y = y_start
    now = datetime.datetime.now()
    draw.text((x_start, y_start), 'Next Holiday', font=font_large, fill=fill)
    y += 70
    for _, row in df.iterrows():
        delta = int(row['start_date'] - now)
        if delta >= 0:
            draw.text((x_start, y_start), row['location'], font=font_small, fill=fill)
            draw.text((x_start + 50, y_start ), str(delta) + ' days to go', font=font_small, fill=fill)
            y += 25
    return draw