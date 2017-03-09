from engine.function import *
from game.constants import *


def gui_create():
    # Create GameObject
    gui = go_create()
    go_set_update_callback(gui, _gui_update)

    return gui


def _gui_update(gui, world):
    player = world_attribute_get(world, "player")
    life = go_attribute_get(player, "life")

    world.scene.canvas.create_rectangle(50, 50, life * 4, 200, fill=GUI_LIFE_COLOR)
    world.scene.canvas.create_text((50, 50), text=str(life))
