# for part 1 solution, store the ranges and do a linear scan of all ranges for
# each ingredient ID to check.
# consider building a binary search tree to store ranges and fresh / spoiled
# attributes for logarithmic checks in part 2.

import sys


class FreshnessDB:
    def __init__(self):
        self.fresh = []

    def Add(self, a, b):
        self.fresh.append((a, b))

    def CheckID(self, i):
        for a, b in self.fresh:
            if i >= a and i <= b:
                return True
        return False


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    i = lines.index('')
    ranges, ingredient_ids = lines[:i], lines[i + 1:]

    db = FreshnessDB()
    for r in ranges:
        a, b = [int(x) for x in r.split('-')]
        db.Add(a, b)

    count = 0
    for i in [int(x) for x in ingredient_ids]:
        if db.CheckID(i):
            count += 1
    print(count)
