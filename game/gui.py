from tkinter import *

from engine.function import *


def gui_create():
    # Create GameObject
    gui = go_create()

    image = PhotoImage(file="resources\\img\\heart.png")
    # Resize - could be better to use a right image without resize
    image = image.zoom(2).subsample(15)
    sprite = sprite_create(image)
    go_set_sprite(gui, sprite)
    go_set_render_callback(gui, _gui_render)

    return gui


def _gui_render(gui, world):
    player = world_attribute_get(world, "player")
    life = go_attribute_get(player, "life")

    for i in range(0, life):
        world.scene.draw(gui.sprite, vec2_create(i * 25, 0))
