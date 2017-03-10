from engine.function import *


def collision_check(world, go_to_check, layer_name):
    scene = world_get_scene(world)
    layer = scene_get_layer(scene, layer_name)
    sprite = go_get_sprite(go_to_check)
    if not go_is_enable(go_to_check) or sprite == None:
        return None

    # Retrieve game object BBox
    x1 = go_get_position_x(go_to_check)
    y1 = go_get_position_y(go_to_check)
    x2 = x1 + sprite_width(sprite)
    y2 = y1 + sprite_height(sprite)
    for go in layer_get_all_game_objects(layer):
        sprite = go_get_sprite(go)
        if go_is_enable(go) and sprite != None:  # Ignore game object disable or without sprite
            # Retrieve to check game object BBox
            cx1 = go_get_position_x(go)
            cy1 = go_get_position_y(go)
            cx2 = cx1 + sprite_width(sprite)
            cy2 = cy1 + sprite_height(sprite)

            # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
            if x1 < cx2 and x2 > cx1 and y1 < cy2 and y2 > cy1:
                # Collision detected
                return go

    return None
