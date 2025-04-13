import generate_tm_moves
import generate_tm_front
import generate_tm_decks
import generate_tm_deck_object


def run_all(overwrite=True):
    generate_tm_moves.run(overwrite)
    generate_tm_front.run(overwrite)
    generate_tm_decks.run()
    generate_tm_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
