import random

class field:

    EMPTY = '0'

    def __init__(self, x=10, y=10, mines=10):
        self.x = x
        self.y = y
        self.mines = mines
        self.grid = []

        for row in range(self.x):
            self.grid.append([])
            for column in range(self.y):
                self.grid[-1].append(self.EMPTY)

    def place_mine(self):
        for i in range(self.mines):
            mine = (random.randint(0, self.x-1), random.randint(0, self.y-1))
            self.grid[mine[0]][mine[1]] = 'X'

    def place_helpers(self):
        for row in range(self.x):
            for column in range(self.y):
                print(row, column)
                if self.grid[row][column] == 'X':
                    continue
                self.grid[row][column] = '-'
                counter = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if row + i == -1 or row + i == self.x:
                            continue
                        if column + j == -1 or column + j == self.y:
                            continue
                        counter += 1 if self.grid[row + i][column + j] == 'X' else 0
                self.grid[row][column] = str(counter)


    def get_field(self, line, column):
        return self.grid[line][column]


new_field = field()

new_field.place_mine()
new_field.place_helpers()


print('    0 1 2 3 4 5 6 7 8 9')
print('    ___________________')
for index, row in enumerate(new_field.grid):
    print(str(index) + " | " + ' '.join(row))

choosenY = input("Line:")
choosenX = input("Column:")


print(new_field.get_field(3,4))