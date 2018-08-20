import random

class Comet:

    def __init__(self, display_width, display_height, orientation):
        self.orientation = orientation
        self.display_width = display_width
        self.display_height = display_height

        if orientation == "left":
            x = -60
            y = random.randint(-60, 600)
        elif orientation == "top":
            x = random.randint(-60, 800)
            y = -60
        elif orientation == "right":
            x = 860
            y = random.randint(-60, 600)
        elif orientation == "bottom":
            x = random.randint(-60, 800)
            y = 660

        self.x = x
        self.y = y

    def move(self):
        speed = 5
        offset = 100
        if self.orientation == "left":
            self.x += speed
        elif self.orientation == "top":
            self.y += speed
        elif self.orientation == "right":
            self.x -= speed
        else:
            self.y -= speed

        if self.x < (0 - offset) or self.x > (self.display_width + offset) or self.y < (0 - offset) \
                or self.y > (self.display_height + offset):
            return False
        else:
            return True



