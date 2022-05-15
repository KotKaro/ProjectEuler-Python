import unittest
from datetime import datetime

from problems.Problem19.problem import is_leap_year, get_all_sundays_between_days, get_first_sunday_date_from, \
    get_all_sundays_between_days_which_are_first_day_of_month


class TestStringMethods(unittest.TestCase):

    def test_is_leap_year_return_true_for_2020(self):
        self.assertEqual(True, is_leap_year(2020))

    def test_is_leap_year_return_true_for_2000(self):
        self.assertEqual(True, is_leap_year(2000))

    def test_is_leap_year_returns_false_for_1900(self):
        self.assertEqual(False, is_leap_year(1900))

    def test_get_first_sunday_date_from_providing_15_may_2022_should_return_same_date_as_original(self):
        date = datetime(2022, 5, 15)

        result = get_first_sunday_date_from(date)

        self.assertEqual(date.day, result.day)
        self.assertEqual(date.month, result.month)
        self.assertEqual(date.year, result.year)

    def test_get_first_sunday_date_from_providing_9_may_2022_should_return_15_may_2022(self):
        date = datetime(2022, 5, 9)

        result = get_first_sunday_date_from(date)
        self.assertEqual(15, result.day)
        self.assertEqual(5, result.month)
        self.assertEqual(2022, result.year)

    def test_get_all_sundays_between_days_raises_value_error_if_start_date_is_greater_than_stop_date(self):
        self.assertRaises(ValueError, lambda: get_all_sundays_between_days(datetime(1902, 1, 1), datetime(1901, 1, 1)))

    def test_get_all_sundays_between_days_returns_52_sundays_in_2021_returns_52_sundays(self):
        sundays = get_all_sundays_between_days(datetime(2021, 1, 1), datetime(2021, 12, 31))
        self.assertEqual(52, len(sundays))

    def test_get_all_sundays_between_days_returns_53_sundays_in_2017_returns_53_sundays(self):
        sundays = get_all_sundays_between_days(datetime(2017, 1, 1), datetime(2017, 12, 31))
        self.assertEqual(53, len(sundays))

    def test_get_all_sundays_between_days_1_1_2017_to_31_12_2022_should_return_expected_count(self):
        sundays_in_2017 = 53
        sundays_in_2018 = 52
        sundays_in_2019 = 52
        sundays_in_2020 = 52
        sundays_in_2021 = 52
        sundays_in_2022 = 52
        sundays_in_2023 = 53

        total = sundays_in_2017 + sundays_in_2018 + sundays_in_2019 + sundays_in_2020 + sundays_in_2021 + sundays_in_2022 + sundays_in_2023

        sundays = get_all_sundays_between_days(datetime(2017, 1, 1), datetime(2023, 12, 31))
        self.assertEqual(total, len(sundays))

    def test_get_all_sundays_between_days_from_1_1_1901_to_31_12_2000_return_5218_sundays(self):
        sundays = get_all_sundays_between_days(datetime(1901, 1, 1), datetime(2000, 12, 31))
        self.assertEqual(5218, len(sundays))

    def test_get_all_sundays_between_days_from_1_1_1901_to_31_12_2000_return_5218_sundays(self):
        sundays = get_all_sundays_between_days_which_are_first_day_of_month(datetime(1901, 1, 1),
                                                                            datetime(2000, 12, 31))
        self.assertEqual(171, len(sundays))


if __name__ == '__main__':
    unittest.main()
