from tkinter import *

from engine.function import *


def main_go_update(go, world):
    position = go_get_position(go)
    vec2_set_x(position, vec2_get_x(position) + 10)


tk = Tk()
world = world_create(tk)

atlas = atlas_create("game\\resources\\img\\characters.gif")
sprite = atlas_create_sprite(atlas, vec2_create(6, 90), vec2_create(26, 120))

go = go_create()
go_set_position(go, vec2_create(50, 50))
go_set_sprite(go, sprite)
go_set_update_callback(go, main_go_update)

scene = world_get_scene(world)
layer = scene_create_layer(scene, "default", 1)
layer_add_game_object(layer, go)

world.run()
