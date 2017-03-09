from .object import Object
from .vec2 import Vec2


class GameObject:
    def __init__(self):
        self.enable = True
        self.position = Vec2()
        self.sprite = None
        self.attributes = Object()

        self.update_callback = None

    def move(self, x, y):
        self.position.x += x
        self.position.y += y

    def move_to(self, x, y):
        self.position.x = x
        self.position.y = y

    def update(self, world):
        if self.enable and self.update_callback:
            self.update_callback(self, world)

    def render(self, world):
        if self.enable and self.sprite:
            world.scene.draw(self.sprite, self.position)
