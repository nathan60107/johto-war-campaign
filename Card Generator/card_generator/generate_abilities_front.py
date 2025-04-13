from io import BytesIO

import pandas as pd
import requests
from PIL import ImageDraw
from tqdm import tqdm

from config import *
from utils import xy, read_cube, get_img, text_font, title_font, wrapped_text

#
# Base
#

def compose_base(stats):
    card_base = 'ability'
    base_img = get_img(CARD_ASSETS_DIR / 'card_bases' / f'{card_base}.png', xy(16, 28))
    return base_img

def add_move(img, stats):
    move_img = get_img(ABILITY_MOVES_OUTPUT_DIR / f'{stats.ability_name}.png', xy(14.5, 7.5))
    img.paste(move_img, xy(0.75, 19.75), move_img)

def add_emblem(img):
    if VANILLA_EMBLEM_PATH.is_file():
        emblem_name = 'vanilla'
    else:
        emblem_name = 'custom'
    emblem_img = get_img(CARD_ASSETS_DIR / 'emblems' / f'{emblem_name}.png', xy(0.5, 0.5))
    img.paste(emblem_img, xy(15, 27), emblem_img)

#
# Entry
#

def run(overwrite=False):
    print('Generating card fronts:')
    ABILITY_CARD_FRONTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = read_cube(sheet_name='abilities')
    for i, stats in tqdm(df.iterrows(), total=df.shape[0]):
        output_path = ABILITY_CARD_FRONTS_OUTPUT_DIR / f'{i}_{stats.ability_name.lower()}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = compose_base(stats)

        # img = Image.new('RGBA', xy(16, 28))
        add_move(img, stats)
        add_emblem(img)

        # base_img.paste(img, xy(0, 0), img)
        img.save(output_path)


if __name__ == '__main__':
    run(overwrite=True)
