from game.collision import *
from game.weapon import *


def player_create(world):
    # Retrieve sprite
    sprite = resources_get_sprite(world, RESOURCE_CHARACTERS, 6, 90, 26, 120)

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
    _player_collision(player, world)


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
        weapon_player_fire(world, player)


def _player_collision(player, world):
    bullet = collision_check(world, player, LAYER_NAME_ENEMY_BULLET)
    if bullet:
        weapon_bullet_hit(world, bullet, player)
        life = go_get_attribute(player, "life") - 1
        if life == 0:
            # Player dead, end game
            pass

        go_set_attribute(player, "life", life)
