from math import prod
import sys


class Table:
    def __init__(self, filename):
        with open(filename, 'r') as in_file:
            lines = [x.strip().split() for x in in_file.readlines()]
        self.width, self.height = len(lines[0]), len(lines)
        self.m = [[0 for i in range(self.width)] for j in range(self.height)]
        
        for j in range(self.height):
            for i in range(self.width):
                self.m[j][i] = lines[j][i]

    def ComputeColumn(self, i):
        if self.m[-1][i] == '*':
            return prod([int(self.m[x][i]) for x in range(self.height - 1)])
        elif self.m[-1][i] == '+':
            return sum([int(self.m[x][i]) for x in range(self.height - 1)])
        else:
            raise Exception('Invalid operand:', self.m[-1][i])

    def Solve(self):
        return sum([self.ComputeColumn(i) for i in range(self.width)])


class Grid:
    def __init__(self, filename):
        with open(filename, 'r') as in_file:
            lines = [x[:-1] for x in in_file.readlines()]
        self.width, self.height = len(lines[0]), len(lines)
        self.g = [[' ' for i in range(self.width)] for j in range(self.height)]

        for j in range(self.height):
            for i in range(self.width):
                self.g[j][i] = lines[j][i]

    def Solve(self):
        operands = []
        total = 0
        for i in range(self.width - 1, -1, -1):
            val = ''.join([self.g[j][i] for j in range(self.height)]).strip()
            if val != '':
                if val[-1] == '*':
                    operands.append(int(val[:-1]))
                    total += prod(operands)
                elif val[-1] == '+':
                    operands.append(int(val[:-1]))
                    total += sum(operands)
                else:
                    operands.append(int(val))
            else:
                operands = []
        return total

if __name__ == '__main__':
    g = Grid(sys.argv[1])
    print(g.Solve())
