import random

from engine.function import *
from game.constants import LAYER_NAME_DEFAULT


def enemy_create():
    atlas = atlas_create("resources\\img\\characters.gif")
    sprite = atlas_create_sprite(atlas, vec2_create(197, 126), vec2_create(221, 159))

    enemy = go_create()
    go_set_sprite(enemy, sprite)
    go_set_update_callback(enemy, _enemy_update)

    return enemy


def enemy_pop(world, enemy):
    go_set_position(enemy, vec2_create(500, 500))

    scene = world_get_scene(world)
    scene_add_go(scene, enemy, LAYER_NAME_DEFAULT)


def _enemy_update(enemy, world):
    x = random.randint(-1, 1) * 10
    y = random.randint(-1, 1) * 10

    go_move(enemy, x, y)  # Move random
