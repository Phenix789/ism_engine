from engine.function import *
from game.constants import *


def player_create():
    # Create sprite
    atlas = atlas_create("game\\resources\\img\\characters.gif")
    sprite = atlas_create_sprite(atlas, vec2_create(6, 90), vec2_create(26, 120))

    # Create Game Object
    player = go_create()
    go_move_to(player, 50, 50)
    go_set_sprite(player, sprite)
    go_set_update_callback(player, _player_update)

    # Set default player attributes
    go_attribute_set(player, "life", PLAYER_DEFAULT_LIFE)

    return player


def _player_update(player, world):
    _player_move(player, world)


def _player_move(player, world):
    input = world_get_input(world)

    x = 0
    y = 0
    if input_key_is_pressed(input, CONTROLLER_LEFT):
        x += -CONTROLLER_DELTA
    if input_key_is_pressed(input, CONTROLLER_RIGHT):
        x += CONTROLLER_DELTA
    if input_key_is_pressed(input, CONTROLLER_UP):
        y += -CONTROLLER_DELTA
    if input_key_is_pressed(input, CONTROLLER_DOWN):
        y += CONTROLLER_DELTA

    if x != 0 or y != 0:
        go_move(player, x, y)
