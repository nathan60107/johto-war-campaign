import generate_tactics
import generate_tactics_moves
import generate_tactics_decks
import generate_tactics_deck_object


def run_all(overwrite=True):
    generate_tactics_moves.run(overwrite)
    generate_tactics.run()
    generate_tactics_decks.run()
    generate_tactics_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
