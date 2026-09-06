
from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large


def display_quote_widget(draw, x_start, y_start, quote_data):
    y = y_start
    # Draw quote data
    for quote in quote_data:
        draw.text((x_start, y), quote['title'], font=font_medium, fill=fill_main)
        y += spacing_normal
        draw.text((x_start, y), quote['description'], font=font_small, fill=fill_main)
        y += spacing_large