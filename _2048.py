"""Algorithm for 2048 game."""

import random


OFFSETS = {'UP': (1, 0),
           'DOWN': (-1, 0),
           'LEFT': (0, 1),
           'RIGHT': (0, -1)}

def merge(line, reverse=False):
    target = line[:]
    if reverse:
        target.reverse()
    target.sort(key=lambda x:bool(x), reverse=True)
    for num in range(len(target)-1):
        if target[num] == target[num+1]:
            target[num] += target[num+1]
            target[num+1] = 0
            target.sort(key=lambda x:bool(x), reverse=True)
    if reverse:
        target.reverse()
    return target


class Gameplay:

    def __init__(self, grid_height=4, grid_width=4):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.state = True
        self.reset()

    def reset(self):
        self._grid = [[0 for num in range(self._grid_width)] 
                       for num in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        debug_str = ""
        for row in self._grid:
            debug_str += str(row) + "\n"
        return debug_str

    def get_grid_height(self):
        return self._grid_height

    def get_grid_width(self):
        return self._grid_width

    def get_state(self):
        return self.state

    def get_score(self):
        score = 0
        for row in self._grid:
            for num in row:
                score += num
        return score

    def move(self, direction):
        new_grid = [[0 for num in range(self._grid_width)] 
                      for num in range(self._grid_height)]

        # for row_num in range(self.grid_height):
        #     for col_num in range(self.grid_width):
        #         new_grid[row_num + OFFSETS[direction][0]][col_num + OFFSETS[direction][1]] = self.grid[row_num][col_num]
        temp_list = list()
        direction = str(direction)
        if OFFSETS[direction][0]:
            for num in range(self._grid_width):
                temp_list = list()
                for row in range(self._grid_height):
                    temp_list.append(self._grid[row][num])
                temp_list = merge(temp_list, reverse=(OFFSETS[direction][0]<0))
                for row in range(self._grid_height):
                    new_grid[row][num] = temp_list[row]
        else:
            for row in range(self._grid_height):
                new_grid[row] = merge(self._grid[row], reverse=(OFFSETS[direction][1]<0))
        if not self._grid == new_grid:
            self._grid = new_grid
            self.new_tile()
            return True
        else:
            self.check_state()
            return False

    def new_tile(self):
        blank_list = list()
        for row in range(self._grid_height):
            for num in range(self._grid_width):
                if self._grid[row][num] == 0:
                    blank_list.append((row, num))
        if blank_list:
            blank_pos = random.choice(blank_list)
            if random.random() <= 0.9:
                self._grid[blank_pos[0]][blank_pos[1]] = 2
            else:
                self._grid[blank_pos[0]][blank_pos[1]] = 4
        else:
            self.state = False

    def check_state(self):
        for row in self._grid:
            for num in row:
                if num == 0:
                    return True
        self.state = False

    def set_tile(self, row, col, value):
        self._grid[row][col] = value

    def get_tile(self, row, col):
        # replace with your code
        return self._grid[row][col]

    def set_grid(self, grid):
        self._grid = grid

    def clone(self):
        new_clone = Gameplay(self._grid_height, self._grid_width)
        new_clone.set_grid(self._grid)
        return new_clone



# poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
