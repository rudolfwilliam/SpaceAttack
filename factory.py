from enemy import Enemy
from enemyA import EnemyA
from enemyB import EnemyB
from enemyC import EnemyC
from comet import Comet
import random

class Factory:

    def __init__(self, figure, display_width, display_height):
        self.figure = figure
        self.display_width = display_width
        self.display_height = display_height

    def createRandomEnemy(self):

        orientation = random.choice(["left", "top", "right", "bottom"])

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

        kind = random.choice(["A", "B", "C"])

        if kind == "A":
            return EnemyA(self.figure, self.display_width, self.display_height, x, y)
        elif kind == "B":
            return EnemyB(self.figure, self.display_width, self.display_height, x, y)
        else:
            return EnemyC(self.figure, self.display_width, self.display_height, x, y)

    def createRandomComet(self):
        return Comet(self.display_width, self.display_height, random.choice(["top", "left", "bottom", "right"]))