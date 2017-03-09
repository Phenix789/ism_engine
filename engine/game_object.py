from .object import Object
from .vec2 import Vec2


class GameObject:
    def __init__(self):
        self.enable = True
        self.position = Vec2()
        self.sprite = None
        self.object = Object()

        self.update_callback = None

    def update(self, world):
        if self.enable and self.update_callback:
            self.update_callback(self, world)

    def render(self, world):
        if self.enable and self.sprite:
            world.scene.draw(self.sprite, self.position)
