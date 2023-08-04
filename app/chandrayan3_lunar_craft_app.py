class Coordinates:

    def __init__(self):
        self.east_west = 0
        self.north_south = 0
        self.above_below = 0
        self.initial_direction = 'N'

    def add_coordinates(self, e_w='', n_s='', a_b='', ini_direction=''):
        coordinates = []
        if e_w != '':
            coordinates = [e_w, n_s, a_b, ini_direction]
        else:
            coordinates = [self.east_west, self.north_south, self.above_below, self.initial_direction]
        return coordinates


if __name__ == '__main__':
    coordinate = Coordinates()

    status = input("If you want to add your own coordinates then write yes otherwise use default coordinates by writhing no: ")

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
