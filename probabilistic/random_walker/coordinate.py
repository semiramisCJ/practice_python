class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Coordinate(self.x + delta_x, self.y + delta_y)
    
    def distance(self, new_coordinate):
        delta_x = self.x - new_coordinate.x
        delta_y = self.y - new_coordinate.y
        # Result is obtained by the formula c**2 = a**2 + b**2
        result = (delta_x**2 + delta_y**2)**0.5
        return result
