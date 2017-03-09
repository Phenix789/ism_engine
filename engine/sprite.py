class Sprite:
    def __init__(self, photo_image):
        self.photo_image = photo_image

    def width(self):
        return self.photo_image.width()

    def height(self):
        return self.photo_image.height()
