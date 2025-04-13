import generate_shrine
import generate_shrine_decks
import generate_shrine_deck_object


def run_all(overwrite=True):
    generate_shrine.run(overwrite)
    generate_shrine_decks.run()
    generate_shrine_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
