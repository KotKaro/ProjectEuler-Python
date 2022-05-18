import math
import unittest

from problems.Problem788.problem import is_dominating_number, count_of_dominating_numbers_in_power, \
    count_of_dominating_numbers_to_power, count_of_dominating_numbers_to_power_slow, count_of_dominating_numbers_in_power_slow


class TestsProblem24(unittest.TestCase):

    def test_is_dominating_number_for_2022_returns_true(self):
        result = is_dominating_number(2022)
        self.assertEqual(True, result)

    def test_is_dominating_number_for_1999_returns_true(self):
        result = is_dominating_number(1999)
        self.assertEqual(True, result)

    def test_is_dominating_number_for_1337_returns_false(self):
        result = is_dominating_number(1337)
        self.assertEqual(False, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to2power_is_18(self):
        result = count_of_dominating_numbers_to_power(2)
        self.assertEqual(18, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to3power_is_252(self):
        result = count_of_dominating_numbers_to_power(3)
        self.assertEqual(270, result)

    def test_count_of_dominating_numbers_in_power_3_is_252(self):
        #X00 = 9
        #XX_ = 9 * 9 = 81
        #x_x = 9 * 9 = 81
        #_xx = 9 * 8 = 72
        #xxx = 9
        #180 + 72 = 252
        result = count_of_dominating_numbers_in_power(3)
        self.assertEqual(252, result)

    def test_count_of_dominating_numbers_in_power_5_is_7704(self):
        # without zero should be 6129
        # with zero should be 1575
        result = count_of_dominating_numbers_in_power(5)
        # result = count_of_dominating_numbers_in_power_slow(5)
        self.assertEqual(7704, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to4power_is_603(self):
        result = count_of_dominating_numbers_to_power(4)
        self.assertEqual(603, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to5power_is_8307(self):
        result = count_of_dominating_numbers_to_power(5)
        self.assertEqual(8307, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to10power_is_21893256(self):
        result = count_of_dominating_numbers_to_power(10)
        self.assertEqual(21893256, result)


if __name__ == '__main__':
    unittest.main()
