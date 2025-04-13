import generate_pokemon_moves
import generate_pokemon_front
import generate_pokemon_decks
import generate_pokemon_deck_object


def run_all(overwrite=True):
    generate_pokemon_moves.run(overwrite)
    generate_pokemon_front.run(overwrite)
    generate_pokemon_decks.run()
    generate_pokemon_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
