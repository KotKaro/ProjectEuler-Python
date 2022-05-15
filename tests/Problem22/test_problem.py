import unittest

from problems.Problem22.problem import calculate_value_for_str


class TestsProblem22(unittest.TestCase):

    def test_calculate_value_for_str_for_COLIN_with_index_938_returns_49714(self):
        result = calculate_value_for_str("colin", 938)
        self.assertEqual(49714, result)


if __name__ == '__main__':
    unittest.main()
