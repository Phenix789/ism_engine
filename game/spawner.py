from game.enemy import *


def spawner_create(world):
    spawner = go_create()

    go_set_update_callback(spawner, _spawner_update)

    return spawner


def _spawner_update(spawner, world):
    if random.randint(0, 10) == 0:
        enemy = enemy_create(world)
        enemy_pop(world, enemy)
