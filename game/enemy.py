import random

from collision import *
from game.weapon import *


def enemy_create(world):
    sprite = resources_get_sprite(world, RESOURCE_CHARACTERS, 197, 126, 221, 159)

    enemy = go_create()
    go_set_sprite(enemy, sprite)
    go_set_update_callback(enemy, _enemy_update)

    return enemy


def enemy_pop(world, enemy):
    go_set_position(enemy, vec2_create(500, 500))

    scene = world_get_scene(world)
    scene_add_go(scene, enemy, LAYER_NAME_ENEMY)


def _enemy_update(enemy, world):
    x = random.randint(-1, 1) * 10
    y = random.randint(-1, 1) * 10

    if x == 0 and y == 0:
        weapon_enemy_fire(world, enemy)
    else:
        go_move(enemy, x, y)  # Move random

    bullet = collision_check(world, enemy, LAYER_NAME_PLAYER_BULLET)
    if bullet:
        weapon_bullet_hit(world, bullet, enemy)
        score = world_get_attribute(world, "score") + 1  # Increase score by 1
        world_set_attribute(world, "score", score)

        # Remove enemy
        scene = world_get_scene(world)
        layer = scene_get_layer(scene, LAYER_NAME_ENEMY)
        layer_remove_game_object(layer, enemy)
