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
    card_base = ''
    base_img = get_img(CARD_ASSETS_DIR / 'tactic_bases' / f'{stats.trainer}.png', xy(16, 22.88))
    return base_img

def add_move(img, stats):
    move_img = get_img(TACTICS_MOVES_OUTPUT_DIR / f'{stats.move_name}.png', xy(14.5, 7.5))
    img.paste(move_img, xy(0.75, 5.71), move_img)

def add_move2(img, stats):
    move_img = get_img(TACTICS_MOVES_OUTPUT_DIR / f'{stats.ability_name}.png', xy(14.5, 7.5))
    img.paste(move_img, xy(0.75, 14.61), move_img)

def add_button(img, stats):
    move_img = get_img(CARD_ASSETS_DIR / 'tactic_bases' / f'{stats.trainer}_button.png', xy(2.03, 2.03))
    img.paste(move_img, xy(6.985, 12.88), move_img)

#
# Entry
#

def run(overwrite=False):
    print('Generating card fronts:')
    TACTICS_CARD_FRONTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = read_cube(sheet_name='tactics')
    for i, stats in tqdm(df.iterrows(), total=df.shape[0]):
        output_path = TACTICS_CARD_FRONTS_OUTPUT_DIR / f'{i}_{stats.tactic_name}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = compose_base(stats)

        # img = Image.new('RGBA', xy(16, 28))
        add_move(img, stats)
        add_move2(img, stats)
        add_button(img, stats)

        # base_img.paste(img, xy(0, 0), img)
        img.save(output_path)


if __name__ == '__main__':
    run(overwrite=True)
