import random


class Player:
    def __init__(self, x, y, icon):
        self.icon = icon
        self.x = x
        self.y = y
        self.score = 0
        self.lifes = 3
        self.strong = False
    

class Enemy:
    def __init__(self, icon):
        self.icon = icon
        self.x = random.randint(0, 960 - 64)
        self.y = random.randint(0, 600 - 64)