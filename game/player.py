from game.constants import *
from game.weapon import *


def player_create():
    # Create sprite
    atlas = atlas_create("resources\\img\\characters.gif")
    sprite = atlas_create_sprite(atlas, vec2_create(6, 90), vec2_create(26, 120))

    # Create Game Object
    player = go_create()
    go_move_to(player, 50, 50)
    go_set_sprite(player, sprite)
    go_set_update_callback(player, _player_update)

    # Set default player attributes
    go_set_attribute(player, "life", PLAYER_DEFAULT_LIFE)

    return player


def _player_update(player, world):
    _player_move(player, world)
    _player_fire(player, world)


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


def _player_fire(player, world):
    input = world_get_input(world)
    if input_key_is_pressed(input, "k"):
        scene = world_get_scene(world)
        bullet = weapon_bullet_create()
        go_move_to(bullet, go_get_position_x(player) + 20, go_get_position_y(player) + 13)
        scene_add_go(scene, bullet, LAYER_NAME_DEFAULT)
