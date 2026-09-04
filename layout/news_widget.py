from .fonts import font_small, font_normal, font_medium, font_large, fill_main, spacing_small, spacing_normal, spacing_medium, spacing_large
import qrcode
from PIL import Image


def display_news_widget(draw, image, x_start, y_start, news_data):
    y = y_start
    
    
    # Draw news title
    draw.text((x_start, y), "News", font=font_large, fill=fill_main)
    y += spacing_large
    
    # Draw news items
    for item in news_data['items']:
        draw.text((x_start, y), item['title'], font=font_medium, fill=fill_main)
        y += spacing_normal
        
        # Draw QR code for the news item
        image.paste(generate_qr(item['url']), (x_start + 600, y - spacing_normal))
        
        y += spacing_large
    


def generate_qr(url):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=6,
        border=2,
    )

    qr.add_data(url)
    qr.make(fit=True)

    return qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGBA")




