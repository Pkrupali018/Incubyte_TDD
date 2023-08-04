class Coordinates:

    def __init__(self):
        # coordinates list contains east_west, north_south, above_below and initial_direction in order.
        self.coordinates = [0, 0, 0, 'N']

    # Add coordinates use when user wants to enter their own choice coordinates.
    def add_coordinates(self, ip_coordinates=''):
        if ip_coordinates != '':
            self.coordinates = ip_coordinates
        return self.coordinates

    # Get coordinates method useful when we will deal with other functionality of lunar carft like MOVE
    def get_coordinates(self):
        return self.coordinates


class Move:
    def __int__(self):
        self.after_forward = []
        self.after_backward = []

    def forward(self, input_coordinates):
        if input_coordinates[3] == 'E' or input_coordinates[3] == 'W':
            input_coordinates[0] += 1
        elif input_coordinates[3] == 'N' or input_coordinates[3] == 'S':
            input_coordinates[1] += 1
        elif input_coordinates[3] == 'U' or input_coordinates[3] == 'D':
            input_coordinates[2] += 1
            # coordinate.add_coordinates(self.coordinates[0], self.coordinates[1], self.coordinates[2], self.coordinates[3])
        return input_coordinates

    def backward(self, input_coordinates):
        if input_coordinates[3] == 'E' or input_coordinates[3] == 'W':
            input_coordinates[0] -= 1
        elif input_coordinates[3] == 'N' or input_coordinates[3] == 'S':
            input_coordinates[1] -= 1
        elif input_coordinates[3] == 'U' or input_coordinates[3] == 'D':
            input_coordinates[2] -= 1
        # coordinate.add_coordinates(self.coordinates[0], self.coordinates[1], self.coordinates[2], self.coordinates[3])
        return input_coordinates


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
        input_coordinates = [east_west, north_south, above_below, initial_direction]
        result = coordinate.add_coordinates(input_coordinates)
    else:
        result = coordinate.add_coordinates()

    no_of_commands = int(input("Enter the number how many commands you want to give: "))
    commands = []

    for i in range(0, no_of_commands):
        ele = input("Enter next command: ")
        commands.append(ele)

    for i in range(0, no_of_commands):
        if commands[i] == 'f':
            move = Move()
            coordinates = coordinate.get_coordinates()
            after_forward = move.forward(coordinates)
            coordinate.add_coordinates(after_forward)
        elif commands[i] == 'b':
            move = Move()
            coordinates = coordinate.get_coordinates()
            after_backward = move.backward(coordinates)
            coordinate.add_coordinates(after_backward)

    check = coordinate.get_coordinates()
    n = len(check)
    for i in range(0, n):
        print(check[i])
