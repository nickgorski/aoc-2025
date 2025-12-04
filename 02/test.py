from importlib import import_module
import unittest

day_02 = import_module('02')


class TestIsInvalid(unittest.TestCase):
    def test_products(self):
        self.assertFalse(day_02.IsInvalid(12))

        self.assertTrue(day_02.IsInvalid(11))
        self.assertTrue(day_02.IsInvalid(22))

        self.assertTrue(day_02.IsInvalid(99))
        self.assertTrue(day_02.IsInvalid(111))

        self.assertTrue(day_02.IsInvalid(999))
        self.assertTrue(day_02.IsInvalid(1010))


if __name__ == '__main__':
    unittest.main()
