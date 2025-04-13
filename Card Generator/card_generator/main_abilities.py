import generate_abilities_moves
import generate_abilities_front
import generate_abilities_decks
import generate_abilities_deck_object


def run_all(overwrite=True):
    generate_abilities_moves.run(overwrite)
    generate_abilities_front.run(overwrite)
    generate_abilities_decks.run()
    generate_abilities_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
