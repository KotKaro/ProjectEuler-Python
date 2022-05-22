import unittest

from problems.Problem788.problem import count_of_dominating_numbers_in_power, \
    count_of_dominating_numbers_to_power


class TestsProblem24(unittest.TestCase):

    def test_count_of_dominating_numbers_in_power_should_return_expected_count(self):
        parameter_result = [
            [3, 252],
            [4, 333],
            [5, 7704],
            [6, 11430],
            [7, 245520],
            [8, 388485],
            [9, 8018280],
            [10, 13221234]
        ]
        for number, expected_result in parameter_result:
            with self.subTest('{0} -> {1}'.format(number, expected_result)):
                # act
                result = count_of_dominating_numbers_in_power(number)

                # assert
                self.assertEqual(result, expected_result)

    def test_count_of_dominating_numbers_to_power_should_return_expected_count_1(self):
        # act
        result = count_of_dominating_numbers_in_power(5)

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
