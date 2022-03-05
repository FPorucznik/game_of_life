import numpy as np


class Grid():
    def __init__(self, size):
        self.size = size
        self.p0 = 0.25
        self.state = self.generate_empty_state()
        #self.state = self.generate_random_state()

    def generate_empty_state(self):
        return np.zeros((self.size, self.size))

    def generate_random_state(self):
        return np.random.choice(a=[0, 1], size=(self.size, self.size),
                                replace=True, p=[1-self.p0, self.p0])

    def reset_state(self):
        self.state = self.generate_random_state()

    def count_neighbours(self, row, col):
        count = 0

        if row < self.size - 1:
            rp = row + 1
        else:
            rp = 0

        if row > 0:
            rm = row - 1
        else:
            rm = self.size - 1

        if col < self.size - 1:
            cp = col + 1
        else:
            cp = 0

        if col > 0:
            cm = col - 1
        else:
            cm = self.size - 1

        count += (self.state[rm][col] + self.state[rp][col] +
                  self.state[row][cp] + self.state[row][cm] +
                  self.state[rm][cp] + self.state[rp][cm] +
                  self.state[rm][cm] + self.state[rp][cp])
        return count

    def update(self):
        newState = self.state.copy()

        for row in range(self.size):
            for col in range(self.size):
                neighbours_count = self.count_neighbours(row, col)
                if self.state[row][col] == 1:
                    if neighbours_count < 2 or neighbours_count > 3:
                        newState[row][col] = 0
                else:
                    if neighbours_count == 3:
                        newState[row][col] = 1

        self.state = newState.copy()
