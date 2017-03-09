class Layer:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.objects = []

    def add_game_object(self, go):
        self.objects.append(go)

    def remove_game_object(self, go):
        self.objects.remove(go)

    def update(self, world):
        for go in self.objects:
            go.update(world)

    def render(self, world):
        for go in self.objects:
            go.render(world)
