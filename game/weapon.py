from engine.function import *
from game.constants import LAYER_NAME_DEFAULT


def weapon_bullet_create():
    atlas = atlas_create("resources\\img\\characters.gif")
    sprite = atlas_create_sprite(atlas, vec2_create(288, 41), vec2_create(297, 47))

    bullet = go_create()
    go_set_sprite(bullet, sprite)
    go_set_update_callback(bullet, _weapon_bullet_update)

    go_set_attribute(bullet, "lifetime", 20)

    return bullet


def _weapon_bullet_update(bullet, world):
    lifetime = go_get_attribute(bullet, "lifetime")
    if lifetime == 0:
        scene = world_get_scene(world)
        layer = scene_get_layer(scene, LAYER_NAME_DEFAULT)
        layer_remove_game_object(layer, bullet)
    else:
        go_move(bullet, 20, 0)
        go_set_attribute(bullet, "lifetime", lifetime - 1)
