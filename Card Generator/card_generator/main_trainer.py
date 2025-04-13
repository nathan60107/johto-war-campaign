import generate_trainer_cards
import generate_trainer_cards_2


def run_all(overwrite=True):
    generate_trainer_cards.run()
    generate_trainer_cards_2.run()


if __name__ == '__main__':
    run_all(overwrite=True)
