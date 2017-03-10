import random

from engine.function import *
from game.constants import LAYER_NAME_DEFAULT, RESOURCE_CHARACTERS
from game.resources import resources_get_sprite


def enemy_create(world):
    sprite = resources_get_sprite(world, RESOURCE_CHARACTERS, 197, 126, 221, 159)

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
