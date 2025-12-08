import sys


class Model:
    def __init__(self, filename):
        with open(filename, 'r') as in_file:
            lines = [x.strip() for x in in_file.readlines()]
        self.width, self.height = len(lines[0]), len(lines)
        self.m = [['.' for i in range(self.width)] for j in range(self.height)]
        
        for j in range(self.height):
            for i in range(self.width):
                self.m[j][i] = lines[j][i]

    def IsValidPos(self, j, i):
        return j >= 0 and j < self.height and i >= 0 and i < self.width

    def GetAllAdjacents(self, j, i):
        adjacents = []
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if self.IsValidPos(j + y, i + x) and (y != 0 or x != 0):
                    adjacents.append(self.m[j + y][i + x])
        return adjacents

    def GetCell(self, j, i):
        return self.m[j][i]

    def GetAccessible(self):
        accessible = []
        for j in range(m.height):
            for i in range(m.width):
                if m.GetCell(j, i) == '@' and m.GetAllAdjacents(j, i).count('@') < 4:
                    accessible.append((j, i))
        return accessible

    def Remove(self, positions):
        for c in positions:
            j, i = c
            self.m[j][i] = '.'


if __name__ == '__main__':
    m = Model(sys.argv[1])
    accessible = m.GetAccessible()
    count = 0
    while len(accessible) > 0:
        count += len(accessible)
        m.Remove(accessible)
        accessible = m.GetAccessible()
    print(count)
