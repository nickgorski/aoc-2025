import unittest

from day_03 import EvaluateJoltage, GreedyEvaluateJoltage


class TestDay03(unittest.TestCase):
    def test_evaluate_joltage(self):
        self.assertEquals(EvaluateJoltage('987654321111111'), '98')
        self.assertEquals(EvaluateJoltage('811111111111119'), '89')
        self.assertEquals(EvaluateJoltage('234234234234278'), '78')
        self.assertEquals(EvaluateJoltage('818181911112111'), '92')

    def test_evaluate_greedy_joltage(self):
        self.assertEquals(GreedyEvaluateJoltage('987654321111111', 2), '98')
        self.assertEquals(GreedyEvaluateJoltage('811111111111119', 2), '89')
        self.assertEquals(GreedyEvaluateJoltage('234234234234278', 2), '78')
        self.assertEquals(GreedyEvaluateJoltage('818181911112111', 2), '92')

        self.assertEquals(GreedyEvaluateJoltage('987654321111111', 12), '987654321111')
        self.assertEquals(GreedyEvaluateJoltage('811111111111119', 12), '811111111119')
        self.assertEquals(GreedyEvaluateJoltage('234234234234278', 12), '434234234278')
        self.assertEquals(GreedyEvaluateJoltage('818181911112111', 12), '888911112111')


if __name__ == '__main__':
    unittest.main()
