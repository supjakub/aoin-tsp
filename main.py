class Coordinates:
    x = None
    y = None

    def __init__(self, line):
        array = line.split()
        self.x = array[1]
        self.y = array[2]

file_name = input('Wpisz nazwe pliku: ')
file = open(file_name)
line = file.readline()
while 'NODE_COORD_SECTION' not in line:
    line = file.readline()
size = 0
cities = []
line = file.readline()
cities = []
while 'EOF' not in line:
    size = size + 1
    cities.append(Coordinates(line))
    line = file.readline()