import unittest
from datetime import datetime

from problems.Problem19.problem import is_leap_year, get_all_sundays_between_days, get_first_sunday_date_from, \
    get_all_sundays_between_days_which_are_first_day_of_month
from problems.Problem20.problem import get_factorial, get_digits_sum_for_factorial


class TestsProblem20(unittest.TestCase):

    def test_get_factorial_return_6_for_number_3(self):
        result = get_factorial(3)
        self.assertEqual(6, result)

    def test_get_factorial_returns_correct_number_for_factorial_of_100(self):
        result = get_factorial(100)
        self.assertEqual(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, result)

    def test_get_digits_sum_for_factorial_returns_648_for_factorial_of_100(self):
        result = get_digits_sum_for_factorial(100)
        self.assertEqual(648, result)


if __name__ == '__main__':
    unittest.main()
