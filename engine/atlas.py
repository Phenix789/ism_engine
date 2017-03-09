from tkinter import PhotoImage

from .sprite import Sprite


class Atlas:
    def __init__(self, source):
        self.source = source
        self.photo_image = PhotoImage(file=source)

    def create_sprite(self, pos1, pos2):
        # todo It's magic
        image = PhotoImage()
        image.tk.call(image, 'copy', self.photo_image, '-from', pos1.x, pos1.y, pos2.x, pos2.y, '-to', 0, 0)

        return Sprite(image)
