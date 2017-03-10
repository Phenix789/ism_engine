from game.constants import *
from game.resources import *


def gui_create(world):
    # Create GameObject
    gui = go_create()

    image = PhotoImage(file=RESOURCE_HEART)
    # Resize - could be better to use a right image without resize
    image = image.zoom(2).subsample(15)
    sprite = sprite_create(image)

    # todo Hack - Put in sprites cache
    sprites = world_get_attribute(world, "sprites")
    object_set(sprites, RESOURCE_HEART + "_resized", sprite)

    go_set_sprite(gui, sprite)
    go_set_render_callback(gui, _gui_render)

    return gui


def _gui_render(gui, world):
    player = world_get_attribute(world, "player")
    life = go_get_attribute(player, "life")

    for i in range(0, life):
        world.scene.draw(gui.sprite, vec2_create(i * 25, 0))
