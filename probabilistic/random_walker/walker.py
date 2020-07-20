import random

class Walker:
    def __init__(self, name):
        self.name = name

class TraditionalWalker(Walker):
    def __init__(self, name):
        super().__init__(name = name)
    def walk(self):
        coords = [(0,1), (0,-1),
                  (1,0), (-1,0)]
        return random.choice(coords)

