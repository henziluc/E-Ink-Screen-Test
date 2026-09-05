from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large
import qrcode
from PIL import Image
import random


def display_news_widget(draw, image, x_start, y_start, news_data):
    y = y_start
    
    
    # Draw news title
    draw.text((x_start, y), "News", font=font_large, fill=fill_main)
    y += spacing_large
    
    
    random_news = {
    category: random.choice(articles)
    for category, articles in news_data.items()
}
    
    
    
    # Draw news items
    for item in random_news.values():
        # Draw QR code for the news item
        qr_code_image = generate_qr(item['link'])
        qr_code_image = qr_code_image.resize((70, 70))  # Resize QR code to fit in the widget
        image.paste(qr_code_image, (x_start + 420, y))
        
        
        lines = wrap_text_to_width(
        item["title"],
        font_small,
        max_width=400,
        draw=draw,
        max_lines=3
)       
        for line in lines:
            draw.text((x_start, y), line, font=font_small, fill=fill_main)
            y += spacing_small
            
        y += 20
        
        
        
    


def generate_qr(url):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=2,
        border=1,
    )

    qr.add_data(url)
    qr.make(fit=True)

    return qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGBA")


def wrap_text_to_width(text, font, max_width, draw, max_lines=2):
    """
    Wrap text to fit max_width pixels.
    Returns a list of lines, with a maximum of max_lines.
    If the text is too long, the last line is shortened with '...'.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + (" " if current_line else "") + word

        width = draw.textbbox(
            (0, 0),
            test_line,
            font=font
        )[2]

        if width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)

            current_line = word

            # Maximum number of lines reached
            if len(lines) == max_lines - 1:
                break

    if current_line and len(lines) < max_lines:
        lines.append(current_line)

    # Check if there are words left that weren't displayed
    if len(lines) == max_lines:
        displayed_text = " ".join(lines)

        if len(displayed_text.split()) < len(words):
            last_line = lines[-1]

            while last_line:
                test = last_line.rstrip() + "..."

                width = draw.textbbox(
                    (0, 0),
                    test,
                    font=font
                )[2]

                if width <= max_width:
                    lines[-1] = test
                    break

                last_line = last_line.rsplit(" ", 1)[0]

    return lines

