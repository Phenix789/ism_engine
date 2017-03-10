from tkinter import Tk

from game.enemy import *
from game.gui import *
from game.player import *


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

    scene_create_layer(scene, LAYER_NAME_BACKGROUND, LAYER_LEVEL_BACKGROUND)
    scene_create_layer(scene, LAYER_NAME_DEFAULT, LAYER_LEVEL_DEFAULT)
    scene_create_layer(scene, LAYER_NAME_PLAYER, LAYER_LEVEL_PLAYER)
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


def game_add_enemy(world):
    enemy = enemy_create(world)
    enemy_pop(world, enemy)


def game_run(world):
    world_run(world)
