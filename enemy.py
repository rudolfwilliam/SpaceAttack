class Enemy:

    def __init__(self, figure, display_width, display_height, start_x, start_y):
        self.figure = figure
        self.display_width = display_width
        self.display_height = display_height
        self.x = start_x
        self.y = start_y

    def move(self):
        offset = 100

        if self.x < self.figure.x:
            self.x += 2

        elif self.x > self.figure.x:
            self.x -= 2

        if self.y < self.figure.y:
            self.y += 2

        elif self.y > self.figure.y:
            self.y -= 2

        if self.x < (0 - offset) or self.x > (self.display_width + offset) or self.y < (0 - offset) \
                or self.y > (self.display_height + offset):
            return False
        else:
            return True