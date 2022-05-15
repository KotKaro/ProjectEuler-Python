import unittest

from problems.Problem21.problem import get_amicable_numbers_in_range, get_sum_of_amicable_numbers_in_range


class TestsProblem21(unittest.TestCase):

    def test_get_amicable_numbers_in_range_for_500_returns_220_and_284(self):
        result = list(get_amicable_numbers_in_range(1, 500))
        self.assertEqual(220, result[0])
        self.assertEqual(284, result[1])

    def test_get_sum_of_amicable_numbers_in_range_from_1_to_500_returns_504(self):
        result = get_sum_of_amicable_numbers_in_range(1, 500)
        self.assertEqual(504, result)

    def test_get_sum_of_amicable_numbers_in_range_from_1_to_10000_returns_504(self):
        result = get_sum_of_amicable_numbers_in_range(1, 10000)
        self.assertEqual(31626, result)


if __name__ == '__main__':
    unittest.main()
