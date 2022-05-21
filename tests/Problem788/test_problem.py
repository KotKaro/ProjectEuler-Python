import unittest

from problems.Problem788.problem import is_dominating_number, count_of_dominating_numbers_in_power, \
    count_of_dominating_numbers_to_power, count_of_dominating_numbers_to_power_slow


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

    def test_count_of_dominating_numbers_in_power_should_return_expected_count(self):
        parameter_result = [
            [3, 252],
            [4, 333],
            [5, 7704]
        ]
        for number, expected_result in parameter_result:
            with self.subTest('{0} -> {1}'.format(number, expected_result)):
                # act
                result = count_of_dominating_numbers_in_power(number)

                # assert
                self.assertEqual(result, expected_result)

    def test_count_of_dominating_numbers_to_power_slow_should_return_expected_count(self):
        parameter_result = [
            [3, 252],
            [4, 333],
            [5, 7704],
            # without zero should be 6129
            # with zero should be 1575
            [10, 21893256]
        ]
        for number, expected_result in parameter_result:
            with self.subTest('{0} -> {1}'.format(number, expected_result)):
                # act
                result = count_of_dominating_numbers_to_power_slow(number)

                # assert
                self.assertEqual(result, expected_result)

    def test_count_of_dominating_numbers_to_power_should_return_expected_count_1(self):
        # act
        result = count_of_dominating_numbers_in_power(5)

        # assert
        self.assertEqual(result, 7704)

    def test_count_of_dominating_numbers_to_power_slow_should_return_expected_count_1(self):
        # act
        result = count_of_dominating_numbers_to_power_slow(5, 0, 1)

        # assert
        self.assertEqual(result, 7704)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to10power_is_21893256(self):
        result = count_of_dominating_numbers_to_power(10)
        self.assertEqual(21893256, result)

    def test_count_of_dominating_numbers_in_range_from_1_to_10to10power_is_21893256_1(self):
        result = count_of_dominating_numbers_to_power(2022)
        self.assertEqual(21893256, result)


if __name__ == '__main__':
    unittest.main()
