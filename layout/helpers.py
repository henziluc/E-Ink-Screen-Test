from PIL import ImageFont

def draw_grid(draw, spacing, height, width):
    i = 1
    #horizontal lines
    while i * spacing < height:
        draw.line((0, i * spacing, width, i * spacing),fill="black",width=1)
        i += 1
    
    i = 1  
    #vertical lines
    while i * spacing < width:
            draw.line((i * spacing, 0, i * spacing, height),fill="black",width=1)
            i += 1
    
    return draw


def draw_centered_text(draw, text, box, font, fill):

    x_start, y_start, x_end, y_end = box

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = x_start + (x_end - x_start - text_width) // 2
    y = y_start + (y_end - y_start - text_height) // 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill
    )
    
    
def draw_centered_text_auto_size(draw, text, box, font, fill, min_size=10):

    x_start, y_start, x_end, y_end = box

    size = font.size

    while size >= min_size:

        current_font = ImageFont.truetype(
            "../fonts/RobotoCondensed-Regular.ttf",
            size
        )

        bbox = draw.textbbox(
            (0, 0),
            text,
            font=current_font
        )

        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        if text_width <= (x_end - x_start):
            break

        size -= 1

    x = x_start + ((x_end - x_start) - text_width) // 2
    y = y_start + ((y_end - y_start) - text_height) // 2

    draw.text(
        (x, y),
        text,
        font=current_font,
        fill=fill
    )