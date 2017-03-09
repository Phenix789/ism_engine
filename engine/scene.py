from .layer import Layer


class Scene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.layers = []

    def create_layer(self, name, level):
        layer = Layer(name, level)
        self.add_layer(layer)

        return layer

    def add_layer(self, layer):
        self.layers.append(layer)
        self.layers.sort(key=lambda layer: layer.level)

    def update(self, world):
        for layer in self.layers:
            layer.update(world)

    def render(self, world):
        self.canvas.delete('all')
        for layer in self.layers:
            layer.render(world)

    def draw(self, sprite, position):
        self.canvas.create_image((position.x, position.y), image=sprite.photo_image)
