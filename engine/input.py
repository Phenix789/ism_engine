class Input:
    def __init__(self, tk):
        self.tk = tk
        self.keys = {}

        # tk.bind_all("<Button-1>", self._on_event)
        tk.bind_all("<Key>", self._on_key_pressed)
        tk.bind_all("<KeyRelease>", self._on_key_released)

    def _on_key_pressed(self, event):
        self.keys[event.char] = True

    def _on_key_released(self, event):
        self.keys[event.char] = False

    def update(self, world):
        pass

    def is_pressed(self, key):
        return self.keys.get(key, False)
