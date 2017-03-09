from tkinter import Canvas, Frame

from .input import Input
from .object import Object
from .scene import Scene


class World:
    def __init__(self, tk):
        self.window = tk
        self.tick = 100

        # todo move this logic
        self.frame = Frame(tk)
        self.frame.grid()
        canvas = Canvas(self.frame, width=1000, height=700)
        canvas.pack()

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
