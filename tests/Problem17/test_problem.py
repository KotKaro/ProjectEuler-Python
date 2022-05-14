import unittest

from problems.Problem17.problem import parse_number_to_word, get_letters_count_in_range_without_spaces


class TestStringMethods(unittest.TestCase):

    def test_parse_number_to_word_should_return_expected_word_representing_number(self):
        parameter_result = [
            [10, 'ten'],
            [17, 'seventeen'],
            [19, 'nineteen'],
            [47, 'forty seven'],
            [59, 'fifty nine'],
            [77, 'seventy seven'],
            [99, 'ninety nine'],
            [100, 'one hundred'],
            [200, 'two hundred'],
            [268, 'two hundred and sixty eight'],
            [471, 'four hundred and seventy one'],
            [789, 'seven hundred and eighty nine'],
            [999, 'nine hundred and ninety nine'],
            [9999, 'nine thousand nine hundred and ninety nine'],
        ]
        for number, expected_word in parameter_result:
            with self.subTest():
                # act
                result = parse_number_to_word(number)

                # assert
                self.assertEqual(result, expected_word)

    def test_get_letters_count_in_range_without_spaces_throws_error_if_start_is_grater_than_stop(self):
        self.assertRaises(ValueError, lambda: get_letters_count_in_range_without_spaces(12, 11))

    def test_get_letters_count_in_range_without_spaces_returns_expected_letters_count_for_provided_range(self):
        parameter_result = [
            [1, 5, len('one two three four five'.replace(' ', ''))],
            [22, 28,
             len('twenty two twenty three twenty four twenty five twenty six twenty seven twenty eight'.replace(' ',
                                                                                                                ''))],
            [342, 342, len('three hundred and forty two'.replace(' ', ''))],
            [1, 1000, 21124]
        ]
        for start, stop, expected_count in parameter_result:
            with self.subTest():
                # act
                result = get_letters_count_in_range_without_spaces(start, stop)

                # assert
                self.assertEqual(result, expected_count)


if __name__ == '__main__':
    unittest.main()
