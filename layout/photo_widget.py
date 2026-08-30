import random
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent


def display_photo(image, x_start, y_start, x_end):
    photo_list = []
    
    # define photo size
    x_size = x_end - x_start
    y_size = int(x_size / 0.75)
    
    # count number of photos
    folder = BASE_DIR / "assets" / "photo"
    photo_count = sum(
        1 for file in folder.iterdir()
        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
    )
    
    # get a list of all photo in a list
    for file in folder.iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
            photo_list.append(file.name)
        
    # get random number between 1 and number of photos
    random_photo_number = random.randint(1, photo_count - 1)
    print(random_photo_number)
    print(photo_list)
    
    photo_path = BASE_DIR / "assets" / "photo" / photo_list[random_photo_number]
    
    picture = Image.open(photo_path).convert("RGBA")
    picture = picture.resize((x_size, y_size))
    
    image.paste(picture, (x_start, y_start) )