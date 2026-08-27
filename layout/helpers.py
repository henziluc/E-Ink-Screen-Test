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


def draw_smooth_curve(draw, points, fill="black", width=3, steps=20):
    """
    Draw a smooth curve through all given points.

    points: list of (x, y) coordinates
    steps: smoothness between each pair of points
    """

    if len(points) < 2:
        return

    curve_points = []

    # Duplicate first and last point for interpolation
    pts = [points[0]] + points + [points[-1]]

    for i in range(1, len(pts) - 2):

        p0 = pts[i - 1]
        p1 = pts[i]
        p2 = pts[i + 1]
        p3 = pts[i + 2]

        for j in range(steps):
            t = j / steps

            t2 = t * t
            t3 = t2 * t

            x = 0.5 * (
                2 * p1[0]
                + (-p0[0] + p2[0]) * t
                + (2*p0[0] - 5*p1[0] + 4*p2[0] - p3[0]) * t2
                + (-p0[0] + 3*p1[0] - 3*p2[0] + p3[0]) * t3
            )

            y = 0.5 * (
                2 * p1[1]
                + (-p0[1] + p2[1]) * t
                + (2*p0[1] - 5*p1[1] + 4*p2[1] - p3[1]) * t2
                + (-p0[1] + 3*p1[1] - 3*p2[1] + p3[1]) * t3
            )

            curve_points.append((x, y))

    curve_points.append(points[-1])

    draw.line(
        curve_points,
        fill=fill,
        width=width
    )
    

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