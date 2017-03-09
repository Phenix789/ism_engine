from .atlas import Atlas
from .game_object import GameObject
from .layer import Layer
from .object import Object
from .scene import Scene
from .vec2 import Vec2
from .world import World


# Atlas


def atlas_create(source):
    return Atlas(source)


def atlas_create_sprite(atlas, pos1, pos2):
    return atlas.create_sprite(pos1, pos2)


# GameObject


def go_create():
    return GameObject()


def go_enable(go):
    go.enable = True


def go_disable(go):
    go.enable = False


def go_set_position(go, position):
    go.position = position


def go_get_position(go):
    return go.position


def go_set_position_x(go, x):
    go.position.x = x


def go_get_position_x(go):
    return go.position.x


def go_set_position_y(go, y):
    go.position.y = y


def go_get_position_y(go):
    return go.position.y


def go_set_sprite(go, sprite):
    go.sprite = sprite


def go_get_sprite(go):
    return go.sprite


def go_object_set(go, key, value):
    go.object.data[key] = value


def go_object_get(go, key):
    return go.object.data.get(key)


def go_set_update_callback(go, callback):
    go.update_callback = callback


# Layer


def layer_create(name, level):
    return Layer(name, level)


def layer_add_game_object(layer, go):
    layer.add_game_object(go)


def layer_remove_game_object(layer, go):
    layer.remove_game_object(go)


# Object


def object_create():
    return Object()


def object_set(object, key, value):
    object.data[key] = value


def object_get(object, key):
    return object.data.get(key)


# Scene


def scene_create(canvas):
    return Scene(canvas)


def scene_create_layer(scene, name, level):
    return scene.create_layer(name, level)


def scene_add_layer(scene, layer):
    scene.add_layer(layer)


# Vec2


def vec2_create(x=0, y=0):
    return Vec2(x, y)


def vec2_set_x(vec, value):
    vec.x = value


def vec2_get_x(vec):
    return vec.x


def vec2_set_y(vec, value):
    vec.y = value


def vec2_get_y(vec):
    return vec.y


# World


def world_create(tk):
    return World(tk)


def world_get_input(world):
    return world.input


def world_get_scene(world):
    return world.scene


def world_run(world):
    world.run()
