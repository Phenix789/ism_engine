from tkinter import PhotoImage

from engine.function import *


def resources_get_atlas(world, resource):
    collection = world_get_attribute(world, "atlas")
    atlas = object_get(collection, resource)
    if atlas == None:
        atlas = atlas_create(resource)
        object_set(collection, resource, atlas)

    return atlas


def resources_get_sprite(world, resource, x1, y1, x2, y2):
    key = resource + "__" + str(x1) + "x" + str(y1) + "." + str(x2) + "x" + str(y2)
    sprites = world_get_attribute(world, "sprites")
    sprite = object_get(sprites, key)
    if sprite == None:
        atlas = resources_get_atlas(world, resource)
        sprite = atlas_create_sprite(atlas, vec2_create(x1, y1), vec2_create(x2, y2))
        object_set(sprites, key, sprite)

    return sprite


def resources_get_image(world, resource):
    sprites = world_get_attribute(world, "sprites")
    sprite = object_get(sprites, resource)
    if sprite == None:
        image = PhotoImage(file=resource)
        sprite = sprite_create(image)
        object_set(sprites, resource, sprite)

    return sprite
