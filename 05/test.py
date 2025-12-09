import unittest

from day_05 import Intervals


class TestDay05(unittest.TestCase):
    def test_intervals(self):
        intervals = Intervals(['4-7', '8-12', '12-13'])

    def test_interval_internal_sort_order(self):
        intervals = Intervals(['8-12', '12-13'])
        self.assertEquals(intervals.i[1][1], Intervals.END)
        self.assertEquals(intervals.i[2][1], Intervals.START)
        

if __name__ == '__main__':
    unittest.main()
