class Figure:
    def __init__(self, x, y, display_width, display_height):
        self.x = x
        self.y = y
        self.display_width = display_width
        self.display_height = display_height

    def move(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change

        if self.x < 0 or self.x > self.display_width - 26 or self.y < 0 or self.y > self.display_height - 26:
            return False
        else:
            return True