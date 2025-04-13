import generate_utility
import generate_utility_decks
import generate_utility_deck_object


def run_all(overwrite=True):
    generate_utility.run(overwrite)
    generate_utility_decks.run()
    generate_utility_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
