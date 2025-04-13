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

    # Card Name (Bolded)
    wrapped_text(d, stats.pokedex_name, bold_font(56), boundaries=(15.5, 1.86), xy=xy(8, 8.15), fill=DARK_COLOUR,
                 anchor='mm', align='center')

    # Image
    type_img = get_img(CARD_ASSETS_DIR / 'card_images' / f'{stats.image_name}.png', xy(15.5, 15.5))
    img.paste(type_img, xy(0.25, 10.71), type_img)

    if stats.state == 5:
        # Quest Info
        wrapped_text(d, stats.quest_info, bold_font(24), boundaries=(15.5, 17.12), xy=xy(8, 18.82), fill=WHITE_COLOUR,
                     anchor='mm', align='left')
    else:
        if stats.state == 4:
            # Quest Info
            wrapped_text(d, stats.quest_info, bold_font(24), boundaries=(15.5, 11.2), xy=xy(8, 15.85), fill=WHITE_COLOUR,
                     anchor='mm', align='left')

            # Objectives
            wrapped_text(d, stats.objectives, bold_font(24), boundaries=(15.5, 3.3), xy=xy(0.25, 23.9), fill=DARK_COLOUR,
                     anchor='lm', align='left')

            # Next State
            wrapped_text(d, stats.next_state, text_font(24), boundaries=(15.5, 1.2), xy=xy(8, 26.775), fill=WHITE_COLOUR,
                     anchor='mm', align='left')
        else:
            # Quest Info
            wrapped_text(d, stats.quest_info, text_font(24), boundaries=(15.5, 11.2), xy=xy(8, 15.85), fill=WHITE_COLOUR,
                     anchor='mm', align='left')

            # Objectives
            wrapped_text(d, stats.objectives, bold_font(24), boundaries=(15.5, 3.3), xy=xy(0.25, 23.9), fill=DARK_COLOUR,
                     anchor='lm', align='left')

            # Next State
            wrapped_text(d, stats.next_state, text_font(24), boundaries=(15.5, 1.2), xy=xy(8, 26.775), fill=WHITE_COLOUR,
                     anchor='mm', align='left')


def add_emblem(img):
    if VANILLA_EMBLEM_PATH.is_file():
        emblem_name = 'vanilla'
    else:
        emblem_name = 'custom'
    emblem_img = get_img(CARD_ASSETS_DIR / 'emblems' / f'{emblem_name}.png', xy(0.5, 0.5))
    img.paste(emblem_img, xy(15, 27.25), emblem_img)

def generate_card_backs(overwrite):
    print('Generating card backs:')
    LEGENDS_CARD_BACKS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = read_cube(sheet_name='legend')
    for _, stats in tqdm(df.iterrows(), total=df.shape[0]):
        output_path = LEGENDS_CARD_BACKS_OUTPUT_DIR / f'{stats.image_name}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = get_img(CARD_ASSETS_DIR / 'card_backs' / 'Legend.png', xy(16, 28))
        img.save(output_path)

#
# Entry
#

def run(overwrite=True):
    print('Generating card fronts:')
    
    df = read_cube(sheet_name='legend')
    for i, stats in tqdm(df.iterrows(), total=df.shape[0]):
        LEGENDS_CARD_FRONTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        output_path = LEGENDS_CARD_FRONTS_OUTPUT_DIR / f'{i}_{stats.image_name.lower()}.png'
        if output_path.is_file() and not overwrite:
            continue

        img = compose_base(stats)

        add_move(img, stats)
        add_emblem(img)

        img.save(output_path)
    generate_card_backs(overwrite)


if __name__ == '__main__':
    run(overwrite=True)
