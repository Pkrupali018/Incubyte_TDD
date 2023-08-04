class Coordinates:

    def __init__(self):
        # coordinates list contains east_west, north_south, above_below and initial_direction in order.
        self.coordinates = [0, 0, 0, 'N']

    # Add coordinates use when user wants to enter their own choice coordinates.
    def add_coordinates(self, e_w='', n_s='', a_b='', ini_direction=''):
        if e_w != '':
            self.coordinates = [e_w, n_s, a_b, ini_direction]
        return self.coordinates

    # Get coordinates method useful when we will deal with other functionality of lunar carft like MOVE
    def get_coordinates(self):
        return self.coordinates


if __name__ == '__main__':

    # Create object of coordinate class
    coordinate = Coordinates()

    status = input("If you want to add your own coordinates then write yes otherwise use default coordinates by "
                   "writhing no: ")

    # If user want to enter their own choice coordinates then use this
    if status == "yes":
        east_west = int(input("Enter value for east or west from origin: "))
        north_south = int(input("Enter value for north or south from origin: "))
        above_below = int(input("Enter value for above or below from origin: "))
        initial_direction = input("Enter value for initial direction: ")
        result = coordinate.add_coordinates(east_west, north_south, above_below, initial_direction)
    else:
        result = coordinate.add_coordinates()

    n = len(result)
    for i in range(0, n):
        print(result[i])
