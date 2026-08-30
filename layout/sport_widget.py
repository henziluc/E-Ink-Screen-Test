from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large



def display_health_widget(draw, x_start, y_start):
    y = y_start
    
    draw.text((x_start, y), 'Health Stats', font=font_large, fill=fill_main)
    
    y += spacing_large
     