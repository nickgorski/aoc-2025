from collections import defaultdict
import sys

class Dial:
    def __init__(self):
        self.p = 50
        self.zeroes = 0
        self.counts = defaultdict(int)

    def Turn(self, r):
        """Turn the dial left or right a set distance, e.g. L7."""
        direction, distance = r[0], int(r[1:])

        if direction == 'L':
            while distance > 0:
                distance -= 1
                self.p -= 1
                if self.p < 0:
                    self.p += 100
                if self.p == 0:
                    self.zeroes += 1
        elif direction == 'R':
            while distance > 0:
                distance -= 1
                self.p += 1
                if self.p >= 100:
                    self.p -= 100
                if self.p == 0:
                    self.zeroes += 1
        else:
            raise Exception('Invalid rotation: %s' % r)
        self.counts[self.p] += 1


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input_file:
        lines = [x.strip() for x in input_file.readlines()]

    dial = Dial()
    for line in lines:
        dial.Turn(line)

    print(dial.counts[0], dial.zeroes)
