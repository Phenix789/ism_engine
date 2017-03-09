from tkinter import Canvas

from .input import Input
from .object import Object
from .scene import Scene


class World:
    def __init__(self, tk):
        self.window = tk
        self.tick = 100

        # todo move this logic
        canvas = Canvas(tk)
        canvas.pack(fill='both', expand=True)  # Fill all available space

        self.scene = Scene(canvas)
        self.input = Input(tk)
        self.attributes = Object()

    def run(self):
        self._register()

        self.window.mainloop()

    def update(self):
        # Input Update
        self.input.update(self)
        # Game Logic
        self.scene.update(self)
        # Render
        self.scene.render(self)

        self._register()

    def _register(self):
        self.window.after(self.tick, self.update)
