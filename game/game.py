from tkinter import Tk

from game.gui import *
from game.player import *
from game.spawner import spawner_create


def game_init():
    tk = Tk()
    tk.resizable(width=False, height=False)
    tk.geometry("1000x700+100+100")  # Window size and position

    world = world_create(tk)

    # Atlas/Sprite cache
    world_set_attribute(world, "atlas", object_create())
    world_set_attribute(world, "sprites", object_create())

    return world


def game_layer_create_all(world):
    scene = world_get_scene(world)

    scene_create_layer(scene, LAYER_NAME_VOID, LAYER_LEVEL_VOID)
    scene_create_layer(scene, LAYER_NAME_BACKGROUND, LAYER_LEVEL_BACKGROUND)
    scene_create_layer(scene, LAYER_NAME_ENEMY, LAYER_LEVEL_ENEMY)
    scene_create_layer(scene, LAYER_NAME_PLAYER, LAYER_LEVEL_PLAYER)
    scene_create_layer(scene, LAYER_NAME_ENEMY_BULLET, LAYER_LEVEL_ENEMY_BULLET)
    scene_create_layer(scene, LAYER_NAME_PLAYER_BULLET, LAYER_LEVEL_PLAYER_BULLET)
    scene_create_layer(scene, LAYER_NAME_FOREGROUND, LAYER_LEVEL_FOREGROUND)
    scene_create_layer(scene, LAYER_NAME_GUI, LAYER_LEVEL_GUI)


def game_player_create(world):
    player = player_create(world)

    # Add player to player layer
    scene = world_get_scene(world)
    scene_add_go(scene, player, LAYER_NAME_PLAYER)

    # Add player as world attribute
    world_set_attribute(world, "player", player)

    return player


def game_gui_create(world):
    gui = gui_create(world)

    # Add to gui layer
    scene = world_get_scene(world)
    scene_add_go(scene, gui, LAYER_NAME_GUI)

    # Add gui as world attribute
    world_set_attribute(world, "gui", gui)

    return gui


def game_spawner_create(world):
    spawner = spawner_create(world)

    world_set_attribute(world, "spawner", spawner)

    # Add to void layer
    scene = world_get_scene(world)
    scene_add_go(scene, spawner, LAYER_NAME_VOID)

    return spawner


def game_run(world):
    world_run(world)
