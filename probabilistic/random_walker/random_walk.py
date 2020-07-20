from bokeh.plotting import figure, show

from walker import TraditionalWalker
from field import Field
from coordinate import Coordinate

def walk(field, walker, steps):
    #start = field.get_coordinate(walker)
    for _ in range(steps):
        field.move_walker(walker)
    # Return the final state
    return field.get_coordinate(walker)

def walk_simulator(steps, times, walker):
    """
    This function can accept different 
    Walker classes as the last parameter
    for example, a TraditionalWalker
    """
    current_walker = walker(name="Pepito")
    origin = Coordinate(0, 0)
    coordinates_walked = []
    for _ in range(times):
        field = Field()
        field.add_walker(walker, origin)
        walk_simulation = walk(field, current_walker, steps)
        coordinates_walked.append(walk_simulation)
    return coordinates_walked

def plot_walk(x_coords, y_coords):
    fig = figure(title='Random walk')
    fig.line(x_coords, y_coords)
    show()

def main(steps, times, walker):
    for step in steps:
        coordinates_walked = walk_simulator(step, times, walker)
        print(coordinates_walked)

if __name__ == "__main__":
    steps = [10, 100, 1000]
    times = 100
    main(steps, times, TraditionalWalker)