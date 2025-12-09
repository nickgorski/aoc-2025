from functools import cmp_to_key
import sys


# Simple brute force for part 1.
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

# Part 2.
class Intervals:
    START = 'start'
    END = 'end'

    def __init__(self, ranges):
        i = []
        for r in ranges:
            a, b = [int(x) for x in r.split('-')]
            i.append((a, Intervals.START))
            i.append((b, Intervals.END))
        self.i = sorted(i, key=cmp_to_key(Intervals.interval_compare))

    def CountFresh(self):
        total, fresh_overlap, fresh_start = 0, 0, None
        for x in range(len(self.i)):
            if self.i[x][1] == Intervals.START:
                if fresh_overlap == 0:
                    fresh_start = self.i[x][0]
                fresh_overlap += 1
            elif self.i[x][1] == Intervals.END:
                fresh_overlap -= 1
                if fresh_overlap == 0:
                    total += self.i[x][0] - fresh_start + 1
            else:
                raise Exception('Bad label.')
        return total

    def interval_compare(x, y):
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        else:
            if x[1] == Intervals.START and y[1] == Intervals.END:
                return 1
            elif x[1] == Intervals.END and y[1] == Intervals.START:
                return -1
            else:
                return 0


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

    intervals = Intervals(ranges)
    print(intervals.CountFresh())
