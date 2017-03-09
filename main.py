from game.game import *


def main():
    game = game_init()
    game_layer_create_all(game)
    game_player_create(game)
    game_gui_create(game)

    game_run(game)


if __name__ == '__main__':
    main()
