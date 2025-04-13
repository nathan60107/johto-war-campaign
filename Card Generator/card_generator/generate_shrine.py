from io import BytesIO

import pandas as pd
import requests
from PIL import ImageDraw
from tqdm import tqdm

from config import *
from utils import xy, read_cube, get_img, text_font, title_font, bold_font, wrapped_text


#
# Base
#

def compose_base(stats):
    base_img = get_img(CARD_ASSETS_DIR / 'card_bases' / f'{stats.image_type}.png', xy(16, 28))
    return base_img

def add_move(img, stats):
    d = ImageDraw.Draw(img)

    # Determine fill color based on image_type
    fill_color = WHITE_COLOUR if stats.image_type == "Warp" else DARK_COLOUR
  
    # Card Name
    d.text(xy(8, 21), str(stats.internal_name), fill=fill_color, font=text_font(36), anchor='mm')
     
    # Effect
    wrapped_text(d, stats.card_effect, text_font(28), boundaries=(13.82, 5.06), xy=xy(8, 24.44), fill=fill_color,
                 anchor='mm', align='center')
    

def add_emblem(img):
    if VANILLA_EMBLEM_PATH.is_file():
        emblem_name = 'vanilla'
    else:
        emblem_name = 'custom'
    emblem_img = get_img(CARD_ASSETS_DIR / 'emblems' / f'{emblem_name}.png', xy(0.5, 0.5))
    img.paste(emblem_img, xy(15, 27), emblem_img)

def generate_card_backs(overwrite):
    print('Generating card backs:')
    SHRINE_CARD_BACKS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = read_cube(sheet_name='shrine')
    for _, stats in tqdm(df.iterrows(), total=df.shape[0]):
        output_path = SHRINE_CARD_BACKS_OUTPUT_DIR / f'{stats.utility_name}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = get_img(CARD_ASSETS_DIR / 'card_backs' / 'Shrine.png', xy(16, 28))
        img.save(output_path)

#
# Entry
#

def run(overwrite=True):
    print('Generating card fronts:')
    
    df = read_cube(sheet_name='shrine')
    for i, stats in tqdm(df.iterrows(), total=df.shape[0]):
        directory_name = stats.image_type if stats.image_type != "Warp" else "Shrine"
        output_dir = (OUTPUT_DIR / directory_name / 'card_fronts')
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f'{i}_{stats.utility_name.lower()}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = compose_base(stats)

        add_move(img, stats)
        add_emblem(img)

        img.save(output_path)
    generate_card_backs(overwrite)


if __name__ == '__main__':
    run(overwrite=True)
