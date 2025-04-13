import generate_legend
import generate_legend_decks
import generate_legend_deck_object


def run_all(overwrite=True):
    generate_legend.run(overwrite)
    generate_legend_decks.run()
    generate_legend_deck_object.run()


if __name__ == '__main__':
    run_all(overwrite=True)
