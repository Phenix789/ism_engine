from game.constants import *
from game.resources import *


def weapon_bullet_create(world):
    sprite = resources_get_sprite(world, RESOURCE_CHARACTERS, 288, 41, 297, 47)

    bullet = go_create()
    go_set_sprite(bullet, sprite)
    go_set_update_callback(bullet, _weapon_bullet_update)

    go_set_attribute(bullet, "lifetime", 20)

    return bullet


def weapon_player_fire(world, player):
    scene = world_get_scene(world)
    bullet = weapon_bullet_create(world)
    go_set_attribute(bullet, "layer", LAYER_NAME_PLAYER_BULLET)
    go_set_attribute(bullet, "velocity_x", 20)
    go_move_to(bullet, go_get_position_x(player) + 20, go_get_position_y(player) + 13)
    scene_add_go(scene, bullet, LAYER_NAME_PLAYER_BULLET)


def weapon_enemy_fire(world, enemy):
    scene = world_get_scene(world)
    bullet = weapon_bullet_create(world)
    go_set_attribute(bullet, "layer", LAYER_NAME_ENEMY_BULLET)
    go_set_attribute(bullet, "velocity_x", -20)
    go_move_to(bullet, go_get_position_x(enemy) - 20, go_get_position_y(enemy) + 13)
    scene_add_go(scene, bullet, LAYER_NAME_ENEMY_BULLET)


def _weapon_bullet_update(bullet, world):
    lifetime = go_get_attribute(bullet, "lifetime")
    if lifetime == 0:
        layer = go_get_attribute(bullet, "layer")
        scene = world_get_scene(world)
        layer = scene_get_layer(scene, layer)
        layer_remove_game_object(layer, bullet)
    else:
        x = go_get_attribute(bullet, "velocity_x")
        go_move(bullet, x, 0)
        go_set_attribute(bullet, "lifetime", lifetime - 1)
