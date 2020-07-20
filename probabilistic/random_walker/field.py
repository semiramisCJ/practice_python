class Field:
    def __init__(self):
        self.walker_coordinates = {}

    def add_walker(self, walker, coordinate):
        self.walker_coordinates.update({walker: coordinate})
    
    def move_walker(self, walker):
        delta_x, delta_y = walker.walk() # this returns a coordinate
        current_coordinate = self.walker_coordinates[walker]
        new_coordinate = current_coordinate.move(delta_x, delta_y)
        self.walker_coordinates[walker] = new_coordinate
    
    def get_coordinate(self, walker):
        return self.walker_coordinates[walker]
