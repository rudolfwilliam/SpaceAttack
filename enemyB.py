from enemy import Enemy

class EnemyB(Enemy):

    def __init__(self, figure, display_width, display_height, start_x, start_y):
        Enemy.__init__(self, figure, display_width, display_height, start_x, start_y)

    def get_kind(self):
        return "B"