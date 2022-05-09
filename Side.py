class Side:
    def __init__(self, size, color):
        self.matrix = [[color for _ in range(size)] for _ in range(size)]

    def rotate(self, reverse=False):
        if reverse:
            self.matrix = list([list(x) for x in zip(*self.matrix)])[::-1]
        else:
            self.matrix = list([list(x) for x in zip(*self.matrix[::-1])])
