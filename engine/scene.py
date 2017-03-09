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

    def get_layer(self, layer_name):
        for layer in self.layers:
            if layer.name == layer_name:
                return layer

        return None

    def add_go(self, go, layer_name):
        layer = self.get_layer(layer_name)
        layer.add_game_object(go)

    def update(self, world):
        for layer in self.layers:
            layer.update(world)

    def render(self, world):
        self.canvas.delete('all')  # @see Tk Constants ALL
        for layer in self.layers:
            layer.render(world)

    def draw(self, sprite, position):
        self.canvas.create_image((position.x, position.y), image=sprite.photo_image, anchor='nw')
